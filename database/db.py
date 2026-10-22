# database/db.py
import sqlite3
import csv
import os

DB_PATH = 'lowkey.db'
SCHEMA_PATH = 'database/schema.sql'

def get_connection():
    """Returns a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row # Returns dict-like rows
    return conn

def initialize_database():
    """Builds tables from schema and loads mock data if empty."""
    conn = get_connection()
    cursor = conn.cursor()
    
    with open(SCHEMA_PATH, 'r') as f:
        cursor.executescript(f.read())
    
    # Simple check to see if we need to load mock data
    cursor.execute("SELECT COUNT(*) FROM students")
    if cursor.fetchone()[0] == 0:
        load_mock_data(conn)
    
    conn.commit()
    conn.close()

def load_mock_data(conn):
    """Loads CSV data into the database with basic validation."""
    cursor = conn.cursor()
    
    # Load Students
    with open('data/sample_students.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row['student_id']: continue # Validation: Skip missing IDs
            cursor.execute('''INSERT INTO students (student_id, name, department, semester) 
                              VALUES (?, ?, ?, ?)''', 
                           (row['student_id'], row['name'], row['department'], row['semester']))

    # Load Attendance
    with open('data/sample_attendance.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            attended, held = int(row['classes_attended']), int(row['classes_held'])
            # Validation: Cap attendance at 100%
            if attended > held: attended = held 
            
            cursor.execute('''INSERT INTO attendance (student_id, week, classes_held, classes_attended) 
                              VALUES (?, ?, ?, ?)''', 
                           (row['student_id'], row['week'], held, attended))

    print("Mock data loaded successfully.")

# Run this when testing the file directly
if __name__ == '__main__':
    initialize_database()
