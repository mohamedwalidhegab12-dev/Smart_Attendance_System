import cv2
import sqlite3
import numpy as np
import threading
import time
from datetime import datetime
from PyQt5.QtCore import QTimer, Qt, QThread, pyqtSignal

# Import external business logic functions
from Mark_attendance import mark_attendance
from Compare_with_database import compare_with_database
from Embedding_pic import get_embedding

from threading import Lock
# Thread lock to prevent race conditions when accessing shared TensorFlow resources
tf_lock = Lock()

class CameraThread(QThread):
    # Signals to communicate with the Main GUI Thread
    frame_ready = pyqtSignal(np.ndarray)     # Sends the processed frame for display
    attendance_marked = pyqtSignal(dict)    # Sends student data upon successful database entry
    already_marked = pyqtSignal(str)        # Sends a notification if student is already recorded
    
    def __init__(self, lecture_id):
        super().__init__()
        self.lecture_id = lecture_id
        self.running = True
        # Load the pre-trained Haar Cascade for initial face detection
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.is_registering = False 
        self.start_hour = datetime.now().hour # Track start time to auto-stop if lecture hour changes
        
        self.is_processing = False           # Flag to ensure only one face is processed at a time
        self.current_face_box = None  
        
        # Color definitions (BGR format) for the UI bounding box
        self.COLOR_BLUE = (255, 0, 0)   # Default: Scanning or Liveness check in progress
        self.COLOR_GREEN = (0, 255, 0)  # Success: Authorized student recognized
        self.COLOR_RED = (0, 0, 255)    # Alert: Face detected but not in database
        
        self.box_color = self.COLOR_BLUE 
        self.box_label = "Scanning"    

        self.last_seen_times = {}       # Local cache to prevent duplicate database writes in one session
        self.cooldown_period = 60       # Minimum seconds before re-logging the same person

    def is_real_human(self, face_img):
        """
        Liveness Detection Logic:
        Differentiates between a physical human presence and a 2D image (phone screen/paper).
        Uses Laplacian variance for texture analysis and YCrCb variance for color depth.
        """
        if face_img is None or face_img.size == 0: return False
        
        # Analyze texture/sharpness: Photos/Screens usually have unnatural blur or moiré patterns
        gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
        texture_score = cv2.Laplacian(gray, cv2.CV_64F).var()
        
        # Analyze color distribution: Human skin has specific Cr channel variance compared to screens
        ycrcb = cv2.cvtColor(face_img, cv2.COLOR_BGR2YCrCb)
        _, cr, _ = cv2.split(ycrcb)
        color_score = cr.var()
        
        # Valid human face usually falls within these specific texture and color variance ranges
        return (70 < texture_score < 500) and (color_score > 35)

    def process_recognition(self, face_crop):
        """
        Background Recognition Task:
        Converts face to embedding, matches against DB, and triggers attendance logging.
        """
        self.is_processing = True
        try:
            with tf_lock:
                # Generate a mathematical vector representation (Embedding) of the face
                current_vec = get_embedding(face_crop)
                # Compare the vector against the authorized students in the SQLite database
                student_id = compare_with_database(current_vec)

            if student_id:
                # Face matched: Update UI to Green and display ID
                self.box_color = self.COLOR_GREEN
                self.box_label = " Accepted "
                
                current_time = time.time()
                last_time = self.last_seen_times.get(student_id, 0)
                
                # Double-check Cooldown: Prevent redundant DB API calls
                if current_time - last_time > self.cooldown_period:
                    
                    # Write record to 'Attendance' table
                    result = mark_attendance(student_id, self.lecture_id)
                    
                    if result["status"] == "success":
                        self.last_seen_times[student_id] = current_time
                        self.attendance_marked.emit(result["data"])
                    elif result["status"] == "already_marked":
                        self.already_marked.emit(result["message"])
            else:
                # Face is human, but no matching embedding found in database
                self.box_color = self.COLOR_RED
                self.box_label = "Unknown"
        except Exception as e:
            print(f"Recognition Error: {e}")
        finally:
            self.is_processing = False

    def run(self):
        """
        Main Camera Loop:
        Handles frame acquisition, performance scaling, and visual feedback.
        """
        # Open camera using DirectShow for faster initialization on Windows
        cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW) 
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1) # Reduce lag by keeping only the latest frame in buffer
    
        frame_count = 0 
        scale = 0.5 # Scale factor (50%) to speed up Haar Cascade processing

        while self.running:
            # Safety exit: Stop thread if system time moves past the lecture start hour
            if datetime.now().hour != self.start_hour:
                break

            ret, frame = cap.read()
            if not ret: break

            frame = cv2.flip(frame, 1) # Mirror the frame for more natural user interaction
            frame_count += 1

            # PERFORMANCE OPTIMIZATION: Only detect faces every 2nd frame to save CPU
            if frame_count % 10 == 0:
                # Resize frame for faster detection calculation
                small_frame = cv2.resize(frame, (0, 0), fx=scale, fy=scale)
                gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)

                if len(faces) == 1:
                    # Map detection coordinates back to the original full-size frame
                    (x, y, w, h) = [int(v / scale) for v in faces[0]]
                    self.current_face_box = (x, y, w, h)
                    face_roi = frame[y:y+h, x:x+w].copy()

                    # SECURITY CHECK: Liveness Test
                    if self.is_real_human(face_roi):
                        # Only initiate Recognition if the box is currently 'Scanning' (Blue)
                        # This prevents constant heavy CPU usage once a person is already known
                        if self.box_color == self.COLOR_BLUE:
                            self.box_label = "Verifying Identity"
                            if not self.is_registering and not self.is_processing:
                                # Trigger heavy recognition in a separate thread every 10 frames
                                if frame_count % 10 == 0:
                                    threading.Thread(target=self.process_recognition, args=(face_roi,)).start()
                    else:
                        # Spoofing detected: Reset box to blue and warn
                        self.box_color = self.COLOR_BLUE
                        self.box_label = "Real face required"
                else:
                    # Clean up: Reset UI state when nobody is looking at the camera
                    self.current_face_box = None
                    self.box_color = self.COLOR_BLUE
                    self.box_label = "Scanning"

            # GRAPHICS: Draw the bounding box and label directly on the frame
            if self.current_face_box:
                (x, y, w, h) = self.current_face_box
                cv2.rectangle(frame, (x, y), (x+w, y+h), self.box_color, 2)
                cv2.putText(frame, self.box_label, (x, y-10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, self.box_color, 2)

            # Emit the final frame to be displayed in the QLabel
            self.frame_ready.emit(frame)

        cap.release()

    def stop(self):
        """Safe thread termination"""
        self.running = False
        self.wait()