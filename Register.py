import sys
import cv2
import sqlite3
import os
import pickle
from deepface import DeepFace
from Embedding_pic import get_embedding
from DB_Students import insert_student
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QComboBox, 
                             QFormLayout, QFrame, QMessageBox)
from PyQt5.QtCore import QPropertyAnimation, QRect, QPoint, QSequentialAnimationGroup, QPauseAnimation, QEasingCurve, Qt, QTimer, QSize
from PyQt5.QtGui import QImage, QPixmap, QTransform
from Dark_Mood import get_dark_stylesheet, apply_dark_titlebar, show_styled_msg
from Compare_with_database import compare_with_database

class RegistrationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(get_dark_stylesheet())

        self.captured_image = None 
        self.cap = None  
        self.initUI()
        
        # Camera Setup Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

        self.start_camera() 

    def initUI(self):
        # 1. Main Layout (Vertical)
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # 2. Upper Layout (Horizontal)
        upper_layout = QHBoxLayout()
        upper_layout.setSpacing(40) 

        camera_container = QWidget()
        camera_center_layout = QVBoxLayout(camera_container)
        
        self.camera_label = QLabel("Camera Feed Loading...")
        self.camera_label.setFixedSize(640, 480) 
        self.camera_label.setStyleSheet("border: 3px solid #2c3e50; background-color: black; border-radius: 15px;")
        self.camera_label.setAlignment(Qt.AlignCenter)
        
        camera_center_layout.addWidget(self.camera_label, alignment=Qt.AlignCenter)
        upper_layout.addWidget(camera_container, 1)

        form_container = QFrame()
        form_container.setStyleSheet("""
            QFrame {
                background-color: #1A1A1A;        
                border-radius: 15px;         
                padding: 20px;             
            }
            QLabel { border: none; color: white; font-size: 18px; font-weight: bold; }
        """)
        
        self.form_layout = QFormLayout()
        self.form_layout.setSpacing(20)
        self.form_layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        
        input_style = """
            QLineEdit, QComboBox {
                background-color: #000000; color: white; border: 1px solid #444444;
                border-radius: 8px; padding: 12px; font-size: 16px; min-width: 300px;
            }
            QLineEdit:focus { border: 1px solid #3498db; }
        """
        label_style = "font-size: 18px; color: #BBB;"

        self.name_input = QLineEdit()
        self.id_input = QLineEdit()
        self.level_combo = QComboBox()
        self.level_combo.addItems(["1", "2", "3", "4"])
        self.department_combo = QComboBox()
        self.department_combo.addItems(["General", "CS", "IS", "SC", "CSYS"])
        self.email_input = QLineEdit()

        for widget in [self.name_input, self.id_input, self.level_combo, self.department_combo, self.email_input]:
            widget.setStyleSheet(input_style)

        self.level_combo.currentTextChanged.connect(self.update_department_status)
        self.update_department_status(self.level_combo.currentText())    

        self.form_layout.addRow(QLabel("Full Name:", styleSheet=label_style), self.name_input)
        self.form_layout.addRow(QLabel("Student ID:", styleSheet=label_style), self.id_input)
        self.form_layout.addRow(QLabel("Academic Level:", styleSheet=label_style), self.level_combo)
        self.form_layout.addRow(QLabel("Department:", styleSheet=label_style), self.department_combo)
        self.form_layout.addRow(QLabel("Email Address:", styleSheet=label_style), self.email_input)
        
        form_container.setLayout(self.form_layout)
        upper_layout.addWidget(form_container, 1) 

        main_layout.addLayout(upper_layout)

        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(15)
        buttons_layout.setContentsMargins(0, 20, 0, 0)

        self.capture_btn = QPushButton("Take Photo")
        self.register_btn = QPushButton("Submit Registration")
        self.cancel_btn = QPushButton("Cancel") 
        
        common_btn_style = "padding: 15px; font-size: 16px; font-weight: bold; border-radius: 10px; min-width: 180px;"
        
        # Capture Button (Blue Border)
        self.capture_btn.setStyleSheet(common_btn_style + """
            background-color: #1e1e1e; 
            color: white; 
            border: 2px solid #3498db;
            font-size: 18px;
        """)

        # Register Button (Green Border)
        self.register_btn.setStyleSheet(common_btn_style + """
            background-color: #1e1e1e; 
            color: white; 
            border: 2px solid #2ecc71;
            font-size: 18px;
        """)

        # Cancel Button (Red Border)
        self.cancel_btn.setStyleSheet(common_btn_style + """
            background-color: #1e1e1e; 
            color: white; 
            border: 2px solid #e74c3c;
            font-size: 18px;
        """)

        buttons_layout.addStretch()
        buttons_layout.addWidget(self.capture_btn)
        buttons_layout.addWidget(self.register_btn)
        buttons_layout.addWidget(self.cancel_btn)
        buttons_layout.addStretch()

        main_layout.addLayout(buttons_layout)
        self.setLayout(main_layout)

        self.capture_btn.clicked.connect(self.take_photo)
        self.register_btn.clicked.connect(self.handle_registration)
        self.cancel_btn.clicked.connect(self.close_and_return)

        # Animation Setup
        self.anim_label = QLabel(self)
        self.anim_label.hide() 
        self.anim_label.setStyleSheet("border: 5px solid #3498db; border-radius: 10px;")
        self.anim_label.setScaledContents(True)

    def update_department_status(self, selected_level):
        if selected_level in ["1", "2"]:
            index = self.department_combo.findText("General")
            if index >= 0:
                self.department_combo.setCurrentIndex(index)
    
            self.department_combo.setEnabled(False)
        else:
            self.department_combo.setEnabled(True)
            input_style = """
                QComboBox {
                    background-color: #000000; color: white; border: 1px solid #444444;
                    border-radius: 8px; padding: 12px; font-size: 16px; min-width: 300px;
                }
            """
            self.department_combo.setStyleSheet(input_style)

    def close_and_return(self):
        self.name_input.clear()
        self.id_input.clear()
        self.email_input.clear()
        self.captured_image = None
        self.stop_camera()
        try:
            if hasattr(self.parent().parent(), 'show_dashboard'):
                self.parent().parent().show_dashboard()
        except:
            self.close()

    def start_camera(self):
        if self.cap is not None:
            self.stop_camera()
            
        self.cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW) 
        if not self.cap.isOpened():
            print("Error: Could not open camera.")
            return
            
        self.timer.start(30)

    def showEvent(self, event):
        super().showEvent(event)
        self.start_camera()

    def stop_camera(self):
        self.timer.stop()
        if self.cap:
            self.cap.release()
            self.cap = None

    def update_frame(self):
        if self.cap is None: return
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.flip(frame, 1)
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            qt_image = QImage(rgb_image.data, w, h, ch * w, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qt_image)
            
            scaled_pixmap = pixmap.scaled(
                self.camera_label.size(), 
                Qt.KeepAspectRatioByExpanding, 
                Qt.SmoothTransformation
            )
            self.camera_label.setPixmap(scaled_pixmap)
            self.camera_label.setPixmap(QPixmap.fromImage(qt_image))

    def take_photo(self):
        if self.cap is None: return
        ret, frame = self.cap.read()
        if ret:
            self.captured_image = frame.copy()
            frame_mirrored = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame_mirrored, cv2.COLOR_BGR2RGB)
            h, w, ch = frame_rgb.shape
            bytes_per_line = ch * w
            
            qt_img = QImage(frame_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888).copy()
            pixmap = QPixmap.fromImage(qt_img).scaled(self.camera_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            
            self.anim_label.setPixmap(pixmap)
            global_point = self.camera_label.mapToGlobal(QPoint(0, 0))
            local_pos = self.mapFromGlobal(global_point)
            
            self.start_size = self.camera_label.size()
            self.anim_label.setGeometry(QRect(local_pos, self.start_size))
            self.anim_label.setStyleSheet("border: 3px solid #3498db; background-color: black; border-radius: 10px;")
            self.anim_label.show()
            self.anim_label.raise_()
            self.camera_label.setStyleSheet("border: 3px solid #2ecc71; background-color: black; border-radius: 10px;")
            self.setup_animation(local_pos)

    def setup_animation(self, start_pos):
        pause_anim_1 = QPauseAnimation(100)
        thumb_width, thumb_height = 300, 225
        margin = 30 
        end_x, end_y = margin, self.height() - thumb_height - margin
        
        self.move_anim = QPropertyAnimation(self.anim_label, b"geometry")
        self.move_anim.setDuration(1200) 
        self.move_anim.setStartValue(QRect(start_pos, self.start_size))
        self.move_anim.setEndValue(QRect(QPoint(end_x, end_y), QSize(thumb_width, thumb_height)))
        self.move_anim.setEasingCurve(QEasingCurve.InOutQuad) 

        self.group = QSequentialAnimationGroup()
        self.group.addAnimation(pause_anim_1)
        self.group.addAnimation(self.move_anim)
        self.group.addAnimation(QPauseAnimation(1000))
        self.group.finished.connect(self.hide_freeze_frame)
        self.group.start()

    def hide_freeze_frame(self):
        self.anim_label.hide()
        self.camera_label.setStyleSheet("border: 3px solid #2c3e50; background-color: black; border-radius: 10px; ")

    def handle_registration(self):
        name = self.name_input.text().strip()
        student_id = self.id_input.text().strip()
        email = self.email_input.text().strip()
        level = self.level_combo.currentText()
        department = self.department_combo.currentText()

        if not name or not student_id or not email:
            show_styled_msg(self, "Input Error", "Please fill in all fields!", QMessageBox.Warning)
            return
        
        if not email.lower().endswith("@gmail.com") :
            show_styled_msg(self, "Email Error", "Email must end with @gmail.com", QMessageBox.Warning)
            return

        email_prefix = email.split('@')[0]
        if not email_prefix:
            show_styled_msg(self, "Email Error", "Email prefix cannot be empty!", QMessageBox.Warning)
            return
        
        if self.captured_image is None:
            show_styled_msg(self,"Photo Error", "Please capture a photo before registering!", QMessageBox.Warning)
            return

        try:
            conn = sqlite3.connect("University.db")
            cursor = conn.cursor()
            cursor.execute("SELECT ID FROM Students WHERE Email = ?", (email,))
            existing_email = cursor.fetchone()
            conn.close()

            if existing_email:
                show_styled_msg(self, "Duplicate Email", 
                                f"This email is already registered with student ID: {existing_email[0]}", 
                                QMessageBox.Critical)
                return
            
            embedding = get_embedding(self.captured_image) 
            vec = embedding
            if embedding is None:
                show_styled_msg(self,"Face Error", "No face detected. Try again!", QMessageBox.Warning)
                return
            
            existing_student_id = compare_with_database(embedding, threshold=0.4)

            if existing_student_id:
                show_styled_msg(self, "Duplicate Registration", 
                                f"This person is already registered in the system!\n"
                                f"Registered under ID: {existing_student_id}", 
                                QMessageBox.Critical)
                return
            
            insert_student(name, student_id, level,department, email ,pickle.dumps(embedding))
            show_styled_msg(self,"Success", f"Student '{student_id}' registered.", QMessageBox.Information)
            
            self.name_input.clear()
            self.id_input.clear()
            self.email_input.clear()
            self.captured_image = None

            self.close_and_return()
            
        except Exception as e:
            show_styled_msg(self, "Error", f"An error occurred: {str(e)}", QMessageBox.Warning)

    def closeEvent(self, event):
        self.stop_camera()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationApp()
    window.showMaximized()
    sys.exit(app.exec_())
