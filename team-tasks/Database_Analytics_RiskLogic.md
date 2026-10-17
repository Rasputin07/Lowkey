Primary Responsibility

Design the database, prepare consistent demonstration data, calculate academic indicators, and implement the initial explainable risk-assessment logic.

***A. Tasks to Complete***

**1. Design the Database**

Use SQLite for the initial prototype.

Create appropriate tables for the information the team actually needs.

Suggested tables include:

students

attendance

assignments

student_assignments

academic_results

lms_activity

risk_assessments

interventions

users

consent_records

The first prototype may use fewer tables if the team can demonstrate its core workflow reliably.

**2. Prepare the Demonstration Dataset**

Create a consistent fictional dataset containing approximately:

30 students.

5 subjects.

8 weeks of academic records.

Assignment submission records.

Internal assessment results.

LMS activity records.

10–15 demonstration intervention records, where useful.

All records must be clearly labelled as fictional demonstration data.

Ensure that attendance, marks, assignment submissions, and risk explanations agree with one another.

**3. Implement Data Validation**

Check for:

Missing student identifiers.

Duplicate records.

Invalid attendance values.

Attendance percentages above 100%.

Marks outside the permitted range.

Invalid dates.

Missing or inconsistent records.

Document how incomplete records are handled.

**4. Calculate Academic Indicators**

Implement calculations such as:

Attendance percentage

(Classes Attended / Classes Held) × 100

Assignment completion rate

(Assignments Submitted / Assignments Due) × 100

SGPA, where credit and grade-point data are available

SGPA = Σ(Credits × Grade Points) / Σ(Credits)

The team must use the institution's applicable grading rules when calculating actual academic metrics.

**5. Implement Initial Risk Rules**

Create transparent rules for indicators such as:

Significant attendance decline.

Repeated missed assignments.

Declining internal marks.

Reduced LMS activity.

Multiple simultaneous warning signs.

The rules should be documented and agreed upon by the team.

For each assessment, return the relevant indicators and evidence.

Do not describe a manually designed rule-based system as a validated machine-learning dropout predictor.

**6. Implement Weekly Trends**

Calculate changes over time so that the system can distinguish between:

A single low score.

A sustained decline.

A recent improvement.

Multiple indicators worsening together.

**7. Support the What-If Simulator**

Where implemented, allow the backend to recalculate an indicator under a hypothetical scenario.

For example, recalculate an attendance-related indicator when the hypothetical attendance value is changed.

Clearly distinguish the simulated result from the student's actual record.

**8. Prepare Data for the Fairness Panel**

If suitable group-level data is available, support the calculation of appropriate evaluation metrics.

If the demonstration data is artificial or too small, document that the results cannot establish real-world fairness or predictive validity.

***B. Expected Deliverables***

By the departmental round:

A working SQLite database.

A consistent fictional dataset.

Data validation functions.

Academic indicator calculations.

Initial rule-based risk logic.

Evidence and explanations for risk assessments.

Data that the frontend and GenAI component can use.

***C. Files This Member May Own***

data/
├── sample_students.csv
├── sample_attendance.csv
└── sample_academic_records.csv

database/
├── schema.sql
└── db.py

analytics/
├── indicators.py
├── risk_rules.py
└── trends.py

The team can modify this structure to fit the actual implementation.

***D. How This Member Works with Others***

With Member 1: Supplies consistent fields, calculated indicators, and risk explanations for display.

With Member 3: Supplies the factual academic information used to ground GenAI responses.

With Member 4: Agrees on database access methods, data formats, and backend integration.

***E. Completion Criteria***

Member 2's work is ready when the application can retrieve consistent fictional records, calculate academic indicators correctly, identify relevant warning signs, and explain those findings using the underlying data.

