# analytics/trends.py
from database.db import get_connection

def get_weekly_attendance_trend(student_id):
    """Returns a list of attendance percentages grouped by week to support visualizations."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''SELECT week, classes_attended, classes_held 
                      FROM attendance WHERE student_id = ? ORDER BY week ASC''', (student_id,))
    rows = cursor.fetchall()
    conn.close()
    
    trend = []
    for r in rows:
        pct = round((r['classes_attended'] / r['classes_held']) * 100, 2) if r['classes_held'] > 0 else 0
        trend.append({"week": r['week'], "attendance_percent": pct})
        
    return trend
