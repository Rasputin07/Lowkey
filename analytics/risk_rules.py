# analytics/risk_rules.py
from analytics.indicators import calculate_overall_attendance, calculate_assignment_completion

def assess_student_risk(student_id):
    """
    Evaluates rule-based indicators and returns a risk profile with evidence.
    """
    attendance_pct = calculate_overall_attendance(student_id)
    assignment_pct = calculate_assignment_completion(student_id)
    
    flags = []
    
    if attendance_pct < 75.0:
        flags.append({
            "indicator": "Low Attendance",
            "evidence": f"Attendance is currently at {attendance_pct}%, which is below the 75% threshold."
        })
        
    if assignment_pct < 60.0:
        flags.append({
            "indicator": "Missed Assignments",
            "evidence": f"Assignment completion is at {assignment_pct}%, indicating repeated missed coursework."
        })
        
    status = "Support recommended" if len(flags) > 0 else "On Track"
    
    return {
        "student_id": student_id,
        "status": status,
        "active_flags": flags
    }
