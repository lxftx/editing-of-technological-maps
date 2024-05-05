-- Создаем тип ENUM posts, если он не существует
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    post_value TEXT UNIQUE
);

-- Вставляем значения в таблицу posts
INSERT INTO posts (post_value) VALUES
    ('Волочильщик'),
    ('Технолог')
ON CONFLICT (post_value) DO NOTHING;

-- Создаем таблицу users
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    patronymic TEXT,
    post INTEGER,
    birthdate DATE,
    email TEXT NOT NULL,
    passwd TEXT,
    code INTEGER,
    FOREIGN KEY (post) REFERENCES posts(id)
);

-- Создаем таблицу для отслеживания изменений имен, фамилий и отчеств пользователей
CREATE TABLE IF NOT EXISTS user_changes (
    change_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    first_name_old TEXT,
    last_name_old TEXT,
    patronymic_old TEXT,
    first_name_new TEXT,
    last_name_new TEXT,
    patronymic_new TEXT,
    change_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
