# 🎓 SmartGate: Advanced AI Attendance System

![Status: Stable](https://img.shields.io/badge/Status-Stable-brightgreen)
![Version: 1.0.0](https://img.shields.io/badge/Version-1.0.0-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)

**SmartGate** is a robust, real-time facial recognition solution designed to automate attendance tracking in academic environments. By leveraging Deep Learning and Computer Vision, the system ensures high accuracy, prevents fraud, and eliminates the administrative burden of manual attendance.

---

## 🏗️ System Architecture

The system follows a modular architecture to ensure high performance and low latency without the need for high-end hardware:
```text
       [ CAMERA INPUT ] 
              |
      [ LIVENESS ENGINE ] ---> (Anti-Spoofing: Texture & Depth Check)
              |
     [ FACE RECOGNITION ] ---> (128-d Embedding Extraction)
              |
      [ LOGIC HANDLER ]  <--- (Schedule & Timetable Sync)
              |
     [ SQLITE DATABASE ] <--- (Persistent Logs & Student Data)
              |
       [ PyQt5 DASHBOARD ] ---> (Real-time Visual Feedback)
