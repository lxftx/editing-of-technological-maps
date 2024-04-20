import os
import sqlite3

from psycopg2 import Error
import psycopg2


class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect_database(self, db, *args,**kwargs):
        # if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config', 'db_config.bin')):
        if db == "postgres":
            try:
                # Подключение к существующей базе данных
                self.connection = psycopg2.connect(**kwargs)

                # Курсор для выполнения операций с базой данных
                self.cursor = self.connection.cursor()
                # Получить результат
                self.cursor.execute("SELECT version();")
                record = self.cursor.fetchone()
                print("Вы подключены к - ", record, "\n")
                return [True, f"Вы подключены к - {record}"]
            except (Exception, Error) as error:
                error_message = str(error)
                if len(error_message) > 50:
                    chunks = [error_message[i:i + 50] for i in range(0, len(error_message), 50)]
                    formatted_error_message = '\n'.join(chunks)
                    return [False, f"Ошибка при работе с PostgreSQL - \n{formatted_error_message}"]
                else:
                    return [False, f"Ошибка при работе с PostgreSQL - {error_message}"]
        else:
            try:
                self.connection = sqlite3.connect(*args)
                self.cursor = self.connection.cursor()
                return [True, f"Вы подключены к - SQLite"]
            except (Exception, Error) as error:
                error_message = str(error)
                if len(error_message) > 50:
                    chunks = [error_message[i:i + 50] for i in range(0, len(error_message), 50)]
                    formatted_error_message = '\n'.join(chunks)
                    return [False, f"Ошибка при работе с SQLite - \n{formatted_error_message}"]
                else:
                    return [False, f"Ошибка при работе с SQLite - {error_message}"]

    def disconnection_database(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Соединение с БД закрыто")
