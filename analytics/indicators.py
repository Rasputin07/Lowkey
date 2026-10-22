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

def get_subject_wise_assignments(student_id):
    """Returns assignment completion status grouped by subject."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Get total and submitted counts per subject
    cursor.execute('''
        SELECT 
            s.subject_name,
            COUNT(a.id) as total_assignments,
            SUM(CASE WHEN a.status = 'submitted' THEN 1 ELSE 0 END) as submitted
        FROM student_assignments a
        JOIN subjects s ON a.subject_id = s.subject_id
        WHERE a.student_id = ?
        GROUP BY s.subject_id
    ''', (student_id,))
    
    results = cursor.fetchall()
    conn.close()
    
    subject_data = []
    for row in results:
        completion_rate = (row['submitted'] / row['total_assignments']) * 100 if row['total_assignments'] > 0 else 100
        subject_data.append({
            "subject": row['subject_name'],
            "total": row['total_assignments'],
            "submitted": row['submitted'],
            "completion_rate": round(completion_rate, 2)
        })
        
    return subject_data


def calculate_cgpa(student_id):
    """Calculates cumulative GPA based on past semester credits and grade points."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT SUM(credits * grade_points) as total_points, SUM(credits) as total_credits
        FROM academic_results 
        WHERE student_id = ?
    ''', (student_id,))
    
    result = cursor.fetchone()
    conn.close()
    
    if not result['total_credits'] or result['total_credits'] == 0:
        return None # No academic history yet
        
    cgpa = result['total_points'] / result['total_credits']
    return round(cgpa, 2)




