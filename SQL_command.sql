-- ============================================================
-- FCIS Ain Shams University – Hall 1 Schedule
-- All times use Normal (non-Ramadan) 24-hour format:
--   Slot 1: 08:00-10:00  Slot 2: 10:00-12:00  Slot 3: 12:00-14:00
--   Slot 4: 14:00-16:00  Slot 5: 16:00-18:00  Slot 6: 18:00-20:00
-- Columns: level | day | course | instructor | start_time | end_time 
-- ============================================================

DROP TABLE IF EXISTS schedule;

CREATE TABLE schedule (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    level       TEXT,
    day         TEXT,    -- Saturday … Thursday
    course      TEXT,
    instructor  TEXT,
    start_time  TEXT,    -- HH:MM 24-hour normal timing
    end_time    TEXT
);

-- ── INSERT DATA ────────────────────────────────────────────

-- ─────────────────────────────────────────
-- Level: CS4 + IS4
-- ────────────────────────────────────────
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('CS4 / IS4', 'Tuesday', 'Software Quality Assurance',  'Prof. Rania El-Gohary / Dr. Yasmin Afify', '16:00', '18:00');

-- ────────────────────────────────────────────────────────
-- Level: SC4 + CS3
-- ────────────────────────────────────────────────────────
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('SC4 / CS3', 'Thursday', 'Natural Language Processing',  'Dr. Sally Saad', '16:00', '18:00');

-- ────────────────────────────────────────────────────────
-- Level: SC4 + IS3
-- ────────────────────────────────────────────────────────
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('SC4 / IS3', 'Thursday', 'Computer and Network Security / Data Security',  'Dr. Shimaa Abo Alian', '12:00', '14:00');

-- ────────────────────────────────────────────────────────
-- Level: SC3 + CSys3 + IS3
-- ────────────────────────────────────────────────────────
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('SC3 / CSys3 / IS3', 'Monday', 'High Performance Computing',  'Dr. Heba Kalied', '08:00', '10:00');

-- ────────────────────────────────────────────────────────
-- Level: CS3 + SC3
-- ────────────────────────────────────────────────────────
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('CS3 / SC3', 'Wednesday', 'Computer Graphics',  'Dr. Salsabeel Amin / Dr. Mahmoud Zeidan', '12:00', '14:00');

-- ────────────────────────────────────────────────────────
-- Level: CS3 + IS3
-- ────────────────────────────────────────────────────────
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('CS3 / IS3', 'Saturday', 'Analysis & Design of Algorithms', 'Dr. Ahmed Salah / Dr. Soha Nabil', '14:00', '16:00');
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('CS3 / IS3', 'Thursday', 'Software Engineering',  'Dr. Hoda Amin / Dr. Fatma Mohamed', '10:00', '12:00');

-- ────────────────────────────────────────────────────────
-- Level: SC3 + CS3
-- ────────────────────────────────────────────────────────
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('SC3 / CS3', 'Thursday', 'Machine Learning / Pattern Recognition',  'Dr. Dina Khattab', '14:00', '16:00');

-- ─────────────────────────────────────────
-- Level: 2
-- ────────────────────────────────────────
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('2G1', 'Sunday', 'Artificial Intelligence',  'Dr. Dina El-Sayad / Dr. Ghada Hamed', '08:00', '10:00');
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('2G1', 'Sunday', 'Computer Organization & Architecture',  'Dr. Hanan Ahmed / Dr. Randa Mohamed', '10:00', '12:00');
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('2G1', 'Tuesday', 'Linear Algebra',  'Dr. Esraa Abd El-Raouf', '12:00', '14:00');
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('2G1', 'Tuesday', 'Data Structures',  'Dr. Wedad Hussein / Dr. Hanan Yosry', '14:00', '16:00');
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('2G1', 'Wednesday', 'Operations Research', 'Prof. Safaa Amin / Dr. Doaa Ezzat / Dr. Doaa Mahmoud', '10:00', '12:00');

INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('2G2', 'Saturday', 'Computer. Organization & Architecture',  'Dr. Hanan Ahmed / Dr. Randa Mohamed', '12:00', '14:00');
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('2G2', 'Sunday', 'Data Structures',  'Dr. Wedad Hussein / Dr. Hanan Yosry', '18:00', '20:00');
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('2G2', 'Tuesday', 'Artificial Intelligence',  'Dr. Dina El-Sayad / Dr. Ghada Hamed', '08:00', '10:00');
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('2G2', 'Tuesday', 'Operations Research', 'Prof. Safaa Amin / Dr. Doaa Ezzat / Dr. Doaa Mahmoud', '10:00', '12:00');
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('2G2', 'Thursday', 'Linear Algebra',  'Dr. Esraa Abd El-Raouf', '08:00', '10:00');

-- ────────────────────────────────────────
-- Level: 1
-- ───────────────────────────────────────
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('1G1', 'Saturday', 'Electronics', 'Dr. Mirfat El-Qat / Dr. Hafez Salim', '10:00', '12:00');
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('1G1', 'Sunday', 'Structured Programming', 'Dr. Mariam Nabil / Dr. Salsabeel Amin / Dr. Naglaa Fathy / Dr. Ghada Hamed', '12:00', '14:00');
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('1G1', 'Sunday', 'Physics II', 'Prof. Hassan Ramadan / Dr. Mahmoud Monir / Dr. Amr Mahmoud', '14:00', '16:00');
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('1G1', 'Monday', 'Calculus II', 'Dr. Suad Bakri / Dr. Salsabeel Mohamed', '16:00', '18:00');

INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('1G2', 'Saturday', 'Electronics', 'Dr. Mirfat El-Qat / Dr. Hafez Salim', '08:00', '10:00');
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('1G2', 'Monday', 'Structured Programming', 'Dr. Mariam Nabil / Dr. Salsabeel Amin / Dr. Naglaa Fathy / Dr. Ghada Hamed', '10:00', '12:00');
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('1G2', 'Wednesday', 'Physics II', 'Prof. Hassan Ramadan / Dr. Mahmoud Monir / Dr. Amr Mahmoud', '16:00', '18:00');
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('1G2', 'Wednesday', 'Calculus II', 'Dr. Suad Bakri / Dr. Salsabeel Mohamed', '18:00', '20:00');

INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('1G3', 'Saturday',  'Physics II', 'Prof. Hassan Ramadan / Dr. Mahmoud Monir / Dr. Amr Mahmoud','16:00', '18:00');
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('1G3', 'Monday', 'Structured Programming', 'Dr. Mariam Nabil / Dr. Salsabeel Amin / Dr. Naglaa Fathy / Dr. Ghada Hamed', '12:00', '14:00');
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('1G3', 'Monday', 'Calculus II', 'Dr. Suad Bakri / Dr. Salsabeel Mohamed', '14:00', '16:00');
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('1G3', 'Wednesday', 'Electronics', 'Dr. Mirfat El-Qat / Dr. Hafez Salim', '08:00', '10:00');



INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('CS4 / IS4', 'Wednesday', 'Software',  'Prof. Rania El-Gohary / Dr. Yasmin Afify', '21:00', '22:00');
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('CS4 / IS4', 'Wednesday', 'Math',  'Prof. Rania El-Gohary / Dr. Yasmin Afify', '22:00', '23:00');
INSERT INTO schedule (level, day, course, instructor, start_time, end_time) VALUES ('CS4 / IS4', 'Wednesday', 'Math',  'Prof. Rania El-Gohary / Dr. Yasmin Afify', '23:00', '00:00');
-- ── USEFUL QUERIES ───────────────────────────────────────
-- 1. Full timetable for one level, ordered chronologically
-- SELECT day, start_time, end_time, course, instructor
-- FROM   schedule WHERE level = '1G3'
-- ORDER  BY CASE day WHEN 'Saturday' THEN 1 WHEN 'Sunday' THEN 2
--            WHEN 'Monday' THEN 3 WHEN 'Tuesday' THEN 4
--            WHEN 'Wednesday' THEN 5 WHEN 'Thursday' THEN 6 END, start_time;

-- 2. All sessions for a specific instructor
-- SELECT level, day, start_time, end_time, course
-- FROM   schedule WHERE instructor LIKE '%Dr. Esraa Abd El-Raouf%';

-- 3. Everything on a given day across all levels
-- SELECT level, start_time, end_time, course,  instructor
-- FROM   schedule WHERE day = 'Monday' ORDER BY level, start_time;

-- 4. All labs for a specific course
-- SELECT level, day, start_time, end_time, instructor
-- FROM   schedule WHERE course LIKE '%Artificial Intelligence%';

-- 5. Session count per course per level
-- SELECT level, course,  COUNT(*) AS sessions
-- FROM   schedule GROUP BY level, course ORDER BY level, course;