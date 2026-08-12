<div align="center"><img src="./images/demo1.png" width="920" alt="SmartGate Dashboard"><br><br>

SmartGate

AI-Powered Smart Attendance System

A real-time computer vision system that automates university attendance using facial recognition and intelligent lecture scheduling.

<br><a href="https://github.com/mohamedwalidhegab12-dev/Smart_Attendance_System">
<img src="https://img.shields.io/badge/Repository-GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
</a>
&nbsp;
<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
&nbsp;
<img src="https://img.shields.io/badge/DeepFace-ArcFace-6C5CE7?style=for-the-badge" alt="DeepFace">
&nbsp;
<img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV"><br><br>

<img src="https://img.shields.io/badge/PyQt5-Desktop%20Application-41CD52?style=flat-square&logo=qt&logoColor=white" alt="PyQt5">
<img src="https://img.shields.io/badge/SQLite-Database-003B57?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite">
<img src="https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=flat-square&logo=numpy&logoColor=white" alt="NumPy">
<img src="https://img.shields.io/badge/TensorFlow-Deep%20Learning-FF6F00?style=flat-square&logo=tensorflow&logoColor=white" alt="TensorFlow"><br><br>

<em>Recognize. Verify. Record.</em>

</div>---

Contents

- "Overview" (#overview)
- "The Problem" (#the-problem)
- "The Solution" (#the-solution)
- "Key Features" (#key-features)
- "How It Works" (#how-it-works)
- "System Architecture" (#system-architecture)
- "Face Recognition Pipeline" (#face-recognition-pipeline)
- "Attendance Workflow" (#attendance-workflow)
- "Application Interface" (#application-interface)
- "Technology Stack" (#technology-stack)
- "Database Architecture" (#database-architecture)
- "Project Structure" (#project-structure)
- "Getting Started" (#getting-started)
- "Usage" (#usage)
- "Engineering Highlights" (#engineering-highlights)
- "Challenges & Design Decisions" (#challenges--design-decisions)
- "Future Roadmap" (#future-roadmap)
- "Team" (#team)

---

Overview

SmartGate is a desktop-based AI attendance management system built to automate the process of recording student attendance in university environments.

The application combines:

- Computer Vision
- Facial Recognition
- Deep Learning
- Real-Time Camera Processing
- Academic Schedule Management
- SQLite Database Management
- PyQt5 Desktop Development

into a single integrated system.

Instead of relying on manual attendance, SmartGate uses a camera to recognize registered students and automatically associate their presence with the currently active lecture.

---

The Problem

Traditional attendance systems can create several practical challenges:

Challenge| Impact
Manual attendance| Consumes valuable lecture time
Repetitive checking| Creates unnecessary administrative work
Duplicate records| Can affect attendance accuracy
Separate lecture tracking| Makes record management harder
Manual data entry| Increases the possibility of human error

A better solution requires the attendance process to be:

Automatic → Context-aware → Fast → Structured

---

The Solution

SmartGate creates an automated pipeline that connects:

<div align="center">Camera

↓

Face Recognition

↓

Student Identification

↓

Active Lecture Detection

↓

Attendance Validation

↓

Database Storage

↓

Real-Time Dashboard

</div>This allows attendance to become part of one continuous workflow instead of a collection of manual steps.

---

Key Features

<table>
<tr><td width="50%" valign="top">Face Recognition

Real-time facial identification using:

- DeepFace
- ArcFace
- Facial embeddings
- Cosine distance comparison
- Configurable recognition threshold

</td><td width="50%" valign="top">Smart Attendance

The system can:

- Identify registered students
- Detect the active lecture
- Record attendance automatically
- Prevent duplicate attendance records

</td></tr><tr><td width="50%" valign="top">Student Registration

Dedicated registration workflow including:

- Student information
- Camera capture
- Face embedding generation
- Duplicate email validation
- Duplicate face validation

</td><td width="50%" valign="top">Lecture Scheduling

Schedule-aware attendance through:

- Current day detection
- Current time detection
- Active lecture identification
- Automatic lecture association

</td></tr><tr><td width="50%" valign="top">Real-Time Dashboard

The PyQt5 interface provides:

- Live camera feed
- Attendance information
- Active lecture
- Daily schedule
- System status
- Manual synchronization

</td><td width="50%" valign="top">Persistent Storage

SQLite is used to manage:

- Student information
- Face embeddings
- Lecture schedules
- Attendance records

</td></tr>
</table>---

How It Works

The complete system follows a controlled recognition-to-attendance pipeline:

┌─────────────────┐
│  Camera Input   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ OpenCV Frames   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Face Detection  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ DeepFace/ArcFace│
│   Embedding     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Face Comparison │
│ Cosine Distance │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Student Match   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Lecture Check   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Attendance      │
│ Validation      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ SQLite Storage  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ PyQt5 Dashboard │
└─────────────────┘

---

System Architecture

SmartGate is organized into several logical layers.

<table>
<tr>
<th>Layer</th>
<th>Responsibility</th>
</tr><tr>
<td><strong>Presentation</strong></td>
<td>PyQt5 dashboard, registration interface and user feedback</td>
</tr><tr>
<td><strong>Camera</strong></td>
<td>Real-time frame acquisition and camera processing</td>
</tr><tr>
<td><strong>AI / Vision</strong></td>
<td>Face detection, ArcFace embeddings and identity matching</td>
</tr><tr>
<td><strong>Business Logic</strong></td>
<td>Lecture validation, recognition results and attendance rules</td>
</tr><tr>
<td><strong>Data Layer</strong></td>
<td>SQLite database operations for students, schedule and attendance</td>
</tr></table>---

Face Recognition Pipeline

SmartGate uses DeepFace with ArcFace to generate a numerical representation of a detected face.

Step 1 — Capture

OpenCV receives frames from the connected camera.

Step 2 — Face Processing

The current frame is processed to obtain the face used by the recognition pipeline.

Step 3 — Embedding Generation

DeepFace generates an ArcFace embedding representing the facial features.

Step 4 — Database Comparison

The generated embedding is compared with registered embeddings.

The current implementation uses cosine distance for the comparison.

Step 5 — Threshold Validation

The configured matching threshold is:

0.4

A candidate must satisfy the configured distance condition to be considered a valid match.

Step 6 — Student Identification

The closest valid candidate is selected as the recognized student.

---

Attendance Workflow

Once a student is recognized, SmartGate connects the recognition result with the academic schedule.

                  Recognized Student
                         │
                         ▼
                ┌────────────────┐
                │ Active Lecture │
                │    Exists?     │
                └───────┬────────┘
                        │
                ┌───────┴───────┐
                │               │
               NO              YES
                │               │
                ▼               ▼
              Wait       Already Recorded?
                              │
                       ┌──────┴──────┐
                       │             │
                      YES            NO
                       │             │
                       ▼             ▼
                     Ignore       Record
                                     │
                                     ▼
                              Update Database
                                     │
                                     ▼
                              Update Dashboard

This prevents the same student from being repeatedly recorded for the same attendance context.

---

Application Interface

<div align="center"><img src="./images/demo1.png" width="900" alt="SmartGate Main Dashboard"><br><br>

Main Dashboard

The main interface combines the live camera feed, attendance information, lecture status and schedule.

<br><br>

<img src="./images/demo2.png" width="900" alt="SmartGate Application"></div>---

Technology Stack

<div align="center">Technology| Role
Python| Core application development
DeepFace| Face recognition pipeline
ArcFace| Facial embedding generation
OpenCV| Camera input and computer vision
NumPy| Numerical and vector operations
PyQt5| Desktop user interface
SQLite| Local persistent storage
TensorFlow| Deep learning backend
Pickle| Embedding serialization

</div>---

Database Architecture

The application uses a local SQLite database:

University.db

The database layer is separated into dedicated modules.

Student Data

Stores information required to identify registered students.

Student
├── ID
├── Name
├── Level
├── Department
├── Email
└── Face Embedding

Schedule Data

Provides lecture information required for active lecture detection.

Schedule
├── Lecture ID
├── Course
├── Day
├── Start Time
└── End Time

Attendance Data

Stores generated attendance records.

Attendance
├── Student ID
├── Lecture
├── Student Name
├── Level
├── Department
├── Date
└── Check-in Time

---

Project Structure

Smart_Attendance_System/
│
├── AttendanceDashboard.py
│   └── Main PyQt5 application
│
├── Register.py
│   └── Student registration
│
├── cameraThread.py
│   └── Camera processing thread
│
├── Embedding_pic.py
│   └── Face embedding generation
│
├── Compare_with_database.py
│   └── Face comparison
│
├── Mark_attendance.py
│   └── Attendance recording
│
├── Fetch_lecture.py
│   └── Lecture scheduling logic
│
├── Dashboard_data.py
│   └── Dashboard data operations
│
├── Data_Model.py
│   └── Application data models
│
├── DB_Setup.py
│   └── Database initialization
│
├── DB_Students.py
│   └── Student database operations
│
├── DB_Attendees.py
│   └── Attendance database operations
│
├── DB_Schedule.py
│   └── Schedule database operations
│
├── SQL_command.sql
│   └── SQL commands
│
├── Dark_Mood.py
│   └── Application styling
│
├── University.db
│   └── SQLite database
│
├── images/
│   ├── demo1.png
│   └── demo2.png
│
└── README.md

---

Getting Started

Prerequisites

Make sure you have:

- Python 3.10+
- Git
- A working webcam
- A compatible Python environment

---

Installation

1. Clone the repository

git clone https://github.com/mohamedwalidhegab12-dev/Smart_Attendance_System.git

cd Smart_Attendance_System

2. Create a virtual environment

python -m venv venv

3. Activate the environment

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate

4. Install dependencies

pip install opencv-python
pip install deepface
pip install numpy
pip install PyQt5
pip install tensorflow

---

Running the Application

Initialize the database:

python DB_Setup.py

Launch the main application:

python AttendanceDashboard.py

Once launched, SmartGate can access the camera and begin monitoring the current attendance context.

---

Student Registration

The registration process follows:

Student Information
        ↓
Camera Capture
        ↓
Face Processing
        ↓
ArcFace Embedding
        ↓
Duplicate Validation
        ↓
Database Registration

The registration module validates the submitted information and checks for existing records before adding the student.

---

Engineering Highlights

SmartGate demonstrates practical integration of several software engineering and AI concepts.

Artificial Intelligence

- Face recognition
- Facial embeddings
- Deep learning inference
- Similarity-based matching

Computer Vision

- Camera streaming
- Image processing
- Face detection
- Real-time frame handling

Software Engineering

- Modular Python architecture
- Separation of database operations
- GUI-driven application flow
- Event-based processing
- Threaded camera handling

Database Engineering

- SQLite persistence
- Student management
- Attendance records
- Academic scheduling
- SQL operations

---

Challenges & Design Decisions

Real-Time Processing

Camera processing needs to run without blocking the graphical interface.

Design approach: camera operations are handled through a dedicated camera thread so the PyQt5 interface remains responsive.

---

Recognition vs. Attendance

Recognizing a student does not automatically mean an attendance record should be created.

The system separates:

Recognition
     ↓
Lecture Validation
     ↓
Attendance Validation
     ↓
Database Record

This allows recognition and attendance management to remain separate responsibilities.

---

Duplicate Attendance

Repeated recognition of the same student should not create unlimited attendance records.

The system checks the attendance state before recording a new entry.

---

Future Roadmap

SmartGate can be extended into a larger university attendance platform.

Priority| Feature
High| Advanced liveness / anti-spoofing
High| Attendance analytics
High| CSV / Excel reports
Medium| Administrator authentication
Medium| Cloud database
Medium| Web administration dashboard
Medium| Multi-camera support
Future| University-wide centralized deployment

---

Project Scope

SmartGate currently focuses on a desktop-based academic attendance workflow.

The project demonstrates how AI can be integrated into a practical application rather than being limited to a standalone machine-learning experiment.

The system connects:

<div align="center">AI

↓

Computer Vision

↓

Application Logic

↓

Database

↓

User Interface

</div>---

Team

<div align="center"><table>
<tr><td align="center" width="33%">Mohamed Walid

AI / Software Development

</td><td align="center" width="33%">Malak Eldesouky

Team Member

</td><td align="center" width="33%">Saif Gamal

Team Member

</td></tr><tr><td align="center">John Hady

Team Member

</td><td align="center">Fatma Gahlan

Team Member

</td><td align="center">Mohamed Eleraqy

Supervisor

</td></tr>
</table></div>---

Academic Project

SmartGate was developed as an academic project focused on applying Artificial Intelligence and Software Engineering to a real-world university problem.

Core Areas

"Artificial Intelligence"
"Computer Vision"
"Face Recognition"
"Deep Learning"
"Database Systems"
"Desktop Application Development"

---

<div align="center"><br>SmartGate

Recognize. Verify. Record.

<br><img src="https://img.shields.io/badge/Built%20with-Python%20%7C%20DeepFace%20%7C%20ArcFace%20%7C%20OpenCV%20%7C%20PyQt5%20%7C%20SQLite-111827?style=for-the-badge"><br><br>

<a href="https://github.com/mohamedwalidhegab12-dev/Smart_Attendance_System">
<img src="https://img.shields.io/badge/View%20Source%20Code-GitHub-181717?style=for-the-badge&logo=github">
</a><br><br>

<sub>Academic AI & Computer Vision Project</sub>

</div>
