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