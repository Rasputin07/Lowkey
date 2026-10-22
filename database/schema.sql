-- database/schema.sql
CREATE TABLE IF NOT EXISTS students (
    student_id TEXT PRIMARY KEY,
    name TEXT,
    department TEXT,
    semester INTEGER
);

CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT,
    week INTEGER,
    classes_held INTEGER,
    classes_attended INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
);

CREATE TABLE IF NOT EXISTS assignments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT,
    week INTEGER,
    assignments_due INTEGER,
    assignments_submitted INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
);

-- Track individual subjects
CREATE TABLE IF NOT EXISTS subjects (
    subject_id TEXT PRIMARY KEY,
    subject_name TEXT
);

-- Replace the old assignments table with a detailed subject-wise table
CREATE TABLE IF NOT EXISTS student_assignments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT,
    subject_id TEXT,
    title TEXT,
    due_date TEXT,
    status TEXT, -- Values: 'submitted', 'missed', 'pending'
    FOREIGN KEY(student_id) REFERENCES students(student_id),
    FOREIGN KEY(subject_id) REFERENCES subjects(subject_id)
);

-- Store previous semester results for CGPA
CREATE TABLE IF NOT EXISTS academic_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT,
    semester INTEGER,
    credits INTEGER,
    grade_points INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
);
