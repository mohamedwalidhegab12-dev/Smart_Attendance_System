<div align="center">

# SMARTGATE

### AI-Powered Smart Attendance System

<p>
An intelligent desktop application that automates university attendance
using real-time facial recognition and lecture scheduling.
</p>

<br>

<a href="https://github.com/mohamedwalidhegab12-dev/Smart_Attendance_System">
<img src="https://img.shields.io/badge/VIEW%20REPOSITORY-181717?style=for-the-badge&logo=github&logoColor=white">
</a>

<br><br>

<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/DeepFace-ArcFace-6C5CE7?style=flat-square">
<img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=flat-square&logo=opencv&logoColor=white">
<img src="https://img.shields.io/badge/PyQt5-Desktop%20GUI-41CD52?style=flat-square&logo=qt&logoColor=white">
<img src="https://img.shields.io/badge/SQLite-Database-003B57?style=flat-square&logo=sqlite&logoColor=white">
<img src="https://img.shields.io/badge/TensorFlow-Deep%20Learning-FF6F00?style=flat-square&logo=tensorflow&logoColor=white">

<br><br>

<em>Recognize. Verify. Record.</em>

</div>

---

## 📌 Project Overview

**SmartGate** is an AI-powered university attendance system designed to
automate the process of identifying students and recording their attendance.

The system combines **Computer Vision, Face Recognition, Deep Learning,
Database Management, and Desktop Application Development** into one
integrated workflow.

Instead of relying on traditional manual attendance, SmartGate uses a
camera to recognize registered students and automatically connect their
presence to the currently active lecture.

---

## 🎯 The Problem

Traditional attendance methods can be:

- Time-consuming
- Repetitive
- Difficult to manage
- Prone to duplicate records
- Dependent on manual data entry

SmartGate was designed to provide a more automated and structured approach.

---

## 💡 The Solution

SmartGate connects the complete attendance process into one pipeline:

<div align="center">

<table>
<tr>

<td align="center" width="20%">

### 📷
<br>
<strong>Camera</strong>
<br>
<sub>Live video input</sub>

</td>

<td align="center" width="20%">

### 👤
<br>
<strong>Recognition</strong>
<br>
<sub>Face identification</sub>

</td>

<td align="center" width="20%">

### 📚
<br>
<strong>Lecture</strong>
<br>
<sub>Schedule validation</sub>

</td>

<td align="center" width="20%">

### ✓
<br>
<strong>Attendance</strong>
<br>
<sub>Record validation</sub>

</td>

<td align="center" width="20%">

### 🗄️
<br>
<strong>Database</strong>
<br>
<sub>Persistent storage</sub>

</td>

</tr>
</table>

</div>

---

# ✨ Key Features

<div align="center">

<table>
<tr>

<td width="50%" valign="top">

### 👤 Face Recognition

Real-time student identification using:

- DeepFace
- ArcFace
- Facial embeddings
- Cosine distance
- Recognition threshold

</td>

<td width="50%" valign="top">

### 📝 Smart Attendance

Automatically:

- Identifies registered students
- Detects the active lecture
- Records attendance
- Prevents duplicate records

</td>

</tr>

<tr>

<td width="50%" valign="top">

### 👨‍🎓 Student Registration

Dedicated workflow for:

- Student information
- Camera capture
- Face embedding generation
- Duplicate validation
- Database registration

</td>

<td width="50%" valign="top">

### 📅 Lecture Scheduling

Schedule-aware attendance based on:

- Current day
- Current time
- Lecture start time
- Lecture end time
- Active lecture detection

</td>

</tr>

<tr>

<td width="50%" valign="top">

### 🖥️ Real-Time Dashboard

PyQt5 interface providing:

- Live camera feed
- Attendance information
- Lecture information
- Daily schedule
- System status

</td>

<td width="50%" valign="top">

### 🗄️ Database Management

SQLite stores:

- Student information
- Face embeddings
- Lecture schedules
- Attendance records

</td>

</tr>

</table>

</div>

---

# 🧠 How SmartGate Works

<div align="center">

<table>
<tr>
<th>Stage</th>
<th>Process</th>
<th>Technology</th>
</tr>

<tr>
<td align="center"><strong>01</strong></td>
<td>Capture live camera frames</td>
<td>OpenCV</td>
</tr>

<tr>
<td align="center"><strong>02</strong></td>
<td>Process and detect the face</td>
<td>Computer Vision</td>
</tr>

<tr>
<td align="center"><strong>03</strong></td>
<td>Generate facial embedding</td>
<td>DeepFace / ArcFace</td>
</tr>

<tr>
<td align="center"><strong>04</strong></td>
<td>Compare with registered embeddings</td>
<td>Cosine Distance</td>
</tr>

<tr>
<td align="center"><strong>05</strong></td>
<td>Identify the registered student</td>
<td>Recognition Engine</td>
</tr>

<tr>
<td align="center"><strong>06</strong></td>
<td>Check the active lecture</td>
<td>Schedule Logic</td>
</tr>

<tr>
<td align="center"><strong>07</strong></td>
<td>Validate attendance</td>
<td>Attendance Logic</td>
</tr>

<tr>
<td align="center"><strong>08</strong></td>
<td>Store and display the result</td>
<td>SQLite + PyQt5</td>
</tr>

</table>

</div>

---

# 🏗️ System Architecture

<div align="center">

<table>
<tr>

<td align="center" width="25%">

### Presentation Layer

PyQt5

<br>

Dashboard  
Registration  
System Status

</td>

<td align="center" width="25%">

### AI Layer

DeepFace  
ArcFace  
Embeddings

<br>

Face Recognition

</td>

<td align="center" width="25%">

### Logic Layer

Lecture Validation  
Attendance Rules  
Recognition Logic

</td>

<td align="center" width="25%">

### Data Layer

SQLite

<br>

Students  
Schedule  
Attendance

</td>

</tr>
</table>

</div>

---

# 👁️ Face Recognition Pipeline

The recognition engine follows a controlled process.

### 01 — Capture

OpenCV receives frames from the connected camera.

### 02 — Face Processing

The current frame is processed for facial recognition.

### 03 — Embedding Generation

DeepFace uses **ArcFace** to generate a numerical representation
of the detected face.

### 04 — Face Comparison

The generated embedding is compared against registered embeddings
using **cosine distance**.

### 05 — Threshold Validation

The current implementation uses:

```text
Recognition Threshold = 0.4
