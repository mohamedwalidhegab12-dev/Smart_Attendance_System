# Smart_Attendance_System
## 🔹 Registration Function
This function is responsible for adding a new student to the system when their face is not recognized.

### 🎯 Purpose
To register a new student by capturing their facial data, storing their information, and integrating them into the attendance system.

### ⚙️ Function Responsibilities
- Accept student input:
  - Name
  - ID
- Capture the student's face using the camera
- Generate face encoding using the face recognition module
- Extract the student's academic year from the ID
- Automatically assign the student to a schedule based on their academic year
- Store student data in the database:
  - ID
  - Name
  - Year
  - Face Encoding
- Add the face encoding to the dataset for future recognition
- Allow the student to proceed to attendance marking

### 🔄 Workflow
1. System detects an unknown face
2. Prompt user to enter Name and ID
3. Capture face image via camera
4. Convert image to face encoding
5. Determine student year based on ID
6. Assign schedule based on academic year
7. Save student data into database
8. Update encodings dataset
9. Detect current lecture based on time
10. Mark attendance for the student
11. Display student details and attendance status

### ⏰ Attendance Rules
- Each lecture has a fixed duration of **2 hours**
- A student can mark attendance **only once per lecture**
- Any repeated attempt within the same lecture time will be rejected
- Attendance is only allowed within the lecture time window

### 🚫 Constraints
- The same student ID cannot be registered more than once
- A valid face must be detected before saving the student
- Duplicate attendance (same student + same lecture + same date) is not allowed

### 📌 Notes
- Face encoding is used for future recognition
- Student schedule is assigned automatically based on their academic year
- After registration, the student is treated as a recognized user in subsequent sessions