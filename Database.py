from psycopg2 import Error
import psycopg2


class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect_database(self, **kwargs):
        try:
            # Подключение к существующей базе данных
            self.connection = psycopg2.connect(**kwargs)

            # Курсор для выполнения операций с базой данных
            self.cursor = self.connection.cursor()
            # Получить результат
            self.cursor.execute("SELECT version();")
            record = self.cursor.fetchone()
            print("Вы подключены к - ", record, "\n")
            return True
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    def disconnection_database(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Соединение с PostgreSQL закрыто")
