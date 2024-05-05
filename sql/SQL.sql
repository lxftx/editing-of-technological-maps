DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'posts') THEN
        CREATE TYPE posts AS ENUM
        ('Волочильщик',
        'Технолог');
    END IF;
END $$;

CREATE TABLE users
(
	user_id int GENERATED ALWAYS AS IDENTITY (start with 1 INCREMENT BY 1) NOT NULL,
	first_name varchar(128) NOT NULL,
	last_name varchar(256) NOT  NULL,
	patronymic varchar(256),
	post posts,
	birthdate date,
	email varchar(256) NOT NULL,
	passwd text,
	code int,
	
	CONSTRAINT PK_users_user_id PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXISTS user_changes (
    change_id SERIAL PRIMARY KEY,
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

-- Создаем функцию для обновления таблицы user_changes
CREATE OR REPLACE FUNCTION update_user_changes()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO user_changes (user_id, first_name_old, last_name_old, patronymic_old, first_name_new, last_name_new, patronymic_new)
    VALUES (OLD.user_id, OLD.first_name, OLD.last_name, OLD.patronymic, NEW.first_name, NEW.last_name, NEW.patronymic);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Создаем триггер для отслеживания изменений в таблице users
CREATE TRIGGER user_changes_trigger
AFTER UPDATE OF first_name, last_name, patronymic ON users
FOR EACH ROW
EXECUTE FUNCTION update_user_changes();