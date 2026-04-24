import sqlite3
from DB_Students import  create_Sudents_table
from DB_Schedule import create_Schedule_from_sql
from DB_Attendees import create_attendees_table

def setup_database():
    
    # Create Students Table
    create_Sudents_table()
    print("Students is ready!") 

    # Create Schedule Table
    create_Schedule_from_sql()
    print("Schedule is ready!") 

    # Create Attendees Table
    create_attendees_table()
    print("Attendees is ready!") 
    
setup_database()