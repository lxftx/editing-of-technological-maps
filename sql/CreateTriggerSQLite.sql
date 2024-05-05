-- Создаем триггер для отслеживания изменений в таблице users
CREATE TRIGGER IF NOT EXISTS user_changes_trigger AFTER UPDATE OF first_name, last_name, patronymic ON users
BEGIN
    INSERT INTO user_changes (user_id, first_name_old, last_name_old, patronymic_old, first_name_new, last_name_new, patronymic_new)
    VALUES (OLD.user_id, OLD.first_name, OLD.last_name, OLD.patronymic, NEW.first_name, NEW.last_name, NEW.patronymic);
END;
