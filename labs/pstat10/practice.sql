DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    major TEXT,
    gpa REAL
);

INSERT INTO students (name, major, gpa) VALUES
    ('Alice', 'Data Science', 3.8),
    ('Bob', 'Statistics', 3.2),
    ('Carol', 'Computer Science', 3.9),
    ('Dan', 'Data Science', 2.9);

SELECT name, gpa FROM students WHERE gpa > 3.0 ORDER BY gpa DESC;

SELECT major, COUNT(*) AS num_students, AVG(gpa) AS avg_gpa
FROM students
GROUP BY major;