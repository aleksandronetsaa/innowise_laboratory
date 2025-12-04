-- Включаем поддержку внешних ключей для SQLite
PRAGMA foreign_keys = ON;

-- ---------------------------
-- Создание таблицы students
-- ---------------------------
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_year INTEGER
);

-- ---------------------------
-- Создание таблицы grades
-- ---------------------------
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER NOT NULL CHECK(grade BETWEEN 1 AND 100),
    FOREIGN KEY (student_id) REFERENCES students(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

---
# Блок вставки тестовых данных — обёрнут в транзакцию
BEGIN TRANSACTION;

INSERT INTO students (full_name, birth_year) VALUES 
    ('Alice Johnson', 2005),
    ('Brian Smith', 2004),
    ('Carla Reyes', 2006),
    ('Daniel Kim', 2005),
    ('Eva Thompson', 2003),
    ('Felix Nguyen', 2007),
    ('Grace Patel', 2005),
    ('Henry Lopez', 2004),
    ('Isabella Martinez', 2006);

INSERT INTO grades (student_id, subject, grade) VALUES 
    (1, 'Math', 88), (1, 'English', 92), (1, 'Science', 85),
    (2, 'Math', 75), (2, 'History', 83), (2, 'English', 79),
    (3, 'Science', 95), (3, 'Math', 91), (3, 'Art', 89),
    (4, 'Math', 84), (4, 'Science', 88), (4, 'Physical Education', 93),
    (5, 'English', 90), (5, 'History', 85), (5, 'Math', 88),
    (6, 'Science', 72), (6, 'Math', 78), (6, 'English', 81),
    (7, 'Art', 94), (7, 'Science', 87), (7, 'Math', 90),
    (8, 'History', 77), (8, 'Math', 83), (8, 'Science', 80),
    (9, 'English', 96), (9, 'Math', 89), (9, 'Art', 92);

COMMIT;

---
-- Создание индексов для оптимизации (можно выполнять ДО запросов)
CREATE INDEX IF NOT EXISTS idx_students_full_name ON students(full_name);
CREATE INDEX IF NOT EXISTS idx_grades_student_id ON grades(student_id);
CREATE INDEX IF NOT EXISTS idx_students_birth_year ON students(birth_year);
CREATE INDEX IF NOT EXISTS idx_grades_grade ON grades(grade);
CREATE INDEX IF NOT EXISTS idx_grades_subject ON grades(subject);

---
-- SQL-ЗАПРОСЫ (домашнее задание)
-- 1) Создать таблицы — выполнено выше.
-- 2) Вставить данные — выполнено выше.
-- 3) Найти все оценки для конкретного студента (Alice Johnson)
-- Пример:
SELECT g.subject, g.grade 
FROM grades g
JOIN students s ON g.student_id = s.id
WHERE s.full_name = 'Alice Johnson'
ORDER BY g.grade;

-- 4) Рассчитать средний балл по каждому студенту
SELECT s.full_name, ROUND(AVG(g.grade), 2) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.full_name
ORDER BY avg_grade DESC;

-- 5) Список всех студентов, родившихся после 2004
SELECT full_name, birth_year 
FROM students 
WHERE birth_year > 2004;

-- 6) Запрос, который перечисляет все предметы и их средний балл
SELECT subject, ROUND(AVG(grade), 2) AS avg_grade 
FROM grades 
GROUP BY subject 
ORDER BY avg_grade_DESC;

-- 7) Топ-3 студента с наивысшим средним баллом
SELECT s.full_name, ROUND(AVG(g.grade), 2) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.full_name
ORDER BY avg_grade DESC 
LIMIT 3;

-- 8) Показать всех студентов, которые набрали более 80 в любом предмете
SELECT DISTINCT s.full_name
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade > 80
ORDER BY s.full_name;
