import sqlite3

DB_NAME = "University.db"
def create_attendees_table():
    # Connect to the DB
    con = sqlite3.connect(DB_NAME)
    cursor = con.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")

    # Create the table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Attendees (
        ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        StudentID INTEGER,                    
        LectureID INTEGER,                    
        Lecture_Name Text ,                       
        Name TEXT,                             
        Level INTEGER,  
        Department TEXT,                       
        CheckIn TEXT DEFAULT (TIME('now', 'localtime')),              -- Time
        AttendanceDate TEXT DEFAULT (DATE('now', 'localtime')),       -- Date         
        
        -- No double attendance for same student & lecture & day
        UNIQUE(StudentID, LectureID, AttendanceDate),
        FOREIGN KEY (StudentID) REFERENCES Students(ID),
        FOREIGN KEY (LectureID) REFERENCES Lectures(ID)           
    )
    """)
    
    con.commit()
    con.close()