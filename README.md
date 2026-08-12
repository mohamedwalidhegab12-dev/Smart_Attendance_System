<div align="center">🎓 SmartGate

Advanced AI-Powered Attendance System

Automating academic attendance through real-time facial recognition, intelligent lecture scheduling, and a desktop management dashboard.

<br><p>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/DeepFace-AI-FF6F00?style=for-the-badge">
  <img src="https://img.shields.io/badge/ArcFace-Face%20Recognition-6C5CE7?style=for-the-badge">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white">
</p><p>
  <img src="https://img.shields.io/badge/PyQt5-Desktop%20GUI-41CD52?style=for-the-badge&logo=qt&logoColor=white">
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
  <img src="https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white">
</p><br><a href="https://github.com/mohamedwalidhegab12-dev/Smart_Attendance_System">
  <img src="https://img.shields.io/badge/🚀%20View%20Repository-GitHub-181717?style=for-the-badge&logo=github">
</a></div>---

🧠 What is SmartGate?

SmartGate is a real-time AI attendance management system built to automate student attendance in academic environments.

The system combines Computer Vision, Face Recognition, Deep Learning, Database Management, and Desktop GUI development into one integrated application.

Instead of manually checking attendance, SmartGate can:

«Detect → Represent → Recognize → Verify → Record»

all while connecting the recognition process to the currently active lecture.

---

<div align="center">📸 Application Preview

<br><img src="./images/demo1.png" width="850"><br><br>

<img src="./images/demo2.png" width="850"></div>---

✨ Core Capabilities

<table>
<tr>
<td width="50%">🎥 Real-Time Recognition

- Live camera processing
- OpenCV image acquisition
- Face detection
- ArcFace embeddings
- Real-time identity matching

</td><td width="50%">📝 Smart Registration

- Student registration
- Live camera capture
- Student information validation
- Face embedding generation
- Duplicate face detection

</td>
</tr><tr>
<td width="50%">📚 Lecture Awareness

- Reads the academic schedule
- Detects the active lecture
- Automatically starts attendance monitoring
- Displays today's complete schedule

</td><td width="50%">📊 Attendance Management

- Automatic attendance marking
- Student ID tracking
- Lecture tracking
- Check-in time
- Duplicate attendance handling

</td>
</tr><tr>
<td width="50%">🖥️ Desktop Dashboard

- PyQt5 interface
- Live camera feed
- Attendance table
- Schedule table
- System status
- Manual synchronization

</td><td width="50%">🗄️ Local Data Layer

- SQLite database
- Student records
- Facial embeddings
- Lecture schedules
- Attendance records

</td>
</tr>
</table>---

🏗️ System Architecture

<div align="center">flowchart TD

    A["📷 Camera Input"]
    B["👁️ Face Detection<br/>OpenCV"]
    C["🧠 ArcFace Embedding<br/>DeepFace"]
    D["🔎 Face Comparison<br/>Cosine Distance"]
    E["👤 Student Identification"]
    F["📚 Active Lecture<br/>Schedule Check"]
    G["✅ Attendance Validation"]
    H[("🗄️ SQLite Database")]
    I["🖥️ PyQt5 Dashboard"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> I


</div>---

🔄 How Attendance Works

01 — Camera Capture

The system receives frames from the connected camera using OpenCV.

02 — Face Detection

The current frame is processed and the face is prepared for recognition.

03 — Feature Extraction

DeepFace generates an ArcFace facial embedding from the detected face.

04 — Identity Matching

The generated embedding is compared against registered student embeddings using cosine distance.

The current implementation accepts a match when the distance is below the configured threshold of 0.4.

05 — Lecture Verification

The application checks the database schedule and identifies the lecture currently taking place.

06 — Attendance Recording

After successful identification, the student's attendance is recorded in the SQLite database.

07 — Dashboard Update

The PyQt5 dashboard immediately updates the attendance table and provides visual feedback.

---

🧩 Technology Stack

Technology| Role
🐍 Python| Core application logic
🧠 DeepFace| Facial representation pipeline
🎯 ArcFace| Facial embedding model
👁️ OpenCV| Camera input & computer vision
🔢 NumPy| Vector and numerical operations
🖥️ PyQt5| Desktop graphical interface
🗄️ SQLite| Persistent application database
📦 Pickle| Facial embedding serialization
⚡ TensorFlow| Deep learning backend

---

🗂️ Project Architecture

Smart_Attendance_System/
│
├── 📊 AttendanceDashboard.py
│   └── Main PyQt5 dashboard
│
├── 👤 Register.py
│   └── Student registration interface
│
├── 🎥 cameraThread.py
│   └── Real-time camera processing
│
├── 🧠 Embedding_pic.py
│   └── ArcFace embedding extraction
│
├── 🔎 Compare_with_database.py
│   └── Facial embedding comparison
│
├── ✅ Mark_attendance.py
│   └── Attendance recording
│
├── 📚 Fetch_lecture.py
│   └── Active lecture & schedule logic
│
├── 📊 Dashboard_data.py
│   └── Dashboard attendance data
│
├── 🧱 Data_Model.py
│   └── Data structures
│
├── 🗄️ DB_Setup.py
│   └── Database initialization
│
├── 👨‍🎓 DB_Students.py
│   └── Student database operations
│
├── 📝 DB_Attendees.py
│   └── Attendance database operations
│
├── 📅 DB_Schedule.py
│   └── Schedule database operations
│
├── 🎨 Dark_Mood.py
│   └── Application styling
│
├── 🖼️ images/
│   ├── demo1.png
│   ├── demo2.png
│   └── student images
│
├── 🗃️ University.db
│   └── SQLite database
│
├── SQL_command.sql
│   └── SQL commands
│
└── README.md

---

🗄️ Data Layer

SmartGate uses SQLite through a local database named:

University.db

The database is responsible for managing the main application data.

👨‍🎓 Students

Stores student information and facial embeddings.

Student
├── ID
├── Name
├── Level
├── Department
├── Email
└── Face Embedding

📚 Schedule

Provides lecture information used to determine the currently active lecture.

Lecture
├── ID
├── Name
├── Day
├── Start Time
└── End Time

📝 Attendance

Stores attendance events generated by the recognition pipeline.

Attendance
├── Student ID
├── Lecture
├── Student Name
├── Level
├── Department
├── Date
└── Check-in Time

---

👤 Student Registration

SmartGate provides a dedicated registration interface.

<div align="center">┌──────────────────────────────────────────────┐
│              STUDENT REGISTRATION            │
├──────────────────────────────────────────────┤
│                                              │
│  📷 Live Camera       👤 Student Information │
│                                              │
│                       Full Name              │
│                       Student ID             │
│                       Academic Level         │
│                       Department             │
│                       Email Address          │
│                                              │
├──────────────────────────────────────────────┤
│     Take Photo  •  Register  •  Cancel       │
└──────────────────────────────────────────────┘

</div>The registration process includes:

- Student information entry
- Camera capture
- Face embedding extraction
- Duplicate email validation
- Duplicate face validation
- Database insertion

---

🔎 Face Recognition Pipeline

                CAMERA FRAME
                     │
                     ▼
             ┌───────────────┐
             │ Face Detection│
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │   DeepFace    │
             │   + ArcFace   │
             └───────┬───────┘
                     │
                     ▼
              FACE EMBEDDING
                     │
                     ▼
             ┌───────────────┐
             │ SQLite Stored │
             │  Embeddings   │
             └───────┬───────┘
                     │
                     ▼
             COSINE DISTANCE
                     │
                     ▼
             ┌───────────────┐
             │ Best Valid    │
             │    Match      │
             └───────┬───────┘
                     │
                     ▼
               STUDENT ID

---

⏱️ Intelligent Lecture Detection

SmartGate continuously monitors the current system time and compares it with the stored academic schedule.

Current Time
     │
     ▼
Read Today's Schedule
     │
     ▼
Find Active Lecture
     │
 ┌───┴──────────────┐
 │                  │
 ▼                  ▼
Lecture Found    No Lecture
 │                  │
 ▼                  ▼
Start Camera      Camera Off
 │
 ▼
Enable Attendance

This allows the system to automatically transition between:

No Active Lecture → Active Lecture → Attendance Monitoring

without requiring the user to manually select a lecture.

---

🛡️ Attendance Validation

SmartGate does not simply recognize a face and insert a row.

The system also handles attendance state:

✅ New Attendance

A recognized student who has not yet been marked for the active lecture is recorded.

🔁 Duplicate Attendance

If the student has already been marked, the system prevents another attendance record and displays a notification.

❌ Unknown Face

If no valid student match is found under the configured recognition threshold, no attendance record is created.

---

🖥️ Dashboard

The main dashboard provides a real-time view of the system.

Left Panel

- Live camera feed
- Current system status
- Attendance notifications
- Student registration access

Right Panel

- Current lecture attendance
- Student ID
- Student name
- Lecture
- Check-in time
- Today's schedule
- Manual synchronization

---

🚀 Getting Started

Prerequisites

Make sure you have:

- Python 3.10+
- A working webcam
- Windows/Linux/macOS environment
- Git

---

1️⃣ Clone

git clone https://github.com/mohamedwalidhegab12-dev/Smart_Attendance_System.git
cd Smart_Attendance_System

2️⃣ Create Virtual Environment

python -m venv venv

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate

3️⃣ Install Dependencies

pip install opencv-python
pip install deepface
pip install numpy
pip install PyQt5
pip install tensorflow

4️⃣ Initialize the Database

python DB_Setup.py

5️⃣ Run SmartGate

python AttendanceDashboard.py

---

🎬 Typical Usage

Launch SmartGate
      │
      ▼
Check Lecture Schedule
      │
      ▼
Active Lecture?
   │          │
  YES         NO
   │          │
   ▼          ▼
Camera ON   Wait
   │
   ▼
Recognize Student
   │
   ▼
Validate Attendance
   │
   ▼
Save to Database
   │
   ▼
Update Dashboard

---

🎯 Project Goals

SmartGate was designed around four major goals:

Goal| Approach
⏱️ Reduce manual effort| Automate attendance
👤 Identify students| Face recognition
📚 Connect attendance to lectures| Schedule-aware logic
📊 Centralize records| SQLite database + dashboard

---

🧪 Engineering Highlights

This project demonstrates practical integration of multiple software and AI concepts:

- Computer Vision
- Face Recognition
- Deep Learning inference
- Facial embeddings
- Vector similarity
- Real-time camera processing
- Multithreaded GUI processing
- Database design
- SQL operations
- Desktop application development
- Event-driven programming
- Input validation
- Application state management

---

🔮 Roadmap

Future iterations could extend SmartGate with:

- [ ] Advanced liveness / anti-spoofing
- [ ] Attendance analytics
- [ ] CSV / Excel reporting
- [ ] Admin authentication
- [ ] Cloud database support
- [ ] Web-based dashboard
- [ ] Multi-camera support
- [ ] Centralized university deployment
- [ ] Advanced recognition under challenging lighting conditions

---

👨‍💻 Team

<div align="center">SmartGate Development Team

Member| Role
Mohamed Walid| AI / Software Development
Malak Eldesouky| Team Member
Saif Gamal| Team Member
John Hady| Team Member
Fatma Gahlan| Team Member

<br>Supervisor

Mohamed Eleraqy

</div>---

🎓 Academic Context

SmartGate was developed as an academic project focused on applying Artificial Intelligence and Software Engineering to a real-world university problem.

The project brings together:

«AI + Computer Vision + Databases + Desktop Development»

into a single practical system.

---

<div align="center">⭐ SmartGate

Recognize. Verify. Record.

An intelligent approach to academic attendance.

<br><a href="https://github.com/mohamedwalidhegab12-dev/Smart_Attendance_System">
  <img src="https://img.shields.io/badge/⭐%20Star%20the%20Repository-181717?style=for-the-badge&logo=github">
</a><br><br>

Built with Python • DeepFace • ArcFace • OpenCV • PyQt5 • SQLite

</div>
