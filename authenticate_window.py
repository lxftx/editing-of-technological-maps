# -*- coding: utf-8 -*-
import os
import sqlite3

from cryptography.fernet import Fernet

from Database import *
from hash_passwd import *
from re_password import *
from main import Main


class User:
    def __init__(self, item):
        self.id = item[0]
        self.name = item[1]
        self.surname = item[2]
        self.patronic = item[3]
        self.posts = item[4]
        self.birthday = item[5]
        self.email = item[6]
        self.password = item[7]
        self.code = item[8]

    def update(self, item):
        self.__init__(item)


class Authenticate(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setFixedSize(641, 674)
        self.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.container = QtWidgets.QLabel(self.centralwidget)
        self.container.setGeometry(QtCore.QRect(30, 30, 581, 621))

        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setUnderline(True)
        self.container.setFont(font)
        self.container.setStyleSheet("background-color: #fff; border-radius: 30px;")
        self.container.setText("")
        self.container.setObjectName("container")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(40, 80, 561, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setStyleSheet("background-color: #fff;")
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.email = QtWidgets.QLabel(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(50, 180, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.email.setFont(font)
        self.email.setStyleSheet("background-color: #fff;\n"
                                 "padding: 0 10px;")
        self.email.setObjectName("email")
        self.email_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.email_edit.setGeometry(QtCore.QRect(50, 230, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(15)
        self.email_edit.setFont(font)
        self.email_edit.setStyleSheet("background-color: #fff;\n"
                                      "border: 2px solid black;\n"
                                      "border-radius: 10px;\n"
                                      "padding: 0 10px;\n"
                                      "")
        self.email_edit.setText("")
        self.email_edit.setObjectName("email_edit")
        self.email_edit.textChanged.connect(self.change_text)
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(50, 300, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color: #fff;\n"
                                    "padding: 0 10px;")
        self.password.setObjectName("password")
        self.password_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_edit.setGeometry(QtCore.QRect(50, 350, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(15)
        self.password_edit.setFont(font)
        self.password_edit.setStyleSheet("background-color: #fff;\n"
                                         "border: 2px solid black;\n"
                                         "border-radius: 10px;\n"
                                         "padding: 0 10px;\n"
                                         "")
        self.password_edit.setText("")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_edit.setObjectName("password_edit")
        self.password_edit.textChanged.connect(self.change_text)
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(100, 470, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        self.button.setFont(font)
        self.button.setStyleSheet("QPushButton#button {\n"
                                  "    background-color: black; \n"
                                  "    color: white;\n"
                                  "    border-radius: 10px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#button:hover {\n"
                                  "    background-color: #474744;\n"
                                  "}"
                                  )
        self.button.setObjectName("button")
        self.button.clicked.connect(self.authenticate if os.path.exists('config/db_config.bin') else self.auth_sqlite)
        self.view_password = QtWidgets.QRadioButton(self.centralwidget)
        self.view_password.setGeometry(QtCore.QRect(60, 400, 511, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.view_password.setFont(font)
        self.view_password.setStyleSheet("background-color: #fff;\n"
                                         "padding: 0 10px;")
        self.view_password.setIconSize(QtCore.QSize(16, 16))
        self.view_password.setObjectName("view_password")
        self.view_password.clicked.connect(self.open_password)
        self.reset_password = QtWidgets.QPushButton(self.centralwidget)
        self.reset_password.setGeometry(QtCore.QRect(250, 530, 141, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setUnderline(True)
        self.reset_password.setFont(font)
        self.reset_password.setStyleSheet("background-color: #fff; border: none;")
        self.reset_password.setObjectName("reset_password")
        self.reset_password.clicked.connect(self.window_reset_pswd)

        self.feedback = QtWidgets.QLabel(self.centralwidget)
        self.feedback.setGeometry(QtCore.QRect(40, 582, 551, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.feedback.setFont(font)
        self.feedback.setStyleSheet("background-color: #fff;\n"
                                    "padding: 0 10px; color: red;")
        self.feedback.setText("")
        self.feedback.setObjectName("feedback")

        self.view_password.installEventFilter(self)
        self.button.installEventFilter(self)
        self.reset_password.installEventFilter(self)

        if not os.path.exists('sql/example.db') and not os.path.exists('config/path_sqlite.bin'):
            self.create_table_sqlite()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle("MainWindow")
        self.header.setText("Авторизация")
        self.email.setText("Email пользователя:")
        self.email_edit.setPlaceholderText("example@<domain>.[ru/com]")
        self.password.setText("Пароль")
        self.button.setText("Войти")
        self.view_password.setText("Посмотреть пароль")
        self.reset_password.setText("Забыли пароль?")

    def read_file(self):
        with open('config/db_config.bin', 'rb') as file:
            lines = file.readlines()
            key = lines[0].strip()
            enc_name_user_db = lines[1].strip()
            enc_passwd_db = lines[2].strip()
            enc_host_db = lines[3].strip()
            enc_port_db = lines[4].strip()
            enc_name_db = lines[5].strip()
        fernet = Fernet(key)
        return [fernet.decrypt(enc_name_user_db).decode(),
                fernet.decrypt(enc_passwd_db).decode(),
                fernet.decrypt(enc_host_db).decode(),
                fernet.decrypt(enc_port_db).decode(),
                fernet.decrypt(enc_name_db).decode()]

    def read_path_sqlite(self):
        if os.path.exists('config/path_sqlite.bin'):
            with open('config/path_sqlite.bin', 'rb') as file:
                lines = file.readlines()
                key = lines[0].strip()
                enc_path_sqllite = lines[1]
            fernet = Fernet(key)
            dec_path_sqllite = fernet.decrypt(enc_path_sqllite).decode()
            return dec_path_sqllite
        else:
            return False

    def open_password(self, event):
        if event:
            self.password_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.password_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def create_table_sqlite(self):
        self.db.connect_database('sql/example.db')
        with open('sql/SQLite.sql', 'r') as sql_file:
            sql_commands = sql_file.read().split(';')
            for command in sql_commands:
                if command.strip():
                    self.db.cursor.execute(command)
        self.db.connection.commit()

    def auth_sqlite(self):
        try:
            if not self.password_edit.text():
                path = self.read_path_sqlite()
                answer = self.db.connect_database(path) if path else self.db.connect_database('sql/example.db')
                if answer[0]:
                    self.db.cursor.execute("""SELECT * FROM users WHERE email = ?""",
                                           (self.email_edit.text(),))
                    select = self.db.cursor.fetchone()
                    post = None if select is None else select[4]
                    if post is not None and post != "Технолог":
                        user = User(select)
                        self.main_window = Main(self.db, user, authentication)
                        self.main_window.show()
                        # self.hide()
                        self.close()
                        self.email_edit.clear()
                        self.password_edit.clear()
                    else:
                        self.feedback.setText("Неверный Email или пароль")
                        self.email_edit.setStyleSheet(
                            """background-color: #fff; border: 2px solid red; border-radius: 10px; padding: 0 10px;\n""")
                        self.password_edit.setStyleSheet(
                            """background-color: #fff; border: 2px solid red; border-radius: 10px; padding: 0 10px;\n""")
                else:
                    self.feedback.setText(answer[1])
            else:
                path = self.read_path_sqlite()
                answer = self.db.connect_database(path) if path else self.db.connect_database('sql/example.db')
                if answer[0]:
                    self.db.cursor.execute("""SELECT COUNT(*) FROM users""")
                    select = self.db.cursor.fetchone()[0]
                    if int(select):
                        self.db.cursor.execute("""SELECT * FROM users WHERE email = ? and passwd = ?""",
                                               (self.email_edit.text(), hash_password(self.password_edit.text())))
                        select = self.db.cursor.fetchone()
                        print(select)
                        if select:
                            user = User(select)
                            self.main_window = Main(self.db, user, authentication)
                            self.main_window.show()
                            self.hide()
                            self.email_edit.clear()
                            self.password_edit.clear()
                        else:
                            self.feedback.setText("Неверный Email или пароль")
                    else:
                        self.db.cursor.execute("""INSERT INTO users (first_name, last_name, patronymic, post, birthdate, email, passwd, code) 
                                                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", ('Admin', 'Admin', '', 'Технолог', datetime.datetime.now().strftime('%Y-%m-%d'), self.email_edit.text(), hash_passwd.hash_password(self.password_edit.text()), 0))
                        self.db.connection.commit()
                        self.db.cursor.execute("""SELECT * FROM users WHERE email = ? and passwd = ?""",
                                               (self.email_edit.text(), hash_password(self.password_edit.text())))
                        select = self.db.cursor.fetchone()
                        if select:
                            user = User(select)
                            self.main_window = Main(self.db, user, authentication)
                            self.main_window.show()
                            self.hide()
                            self.email_edit.clear()
                            self.password_edit.clear()
                else:
                    self.feedback.setText(answer[1])
        except Exception as ex:
            print(ex)

    def authenticate(self):
        read = self.read_file()
        if not self.password_edit.text():
            answer = self.db.connect_database(user=read[0], password=read[1], host=read[2], port=read[3],
                                              database=read[4])
            if answer[0]:
                self.db.cursor.execute("""SELECT * FROM users WHERE email = %s""",
                                       (self.email_edit.text(),))
                select = self.db.cursor.fetchone()
                post = None if select is None else select[4]
                if post is not None and post != "Технолог":
                    user = User(select)
                    self.main_window = Main(self.db, user, authentication)
                    self.main_window.show()
                    # self.hide()
                    self.close()
                    self.email_edit.clear()
                    self.password_edit.clear()
                else:
                    self.feedback.setText("Неверный Email или пароль")
                    self.email_edit.setStyleSheet(
                        """background-color: #fff; border: 2px solid red; border-radius: 10px; padding: 0 10px;\n""")
                    self.password_edit.setStyleSheet(
                        """background-color: #fff; border: 2px solid red; border-radius: 10px; padding: 0 10px;\n""")
            else:
                self.feedback.setText(answer[1])
        else:
            answer = self.db.connect_database(user=read[0], password=read[1], host=read[2], port=read[3],
                                              database=read[4])
            self.db.cursor.execute("""SELECT COUNT(*) FROM users""")
            select = self.db.cursor.fetchone()[0]
            if answer[0]:
                if int(select):
                    self.db.cursor.execute("""SELECT * FROM users WHERE email = %s and passwd = %s""",
                                           (self.email_edit.text(), hash_password(self.password_edit.text())))
                    select = self.db.cursor.fetchone()
                    if select:
                        user = User(select)
                        self.main_window = Main(self.db, user, authentication)
                        self.main_window.show()
                        self.hide()
                        self.email_edit.clear()
                        self.password_edit.clear()
                    else:
                        self.feedback.setText("Неверный Email или пароль")
                else:
                    postgres_insert_query = """INSERT INTO users (first_name, last_name, patronymic, post, birthdate, email, passwd, code) 
                                                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                    record_to_insert = ('Admin', 'Admin',
                                        '',
                                        'Технолог',
                                        datetime.date(2000, 1, 1), self.email_edit.text(),
                                        hash_passwd.hash_password(self.password_edit.text()), 0)
                    self.db.cursor.execute(postgres_insert_query, record_to_insert)
                    self.db.connection.commit()
                    self.db.cursor.execute("""SELECT * FROM users WHERE email = %s and passwd = %s""",
                                           (self.email_edit.text(), hash_password(self.password_edit.text())))
                    select = self.db.cursor.fetchone()
                    if select:
                        user = User(select)
                        self.main_window = Main(self.db, user, authentication)
                        self.main_window.show()
                        self.hide()
                        self.email_edit.clear()
                        self.password_edit.clear()
            else:
                self.feedback.setText(answer[1])

    def change_text(self):
        self.email_edit.setStyleSheet(
            """background-color: #fff; border: 2px solid black; border-radius: 10px; padding: 0 10px;\n""")
        self.password_edit.setStyleSheet(
            """background-color: #fff; border: 2px solid black; border-radius: 10px; padding: 0 10px;\n""")
        self.feedback.clear()

    def eventFilter(self, watched, event):
        if event.type() == QtCore.QEvent.Enter and watched == self.reset_password:
            self.reset_password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        elif event.type() == QtCore.QEvent.Enter and watched == self.button:
            self.button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        return super().eventFilter(watched, event)

    def window_reset_pswd(self):
        if os.path.exists('config/email.bin'):
            with open('config/email.bin', 'rb') as file:
                lines = file.readlines()
                key = lines[0].strip()
                encEmail = lines[1].strip()
                encpaswd = lines[2].strip()
                fernet = Fernet(key)
                dec_email = fernet.decrypt(encEmail).decode()
                dec_paswd = fernet.decrypt(encpaswd).decode()
                if dec_email.strip() and dec_paswd.strip():
                    read = self.read_file()
                    answer = self.db.connect_database(user=read[0], password=read[1], host=read[2], port=read[3],
                                                      database=read[4])
                    if answer[0]:
                        self.reset_password_ui = ResetPassword(self.db, authentication, dec_email, dec_paswd)
                        self.reset_password_ui.show()
                        self.hide()
                    else:
                        self.feedback.setText(answer[1])
                else:
                    self.feedback.setText("Корпоративная почта или пароль не имеют данных,\nПерейдите в настройки и установите их!")
        else:
            self.feedback.setText("Установите в настройках корпоративную почту,\nдля восстановлении учетной записи!")

    def closeEvent(self, event):
        self.db.disconnection_database()
        event.accept()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    authentication = Authenticate()
    authentication.show()
    sys.exit(app.exec_())
