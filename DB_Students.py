import sqlite3 
import pickle

class DatabaseError(Exception):
    pass

DB_NAME = "University.db"
# create database
def create_Sudents_table():
    con = sqlite3.connect(DB_NAME)
    cursor = con.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        Name TEXT,          
        ID INTEGER PRIMARY KEY,
        Level INTEGER,
        Department TXTE,
        Email TEXT ,                      
        Embedding BLOB
    )
    """)

    con.commit()
    con.close()


# insert into database
def insert_student(name, student_id, level, department, email, embedding):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO students (Name, ID, Level, Department, Email, Embedding)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (name, student_id, level,department, email, embedding))

        conn.commit()
        conn.close()

    except sqlite3.IntegrityError:
        raise DatabaseError("Student with this ID already exists")

    except Exception as e:
        raise DatabaseError(f"Insert failed: {e}")    