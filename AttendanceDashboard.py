import sys
import os
from datetime import datetime
import cv2
import numpy as np

# --- TensorFlow Optimization ---
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
try:
    import tensorflow as tf
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
except Exception:
    pass

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
                             QHeaderView, QPushButton, QStackedWidget)
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, Qt

# --- Custom Imports ---
from Dark_Mood import get_dark_stylesheet, apply_dark_titlebar
from Fetch_lecture import fetch_lecture_from_db, get_today_schedule
from Dashboard_data import get_dashboard_data
from Register import RegistrationApp
from cameraThread import CameraThread

class AttendanceDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Attendance System")
        self.setStyleSheet(get_dark_stylesheet())

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.last_checked_hour = -1
        self.current_lecture = None

        self.init_ui()
        self.sync_system_state()

        self.monitor_timer = QTimer()
        self.monitor_timer.timeout.connect(self.time_monitoring_logic)
        self.monitor_timer.start(1000)

    def init_ui(self):
        self.setCentralWidget(self.stacked_widget)
        self.dashboard_page = QWidget()
        layout = QHBoxLayout(self.dashboard_page) 
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # --- Left Section: Camera Feed ---
        left_layout = QVBoxLayout()
        
        self.camera_label = QLabel("Initializing Camera...")
        self.camera_label.setFixedSize(930, 475) 
        self.camera_label.setStyleSheet("border: 2px solid #333; background-color: #000; border-radius: 10px;")
        self.camera_label.setAlignment(Qt.AlignCenter)
        
        self.status_label = QLabel("Status: Standby")
        self.status_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #CCC;")
        
        self.msg_label = QLabel("") 
        self.reg_btn = QPushButton("Register New Student")
        self.reg_btn.clicked.connect(self.open_registration_page)
        self.reg_btn.setMinimumHeight(60) # 
        self.reg_btn.setStyleSheet("""
        QPushButton {
        background-color: #1e1e1e; 
        color: white; 
        font-size: 20px; 
        font-weight: bold; 
        border: 2px solid #3498db; 
        border-radius: 10px;
        padding: 10px;
            }

        QPushButton:hover {
        background-color: #2d2d2d;
        border: 2px solid #3498db; 
            }

        QPushButton:pressed {
        background-color: #121212;
            }
            """)

        left_layout.addWidget(self.camera_label)
        left_layout.addWidget(self.status_label)
        left_layout.addWidget(self.msg_label)
        left_layout.addStretch()
        left_layout.addWidget(self.reg_btn)
        # --- Right Section: Tables ---

        right_layout = QVBoxLayout()
        table_style = """
            QTableWidget {
                background-color: #121212;
                color: #FFFFFF;
                border: 1px solid #333;
                gridline-color: #333;
                outline: none;
                border-radius: 5px;
            }
            QTableWidget::item {
                background-color: transparent;
                padding: 5px;
                border-bottom: 1px solid #222;
            }
            QTableWidget::item:hover, QTableWidget::item:selected {
                background-color: transparent;
                color: #FFFFFF;
            }
            QHeaderView::section {
                background-color: #1e1e1e;
                color: #EEE;
                padding: 5px;
                border: 1px solid #333;
                font-weight: bold;
                font-size: 16px
            }
        """
        # 1. Current Attendance List
        attendance_box = QVBoxLayout()
        attn_title = QLabel("LECTURE ATTENDANCE")
        attn_title.setStyleSheet("font-size: 18px; color: #4CAF50; font-weight: bold;")

        self.attendance_table = QTableWidget()
        self.attendance_table.setColumnCount(4)
        self.attendance_table.setHorizontalHeaderLabels(["ID", "Name", "Lecture", "Time"])
        self.attendance_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.attendance_table.setStyleSheet(table_style)
        self.attendance_table.verticalHeader().setVisible(False)
        self.attendance_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.attendance_table.setSelectionMode(QTableWidget.NoSelection)
        self.attendance_table.setFocusPolicy(Qt.NoFocus)

        attendance_box.addWidget(attn_title)
        attendance_box.addWidget(self.attendance_table)

        # 2. Daily Schedule List
        schedule_box = QVBoxLayout()
        sched_title = QLabel("TODAY'S FULL SCHEDULE")
        sched_title.setStyleSheet("font-size: 18px;color: #FFA500; font-weight: bold;")

        self.schedule_table = QTableWidget()
        self.schedule_table.setColumnCount(3)
        self.schedule_table.setHorizontalHeaderLabels(["Lecture", "Start", "End"])
        self.schedule_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.schedule_table.setStyleSheet(table_style)

        self.schedule_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.schedule_table.setSelectionMode(QTableWidget.NoSelection)
        self.schedule_table.setFocusPolicy(Qt.NoFocus)
        self.schedule_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.schedule_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.schedule_table.verticalHeader().setVisible(False)

        row_height = 40
        self.schedule_table.verticalHeader().setDefaultSectionSize(row_height)
        self.schedule_table.setMinimumHeight(row_height * 7)

        schedule_box.addWidget(sched_title)
        schedule_box.addWidget(self.schedule_table)

        right_layout.addLayout(attendance_box, stretch=2)
        right_layout.addLayout(schedule_box, stretch=1)

        self.refresh_btn = QPushButton("Manual Sync")
        self.refresh_btn.clicked.connect(self.sync_system_state)
        right_layout.addWidget(self.refresh_btn)
        self.refresh_btn.setMinimumHeight(60)
        self.refresh_btn.setStyleSheet("""
        QPushButton {
        background-color: #1e1e1e; 
        color: white; 
        font-size: 20px; 
        font-weight: bold; 
        border: 2px solid #3498db; 
        border-radius: 10px;
        padding: 10px;
            }

        QPushButton:hover {
        background-color: #2d2d2d;
        border: 2px solid #3498db; 
            }

        QPushButton:pressed {
        background-color: #121212;
            }
            """)

        layout.addLayout(left_layout, stretch=1)
        layout.addLayout(right_layout, stretch=1)
 
        self.registration_page = RegistrationApp()

        self.stacked_widget.addWidget(self.dashboard_page)    
        self.stacked_widget.addWidget(self.registration_page) 

    def open_registration_page(self):
        self.stop_camera_thread()
        self.stacked_widget.setCurrentWidget(self.registration_page)
        if hasattr(self.registration_page, 'start_camera'):
            self.registration_page.start_camera()

    def show_dashboard(self):
        self.stacked_widget.setCurrentIndex(0)
        self.start_camera_thread()

    def time_monitoring_logic(self):
        now = datetime.now()
        if now.minute == 0 and now.second == 0 and now.hour != self.last_checked_hour or self.last_checked_hour == -1:
            self.sync_system_state()

    def sync_system_state(self):
        self.current_lecture = fetch_lecture_from_db()
        self.last_checked_hour = datetime.now().hour
        self.update_daily_schedule_view()
        self.refresh_attendance_table() 

        if self.current_lecture:
            self.lecture_id, self.lecture_name = self.current_lecture
            self.status_label.setText(f"Active Now: {self.lecture_name}")
            self.status_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #4CAF50;")
            self.start_camera_thread()
        else:
            self.lecture_id = None
            self.status_label.setText("Status: No Active Lecture Found")
            self.status_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #E74C3C;")
            self.stop_camera_thread()

    def update_daily_schedule_view(self):
        try:
            full_schedule = get_today_schedule()
            self.schedule_table.setRowCount(0)
            for i, lec in enumerate(full_schedule):
                self.schedule_table.insertRow(i)
                self.schedule_table.setItem(i, 0, QTableWidgetItem(str(lec['name'])))
                self.schedule_table.setItem(i, 1, QTableWidgetItem(str(lec['start'])))
                self.schedule_table.setItem(i, 2, QTableWidgetItem(str(lec['end'])))
        except Exception as e:
            print(f"Error loading schedule: {e}")

    def start_camera_thread(self):
        if hasattr(self, 'camera_thread') and self.camera_thread.isRunning():
            self.camera_thread.stop()
            self.camera_thread.wait()
        self.camera_thread = CameraThread(self.lecture_id)
        self.camera_thread.frame_ready.connect(self.display_camera_frame)
        self.camera_thread.attendance_marked.connect(self.on_attendance_success)
        self.camera_thread.already_marked.connect(self.on_attendance_duplicate)
        self.camera_thread.start()

    def stop_camera_thread(self):
        if hasattr(self, 'camera_thread') and self.camera_thread.isRunning():
            self.camera_thread.stop()
            self.camera_thread.wait()
        self.camera_label.setText("Camera Offline")

    def display_camera_frame(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_frame.shape
        q_img = QImage(rgb_frame.data, w, h, ch * w, QImage.Format_RGB888)
        self.camera_label.setPixmap(QPixmap.fromImage(q_img).scaled(
        self.camera_label.size(), 
        Qt.KeepAspectRatioByExpanding,
        Qt.SmoothTransformation))
        
    def on_attendance_success(self, data):
        self.msg_label.setText(f"SUCCESS: {data['name']} marked.")
        self.msg_label.setStyleSheet("font-size: 18px; color: #4CAF50; font-weight: bold;")
        self.refresh_attendance_table()
        QTimer.singleShot(5000, lambda: self.msg_label.setText(""))

    def on_attendance_duplicate(self, message):
        self.msg_label.setText(message)
        self.msg_label.setStyleSheet("font-size: 18px; color: #2196F3; font-weight: bold;")
        QTimer.singleShot(5000, lambda: self.msg_label.setText(""))

    def refresh_attendance_table(self):
        if hasattr(self, 'lecture_id') and self.lecture_id:
            attendance_list = get_dashboard_data()
            self.attendance_table.setRowCount(0)
            for i, entry in enumerate(attendance_list):
                self.attendance_table.insertRow(i)
                self.attendance_table.setItem(i, 0, QTableWidgetItem(str(entry['student_id'])))
                self.attendance_table.setItem(i, 1, QTableWidgetItem(entry['name']))
                self.attendance_table.setItem(i, 2, QTableWidgetItem(str(entry['lecture_name'])))
                self.attendance_table.setItem(i, 3, QTableWidgetItem(entry['time']))

    def closeEvent(self, event):
        self.stop_camera_thread()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AttendanceDashboard()
    apply_dark_titlebar(window)
    window.showMaximized()
    sys.exit(app.exec_())
