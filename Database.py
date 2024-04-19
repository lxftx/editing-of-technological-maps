import os
import sqlite3

from psycopg2 import Error
import psycopg2


class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect_database(self, *args,**kwargs):
        if os.path.exists('config/db_config.bin'):
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
                return [False, f"Ошибка при работе с PostgreSQL - {error}"]
        else:
            try:
                self.connection = sqlite3.connect(*args)
                self.cursor = self.connection.cursor()
                return [True, f"Вы подключены к - SQLite"]
            except (Exception, Error) as error:
                return [False, f"Ошибка при работе с PostgreSQL - {error}"]

    def disconnection_database(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Соединение с БД закрыто")
