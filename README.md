# 🎓 SmartGate: AI-Driven Attendance System

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-green?style=for-the-badge&logo=opencv)
![PyQt5](https://img.shields.io/badge/PyQt5-GUI-red?style=for-the-badge&logo=qt)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite)

**SmartGate** is a high-performance, automated attendance system that replaces manual logs with real-time **AI Face Recognition**. Designed for modern educational environments, it combines security through **Liveness Detection** with a sleek, dark-themed management dashboard.

---

## 🎬 Live Demo & Interface

### 1. Seamless Recognition
As soon as a student is detected, the system locks on their face and instantly records their presence in the attendance log.
![Main Interface](Screenshot%202026-04-19%20123501.png)

### 2. Smart Validation Logic
The system is "context-aware"—it knows if a student has already checked in and prevents duplicate entries with clear visual feedback.
![Validation Feedback](Screenshot%202026-04-19%20123558.png)

---

## 🚀 Key Innovation: "The Three Pillars"

*   **🛡️ Anti-Spoofing (Liveness Detection):** Unlike basic recognition tools, SmartGate analyzes texture and color depth to ensure it is identifying a real human, not a photo or a screen.
*   **📅 Dynamic Schedule Sync:** The system automatically identifies the current active lecture (e.g., *Structured Programming*) and logs attendance accordingly.
*   **🧵 Multi-threaded Architecture:** Using Python's threading, the UI stays 100% responsive while the AI processes heavy image data in the background.

---

## 🧠 System Logic Flow

1.  **Capture:** Real-time frames are captured via OpenCV.
2.  **Liveness Check:** The engine verifies the physical presence of the user.
3.  **Recognition:** Face embeddings are extracted and compared with the `SQLite` database.
4.  **Logging:** If a match is found and not already checked in, the `LECTURE ATTENDANCE` table updates instantly.
5.  **UI Feedback:** Color-coded status messages (Green/Blue) guide the user.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Vision:** OpenCV, Face_Recognition
- **GUI:** PyQt5 (Dark Mode optimized)
- **Database:** SQLite3

---

## 📦 Structure
```text
├── main.py              # Application Entry Point
├── cameraThread.py      # Background AI Processing
├── DB_Manager.py        # SQL Database Logic
├── screenshots/         # UI Assets
└── dataset/             # Student Face Data
