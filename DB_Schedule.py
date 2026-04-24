import sqlite3
import os


# ── Configuration ────────────────────────────────────────────
SQL_FILE = "SQL_command.sql"   # <-- change this to your txt file name
DB_NAME  = "University.db"
# ─────────────────────────────────────────────────────────────
 
 
def create_Schedule_from_sql():
    """
    Reads a .sql / .txt file that contains CREATE TABLE + INSERT statements
    and executes them against a local SQLite database.
    """
    # Make sure the SQL file exists
    if not os.path.exists(SQL_FILE):
        print(f"[ERROR] SQL file not found: '{SQL_FILE}'")
        print("Make sure the file is in the same folder as this script.")
        return
 
    # Read the SQL file
    with open(SQL_FILE, "r", encoding="utf-8") as f:
        sql_script = f.read()
 
    # Connect (creates the .db file if it doesn't exist)
    con = sqlite3.connect(DB_NAME)
    cursor = con.cursor()
 
    # Execute the entire script at once
    cursor.executescript(sql_script)
 
    con.commit()
    con.close()