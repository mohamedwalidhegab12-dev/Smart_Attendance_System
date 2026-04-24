import sqlite3
from datetime import datetime

def get_dashboard_data(): 
    try: 
        db = sqlite3.connect("University.db")
        cursor = db.cursor()
    
        today = datetime.now().strftime("%Y-%m-%d")

        query = """
            SELECT StudentID, Name, Lecture_Name, CheckIn 
            FROM Attendees 
            WHERE AttendanceDate = ?
            ORDER BY ID ASC
        """

        cursor.execute(query, (today,)) 
        rows = cursor.fetchall()
        db.close()

        final_list = []
        for row in rows:
            raw_time = row[3] 
            try:
                display_time = datetime.strptime(raw_time, "%H:%M").strftime("%I:%M %p")
            except:
                display_time = raw_time

            final_list.append({
                "student_id": row[0],
                "name": row[1],
                "lecture_name": row[2],
                "time": display_time
            })

        return final_list
        
    except Exception as e:
        print(f"Error fetching today's attendees: {e}")
        return []