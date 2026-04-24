import sqlite3
from datetime import datetime

def mark_attendance(student_id, lecture_id):
    con = sqlite3.connect("University.db")
    cursor = con.cursor()
    
    today = datetime.now().strftime("%Y-%m-%d")
    now_time = datetime.now().strftime("%H:%M")

    try:
        cursor.execute("SELECT Name, Level, Department FROM Students WHERE ID = ?", (student_id,))
        student_info = cursor.fetchone()
        
        if not student_info:
            return {"status": "error", "message": "Student ID not found."}

        s_name, s_level, s_department = student_info

        cursor.execute("SELECT course FROM schedule WHERE id = ?", (lecture_id,))
        lecture_result = cursor.fetchone()
        
        if not lecture_result:
            return {"status": "error", "message": "Lecture ID not found."}
        
        course_name = lecture_result[0]

        cursor.execute("""
            INSERT INTO Attendees (StudentID, LectureID, Lecture_Name, Name, Level, Department, CheckIn, AttendanceDate)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (student_id, lecture_id, course_name, s_name, s_level, s_department, now_time, today))
        
        con.commit()
        
        return {
            "status": "success",
            "message": f"Welcome {s_name}! to lecture {course_name}.",
            "data": {
                "name": s_name,
                "lecture_name": course_name,
                "time": now_time,
                "level": s_level,
            }
        }

    except sqlite3.IntegrityError:
        return {
            "status": "already_marked",
            "message": f"Student {s_name} is already checked in for this lecture today."
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        con.close()