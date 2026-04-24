import sqlite3
from datetime import datetime

def fetch_lecture_from_db():
    try:
        conn = sqlite3.connect("University.db")
        cursor = conn.cursor()
        
        # Get current day name (e.g., Monday) and time (HH:MM)
        current_day = datetime.now().strftime("%A") 
        current_time = datetime.now().strftime("%H:%M")

        # Query to find a lecture where the current time is between start and end
        query = """
            SELECT id, course FROM Schedule 
            WHERE day = ? AND ? BETWEEN start_time AND end_time
        """
        cursor.execute(query, (current_day, current_time))
        result = cursor.fetchone()
        
        conn.close()
        return result  # Returns (ID, Name) if found, else returns None
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None
    
def get_today_schedule():
    try:
        conn = sqlite3.connect("University.db")
        cursor = conn.cursor()
        
        current_day = datetime.now().strftime("%A") 

        query = """
            SELECT DISTINCT course, start_time, end_time 
            FROM Schedule 
            WHERE day = ? 
        """
        cursor.execute(query, (current_day,))
        rows = cursor.fetchall()
        conn.close()

        schedule_list = []
        for row in rows:
            schedule_list.append({
                'name': row[0],
                'start_raw': row[1],
                'end_raw': row[2]
            })

        schedule_list.sort(key=lambda x: datetime.strptime(x['start_raw'], "%H:%M"))

        final_list = []
        for item in schedule_list:
            final_list.append({
                'name': item['name'],
                'start': datetime.strptime(item['start_raw'], "%H:%M").strftime("%I:%M %p"),
                'end': datetime.strptime(item['end_raw'], "%H:%M").strftime("%I:%M %p")
            })

        return final_list
        
    except Exception as e:
        print(f"Error fetching today's schedule: {e}")
        return []