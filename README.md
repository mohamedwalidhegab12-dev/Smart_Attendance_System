🎓 SmartGate — Advanced AI Attendance System

«A real-time AI-powered attendance management system that uses facial recognition to automate student attendance in academic environments.»

"Python" (https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
"PyQt5" (https://img.shields.io/badge/GUI-PyQt5-green)
"DeepFace" (https://img.shields.io/badge/AI-DeepFace-orange)
"ArcFace" (https://img.shields.io/badge/Face%20Recognition-ArcFace-purple)
"OpenCV" (https://img.shields.io/badge/Computer%20Vision-OpenCV-red)
"SQLite" (https://img.shields.io/badge/Database-SQLite-lightgrey)
"Status" (https://img.shields.io/badge/Status-Completed-brightgreen)

---

📌 Overview

SmartGate is an AI-powered attendance system designed to automate the process of recording student attendance using real-time face recognition.

Instead of relying on manual attendance or traditional ID-based check-ins, the system captures a student's face through a camera, extracts a facial embedding using ArcFace, compares it against registered students, identifies the student, and records the attendance in a local SQLite database.

The system also integrates the academic schedule to determine the currently active lecture and provides a real-time desktop dashboard for monitoring attendance.

---

🎯 Project Objectives

- Automate student attendance using facial recognition.
- Reduce manual attendance-taking effort.
- Identify registered students from live camera input.
- Prevent duplicate attendance for the same lecture and day.
- Connect attendance records with the academic schedule.
- Provide a simple real-time interface for monitoring attendance.
- Store student and attendance information in a structured database.

---

✨ Key Features

👤 Student Registration

Students can be registered through a dedicated PyQt5 interface.

The registration process collects:

- Full Name
- Student ID
- Academic Level
- Department
- Email Address
- Face Image

Before registration, the system validates the provided information and checks whether the email or face already exists in the database.

A facial embedding is generated from the captured image and stored with the student's information.

---

🧠 AI Face Recognition

SmartGate uses DeepFace with the ArcFace model to generate facial embeddings from camera frames.

The system:

1. Captures a frame from the camera.
2. Converts the image into the required format.
3. Detects and aligns the face.
4. Generates an ArcFace facial embedding.
5. Compares the embedding with registered students.
6. Selects the closest valid match based on cosine distance.

The current implementation uses a configurable matching threshold of "0.4".

---

📸 Real-Time Camera Processing

The application uses OpenCV for camera input and real-time frame processing.

Camera processing is integrated with the PyQt5 interface through a dedicated camera thread, allowing the dashboard to display the live camera feed while handling attendance events.

---

📚 Automatic Lecture Detection

SmartGate automatically checks the current day and time against the stored academic schedule.

If the current time falls within a scheduled lecture, that lecture becomes the active lecture for attendance.

The dashboard then displays the active course and starts the attendance monitoring process.

---

✅ Automatic Attendance Marking

After successfully recognizing a registered student, the system records:

- Student ID
- Student Name
- Lecture ID
- Lecture Name
- Academic Level
- Department
- Check-in Time
- Attendance Date

The system also handles duplicate attendance attempts and prevents the same student from being checked in again for the same lecture/day.

---

📊 Real-Time Dashboard

The PyQt5 dashboard provides:

- Live camera feed
- Current system status
- Active lecture information
- Current lecture attendance table
- Today's complete lecture schedule
- Successful attendance notifications
- Duplicate attendance notifications
- Student registration interface
- Manual synchronization

The dashboard automatically refreshes its attendance and schedule information as the system state changes.

---

🏗️ System Architecture

                    ┌───────────────────┐
                    │   Camera Input    │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   OpenCV Frames   │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Face Detection &  │
                    │     Alignment     │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ ArcFace Embedding │
                    │   via DeepFace    │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Face Comparison   │
                    │ Cosine Distance   │
                    └─────────┬─────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │ Student Identification  │
                 └────────────┬────────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Active Lecture    │
                    │  & Schedule Check │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ SQLite Database   │
                    │  Attendance Logs  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │  PyQt5 Dashboard  │
                    └───────────────────┘

---

🧩 Technologies & Tools

Technology| Purpose
Python| Core application development
DeepFace| Facial representation and recognition pipeline
ArcFace| Face embedding generation
OpenCV| Camera access and image processing
NumPy| Numerical operations and vector processing
PyQt5| Desktop GUI
SQLite| Student, schedule, and attendance storage
Pickle| Serialization of facial embeddings
TensorFlow| Backend used by the DeepFace/ArcFace pipeline

---

🗄️ Database Structure

The application uses a local SQLite database named:

University.db

The system contains dedicated database components for:

Students

Stores student information and facial embeddings.

Students
├── Name
├── ID
├── Level
├── Department
├── Email
└── Embedding

Schedule

Stores lecture scheduling information used to determine the active lecture.

Schedule
├── ID
├── Course
├── Day
├── Start Time
└── End Time

Attendees

Stores attendance records generated by the recognition system.

Attendees
├── Student ID
├── Lecture ID
├── Lecture Name
├── Name
├── Level
├── Department
├── Check-in Time
└── Attendance Date

Database initialization is handled through dedicated database modules and "DB_Setup.py".

---

🔄 Attendance Workflow

Start Application
       │
       ▼
Check Current Schedule
       │
       ▼
Is There an Active Lecture?
       │
   ┌───┴───┐
   │       │
  No      Yes
   │       │
   ▼       ▼
Wait    Start Camera
           │
           ▼
      Capture Frame
           │
           ▼
      Detect Face
           │
           ▼
    Generate ArcFace
       Embedding
           │
           ▼
 Compare With Students
       Database
           │
      ┌────┴────┐
      │         │
   Match      No Match
      │         │
      ▼         ▼
Check Duplicate   Ignore
      │
  ┌───┴────┐
  │        │
New       Already
Entry     Marked
  │        │
  ▼        ▼
Record    Notify
Attendance User

---

📁 Project Structure

Smart_Attendance_System/
│
├── AttendanceDashboard.py
├── Register.py
├── Mark_attendance.py
├── Compare_with_database.py
├── Embedding_pic.py
├── cameraThread.py
│
├── Fetch_lecture.py
├── Dashboard_data.py
├── Data_Model.py
│
├── DB_Setup.py
├── DB_Students.py
├── DB_Attendees.py
├── DB_Schedule.py
├── SQL_command.sql
│
├── Dark_Mood.py
├── University.db
│
├── images/
├── .gitignore
└── README.md

---

🚀 Installation

1. Clone the Repository

git clone https://github.com/mohamedwalidhegab12-dev/Smart_Attendance_System.git

2. Navigate to the Project

cd Smart_Attendance_System

3. Create a Virtual Environment

python -m venv venv

4. Activate the Environment

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate

5. Install Dependencies

Install the required Python packages:

pip install opencv-python
pip install deepface
pip install numpy
pip install PyQt5
pip install tensorflow

---

▶️ Running the Application

Initialize the database:

python DB_Setup.py

Then start the main dashboard:

python AttendanceDashboard.py

The application opens the main SmartGate dashboard where the system can monitor the current lecture, access the camera, recognize registered students, and record attendance.

---

📝 Student Registration Flow

To register a new student:

1. Open the SmartGate dashboard.
2. Select Register New Student.
3. Enter the student's information.
4. Capture the student's face.
5. The system extracts an ArcFace embedding.
6. The system checks for duplicate email and face registration.
7. If validation succeeds, the student is stored in the database.

The registration module performs both database-level and face-level duplicate checks before inserting a new student.

---

🔍 Face Matching

Registered facial embeddings are stored in the SQLite database.

For recognition, the current face embedding is compared against stored embeddings using cosine similarity/distance.

The system keeps the closest valid match under the configured threshold.

Current Face
     │
     ▼
ArcFace Embedding
     │
     ▼
Compare Against
Stored Embeddings
     │
     ▼
Cosine Distance
     │
     ▼
Threshold Check
     │
     ▼
Best Matching Student

---

🖥️ User Interface

The application uses PyQt5 to provide a desktop-based interface.

The main dashboard includes:

- Live camera display
- Attendance table
- Daily schedule
- Active lecture status
- Student registration
- Synchronization controls
- Attendance feedback

The registration interface also includes camera capture and form validation.

---

🔐 Data & Validation

SmartGate includes several validation mechanisms:

- Required student information validation
- Gmail address validation
- Duplicate email detection
- Duplicate student face detection
- Student ID database constraints
- Lecture existence validation
- Duplicate attendance handling

These checks help maintain consistent student and attendance records.

---

📈 Future Improvements

Potential future enhancements include:

- Advanced liveness / anti-spoofing mechanisms.
- More robust recognition under difficult lighting conditions.
- Cloud-based database integration.
- Web-based administration dashboard.
- Attendance reports and analytics.
- Export attendance records to CSV/Excel.
- Role-based authentication for administrators.
- Support for multiple cameras.
- Centralized university deployment.

---

👨‍💻 Contributors

Mohamed Walid

AI & Data Science / Computer Science Student

Malak Eldesouky

Saif Gamal

John Hady

Fatma Gahlan

Supervisor: Mohamed Eleraqy

---

🎓 Academic Project

This project was developed as an academic software and AI project focused on applying:

- Computer Vision
- Facial Recognition
- Deep Learning
- Database Management
- Desktop Application Development

to solve a real-world problem in educational environments.

---

⭐ Why SmartGate?

Traditional attendance can be time-consuming, repetitive, and difficult to manage at scale.

SmartGate combines AI-based face recognition, automated lecture detection, database management, and a real-time desktop interface into one integrated attendance solution.

«Recognize. Verify. Record. Automatically.»

---

📄 License

This project is intended for educational and academic purposes.

---

🔗 Repository

GitHub:
https://github.com/mohamedwalidhegab12-dev/Smart_Attendance_System
