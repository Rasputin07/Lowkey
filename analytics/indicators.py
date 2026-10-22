# analytics/indicators.py
from database.db import get_connection

def calculate_overall_attendance(student_id):
    """Calculates: (Classes Attended / Classes Held) * 100"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''SELECT SUM(classes_attended) as attended, SUM(classes_held) as held 
                      FROM attendance WHERE student_id = ?''', (student_id,))
    result = cursor.fetchone()
    conn.close()
    
    if not result['held'] or result['held'] == 0:
        return 0.0
    
    return round((result['attended'] / result['held']) * 100, 2)

def calculate_assignment_completion(student_id):
    """Calculates: (Assignments Submitted / Assignments Due) * 100"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''SELECT SUM(assignments_submitted) as sub, SUM(assignments_due) as due 
                      FROM assignments WHERE student_id = ?''', (student_id,))
    result = cursor.fetchone()
    conn.close()
    
    if not result['due'] or result['due'] == 0:
        return 100.0 # No assignments due yet
        
    return round((result['sub'] / result['due']) * 100, 2)
