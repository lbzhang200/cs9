-- =====================================================================
--  SQL BASICS — catch-up file (SQLite)
--
--  HOW TO RUN (terminal, in the folder with this file):
--      sqlite3 school.db < sql_basics.sql
--  Or interactively, so you can play:
--      sqlite3 school.db
--      .read sql_basics.sql
--      then type your own queries, ending each with ;   (.quit to exit)
--
--  Everything below is safe to rerun: it rebuilds the tables each time.
--  Read the comment, GUESS the result, then run and check.
--  Practice problems at the bottom, answers below them.
-- =====================================================================

-- Lines starting with a dot (.headers, .mode, .print) are SQLite-only "dot commands"
-- that make the output readable.
-- (If you ever run this in a VS Code SQL extension, delete those lines.)
.headers on
.mode column


-- ---------------------------------------------------------------------
-- 0. BUILD THE DATABASE
--    A database = a set of TABLES. Each table = rows + named columns.
--    PRIMARY KEY = unique id for each row.
--    FOREIGN KEY = a column that points to another table's id.
-- ---------------------------------------------------------------------
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS courses;

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name       TEXT NOT NULL,
    major      TEXT,
    year       INTEGER,          -- 1 = freshman ... 4 = senior
    gpa        REAL
);

CREATE TABLE courses (
    course_id  TEXT PRIMARY KEY,
    title      TEXT,
    dept       TEXT,
    units      INTEGER
);

CREATE TABLE enrollments (
    student_id INTEGER,
    course_id  TEXT,
    quarter    TEXT,
    grade      REAL,              -- grade points (4.0 = A); NULL = in progress
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id)  REFERENCES courses(course_id)
);

INSERT INTO students (student_id, name, major, year, gpa) VALUES
    (1, 'Alice',  'Data Science',     3, 3.8),
    (2, 'Bob',    'Statistics',       2, 3.2),
    (3, 'Carol',  'Computer Science', 4, 3.9),
    (4, 'Dan',    'Data Science',     1, 2.9),
    (5, 'Eve',    'Statistics',       3, 3.6),
    (6, 'Frank',  'Mathematics',      2, 3.1),
    (7, 'Grace',  'Computer Science', 1, NULL),   -- no GPA yet
    (8, 'Leo',    'Data Science',     3, 3.7);

INSERT INTO courses (course_id, title, dept, units) VALUES
    ('PSTAT10',   'Principles of Data Science with R', 'PSTAT', 5),
    ('PSTAT120A', 'Probability',                       'PSTAT', 4),
    ('CS9',       'Intermediate Python',               'CS',    4),
    ('MATH8',     'Transition to Higher Math',         'MATH',  5),
    ('CS16',      'Problem Solving with C++',          'CS',    4);   -- nobody enrolled

INSERT INTO enrollments (student_id, course_id, quarter, grade) VALUES
    (1, 'PSTAT10',   'F26', 4.0),
    (1, 'PSTAT120A', 'F26', 3.7),
    (2, 'PSTAT10',   'F26', 3.0),
    (2, 'MATH8',     'F26', 2.7),
    (3, 'CS9',       'F26', 4.0),
    (4, 'PSTAT10',   'F26', 2.3),
    (4, 'CS9',       'F26', NULL),
    (5, 'PSTAT120A', 'F26', 3.3),
    (5, 'MATH8',     'F26', 3.7),
    (6, 'MATH8',     'F26', 3.0),
    (8, 'PSTAT10',   'F26', NULL),
    (8, 'PSTAT120A', 'F26', NULL),
    (8, 'CS9',       'F26', NULL),
    (8, 'MATH8',     'F26', NULL);
-- note: Grace (7) has no enrollments


-- ---------------------------------------------------------------------
-- 1. SELECT ... FROM   (pick columns)
-- ---------------------------------------------------------------------
.print
.print --- 1a. everything ---
SELECT * FROM students;

.print
.print --- 1b. specific columns ---
SELECT name, major FROM students;

.print
.print --- 1c. aliases + computed columns ---
SELECT name,
       gpa,
       gpa * 25 AS gpa_out_of_100        -- AS renames the column
FROM students;

.print
.print --- 1d. DISTINCT = unique values ---
SELECT DISTINCT major FROM students;


-- ---------------------------------------------------------------------
-- 2. WHERE   (filter rows)
--    = equal   <> or != not equal   < > <= >=   AND OR NOT
-- ---------------------------------------------------------------------
.print
.print --- 2a. gpa above 3.5 ---
SELECT name, gpa FROM students WHERE gpa > 3.5;

.print
.print --- 2b. AND / OR ---
SELECT name, major, year FROM students
WHERE major = 'Data Science' AND year >= 3;

SELECT name, major FROM students
WHERE major = 'Statistics' OR major = 'Mathematics';

.print
.print --- 2c. IN (shortcut for many ORs) ---
SELECT name, major FROM students
WHERE major IN ('Statistics', 'Mathematics');

.print
.print --- 2d. BETWEEN (inclusive) ---
SELECT name, gpa FROM students WHERE gpa BETWEEN 3.0 AND 3.6;

.print
.print --- 2e. LIKE pattern matching: % = any chars, _ = one char ---
SELECT name FROM students WHERE name LIKE 'A%';        -- starts with A
SELECT title FROM courses WHERE title LIKE '%Data%';   -- contains Data

.print
.print --- 2f. NULL: must use IS NULL, not = NULL ---
SELECT name FROM students WHERE gpa IS NULL;
SELECT name FROM students WHERE gpa IS NOT NULL;


-- ---------------------------------------------------------------------
-- 3. ORDER BY + LIMIT   (sort, take top N)
-- ---------------------------------------------------------------------
.print
.print --- 3a. sort by gpa, highest first ---
SELECT name, gpa FROM students ORDER BY gpa DESC;

.print
.print --- 3b. sort by two columns ---
SELECT name, major, gpa FROM students ORDER BY major ASC, gpa DESC;

.print
.print --- 3c. top 3 ---
SELECT name, gpa FROM students ORDER BY gpa DESC LIMIT 3;


-- ---------------------------------------------------------------------
-- 4. AGGREGATE FUNCTIONS   (collapse many rows into one number)
--    COUNT  SUM  AVG  MIN  MAX
-- ---------------------------------------------------------------------
.print
.print --- 4a. whole-table summaries ---
SELECT COUNT(*)            AS num_students,
       COUNT(gpa)          AS num_with_gpa,     -- COUNT(col) skips NULLs
       ROUND(AVG(gpa), 2)  AS avg_gpa,          -- AVG ignores NULLs
       MIN(gpa)            AS lowest,
       MAX(gpa)            AS highest
FROM students;


-- ---------------------------------------------------------------------
-- 5. GROUP BY + HAVING   (summaries PER group)
--    WHERE filters rows BEFORE grouping, HAVING filters groups AFTER.
-- ---------------------------------------------------------------------
.print
.print --- 5a. per major ---
SELECT major,
       COUNT(*)           AS n,
       ROUND(AVG(gpa), 2) AS avg_gpa
FROM students
GROUP BY major
ORDER BY n DESC;

.print
.print --- 5b. HAVING: only majors with 2+ students ---
SELECT major, COUNT(*) AS n
FROM students
GROUP BY major
HAVING COUNT(*) >= 2;

.print
.print --- 5c. WHERE + GROUP BY + HAVING together ---
SELECT major, ROUND(AVG(gpa), 2) AS avg_gpa
FROM students
WHERE year >= 2              -- 1) drop freshmen
GROUP BY major               -- 2) group what's left
HAVING AVG(gpa) > 3.3;       -- 3) keep strong groups


-- ---------------------------------------------------------------------
-- 6. JOINS   (combine tables using matching keys)
-- ---------------------------------------------------------------------
.print
.print --- 6a. INNER JOIN: only rows that match in both ---
SELECT s.name, e.course_id, e.grade
FROM students AS s
JOIN enrollments AS e ON s.student_id = e.student_id
ORDER BY s.name;
-- Grace is missing (no enrollments)

.print
.print --- 6b. three-table join ---
SELECT s.name, c.title, c.units, e.grade
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses  c ON e.course_id  = c.course_id
ORDER BY s.name, c.title;

.print
.print --- 6c. LEFT JOIN: keep ALL rows from the left table ---
SELECT s.name, e.course_id
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
ORDER BY s.name;
-- Grace now shows up with NULL course

.print
.print --- 6d. LEFT JOIN + IS NULL = "things with no match" ---
SELECT c.course_id, c.title
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
WHERE e.course_id IS NULL;      -- courses nobody is taking

.print
.print --- 6e. join + group by: enrollment count per course ---
SELECT c.course_id, COUNT(e.student_id) AS enrolled
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id
ORDER BY enrolled DESC;

.print
.print --- 6f. total units per student ---
SELECT s.name, SUM(c.units) AS total_units
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c     ON e.course_id  = c.course_id
GROUP BY s.name
ORDER BY total_units DESC;


-- ---------------------------------------------------------------------
-- 7. CASE   (if/else inside a query)
-- ---------------------------------------------------------------------
.print
.print --- 7a. label students ---
SELECT name, gpa,
       CASE
           WHEN gpa >= 3.5 THEN 'Dean''s List'     -- '' = escaped quote
           WHEN gpa >= 3.0 THEN 'Good'
           WHEN gpa IS NULL THEN 'No GPA yet'
           ELSE 'Needs work'
       END AS standing
FROM students;

.print
.print --- 7b. count with CASE ---
SELECT major,
       SUM(CASE WHEN year >= 3 THEN 1 ELSE 0 END) AS upperclassmen
FROM students
GROUP BY major;


-- ---------------------------------------------------------------------
-- 8. SUBQUERIES + CTEs   (a query inside a query)
-- ---------------------------------------------------------------------
.print
.print --- 8a. students above the average gpa ---
SELECT name, gpa FROM students
WHERE gpa > (SELECT AVG(gpa) FROM students);

.print
.print --- 8b. students taking PSTAT10 (subquery with IN) ---
SELECT name FROM students
WHERE student_id IN (SELECT student_id FROM enrollments
                     WHERE course_id = 'PSTAT10');

.print
.print --- 8c. CTE (WITH): name a subquery, then use it ---
WITH course_avgs AS (
    SELECT course_id, AVG(grade) AS avg_grade
    FROM enrollments
    WHERE grade IS NOT NULL
    GROUP BY course_id
)
SELECT course_id, ROUND(avg_grade, 2) AS avg_grade
FROM course_avgs
WHERE avg_grade >= 3.0;


-- ---------------------------------------------------------------------
-- 9. CHANGING DATA:  INSERT  UPDATE  DELETE
--    ALWAYS write the WHERE first — UPDATE/DELETE without WHERE hits EVERY row.
-- ---------------------------------------------------------------------
.print
.print --- 9a. INSERT a new student ---
INSERT INTO students (student_id, name, major, year, gpa)
VALUES (9, 'Hank', 'Statistics', 4, 3.4);
SELECT * FROM students WHERE student_id = 9;

.print
.print --- 9b. UPDATE ---
UPDATE students SET gpa = 3.5 WHERE name = 'Hank';
SELECT name, gpa FROM students WHERE name = 'Hank';

.print
.print --- 9c. DELETE ---
DELETE FROM students WHERE name = 'Hank';
SELECT COUNT(*) AS students_left FROM students;

.print
.print --- 9d. ALTER TABLE: add a column ---
ALTER TABLE students ADD COLUMN email TEXT;
UPDATE students SET email = lower(name) || '@ucsb.edu';   -- || joins strings
SELECT name, email FROM students LIMIT 3;


-- ---------------------------------------------------------------------
-- 10. HANDY FUNCTIONS
-- ---------------------------------------------------------------------
.print
.print --- 10. string + number + null helpers ---
SELECT upper(name)              AS upper_name,
       length(name)             AS name_len,
       substr(major, 1, 4)      AS major_abbr,
       ROUND(gpa, 1)            AS gpa_1dp,
       COALESCE(gpa, 0)         AS gpa_or_zero    -- replace NULL
FROM students;


-- ---------------------------------------------------------------------
-- 11. WINDOW FUNCTIONS   (a bit ahead — common in internship interviews)
--     Like GROUP BY, but keeps every row.
-- ---------------------------------------------------------------------
.print
.print --- 11a. rank students by gpa within each major ---
SELECT name, major, gpa,
       RANK() OVER (PARTITION BY major ORDER BY gpa DESC) AS rank_in_major
FROM students
WHERE gpa IS NOT NULL;

.print
.print --- 11b. compare each student to their major average ---
SELECT name, major, gpa,
       ROUND(AVG(gpa) OVER (PARTITION BY major), 2) AS major_avg
FROM students;


-- =====================================================================
--  ORDER SQL RUNS A QUERY IN (not the order you write it!):
--    FROM/JOIN -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT
--  That's why you can't use a SELECT alias inside WHERE.
-- =====================================================================


-- =====================================================================
--  PRACTICE — try these yourself first! (run: sqlite3 school.db  then type)
-- =====================================================================
-- Q1. Names of all Statistics majors, sorted alphabetically.
-- Q2. How many students are in each year? (year + count)
-- Q3. The student with the lowest GPA (name + gpa).
-- Q4. All courses in the PSTAT department with 4+ units.
-- Q5. Each student's name and how many courses they're enrolled in,
--     INCLUDING students with 0 courses.
-- Q6. Average grade per course, only counting graded rows,
--     highest first, rounded to 2 decimals.
-- Q7. Names of students taking BOTH PSTAT10 and PSTAT120A.
-- Q8. Majors whose average GPA is below the overall average GPA.


-- =====================================================================
--  ANSWERS
-- =====================================================================
.print
.print === Q1 ===
SELECT name FROM students WHERE major = 'Statistics' ORDER BY name;

.print
.print === Q2 ===
SELECT year, COUNT(*) AS n FROM students GROUP BY year ORDER BY year;

.print
.print === Q3 ===
SELECT name, gpa FROM students
WHERE gpa IS NOT NULL
ORDER BY gpa ASC
LIMIT 1;

.print
.print === Q4 ===
SELECT * FROM courses WHERE dept = 'PSTAT' AND units >= 4;

.print
.print === Q5 ===
SELECT s.name, COUNT(e.course_id) AS num_courses   -- COUNT(col) gives 0 for NULLs
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id, s.name
ORDER BY num_courses DESC;

.print
.print === Q6 ===
SELECT course_id, ROUND(AVG(grade), 2) AS avg_grade
FROM enrollments
WHERE grade IS NOT NULL
GROUP BY course_id
ORDER BY avg_grade DESC;

.print
.print === Q7 ===
SELECT s.name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
WHERE e.course_id IN ('PSTAT10', 'PSTAT120A')
GROUP BY s.student_id, s.name
HAVING COUNT(DISTINCT e.course_id) = 2;

.print
.print === Q8 ===
SELECT major, ROUND(AVG(gpa), 2) AS avg_gpa
FROM students
GROUP BY major
HAVING AVG(gpa) < (SELECT AVG(gpa) FROM students);
