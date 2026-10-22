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
