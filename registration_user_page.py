import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from alert import AlertMessage

import hash_passwd
import re


class RegistrationUserPage(QWidget, AlertMessage):
    def __init__(self, db, main):
        super().__init__()

        self.add_user_page = self
        self.db = db
        self.main = main

        self.content_registration = QtWidgets.QLabel(self.add_user_page)
        self.content_registration.setGeometry(QtCore.QRect(10, 10, 1021, 861))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.content_registration.setFont(font)
        self.content_registration.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                                "border-radius: 30px;\n"
                                                "color: rgb(255, 255, 17);")
        self.content_registration.setText("")
        self.content_registration.setObjectName("content_registration")

        self.name_label = QtWidgets.QLabel(self.add_user_page)
        self.name_label.setGeometry(QtCore.QRect(60, 40, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                      " padding-left: 5px;")
        self.name_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.name_label.setObjectName("name_registration_label")
        self.name_label.setText("Имя")

        self.name_edit = QtWidgets.QLineEdit(self.add_user_page)
        self.name_edit.setGeometry(QtCore.QRect(60, 80, 201, 41))
        self.name_edit.setStyleSheet("background-color: #fff;\n"
                                     "border-radius: 10px; \n"
                                     "padding-left: 5px;\n"
                                     "font-size: 15px;\n"
                                     "")
        self.name_edit.setText("")
        self.name_edit.setObjectName("name_registration_edit")
        self.name_edit.setPlaceholderText('Обязательное поле')
        self.name_edit.textChanged.connect(self.reset_name)

        self.surname_label = QtWidgets.QLabel(self.add_user_page)
        self.surname_label.setGeometry(QtCore.QRect(360, 40, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.surname_label.setFont(font)
        self.surname_label.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                         " padding-left: 5px;")
        self.surname_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.surname_label.setObjectName("surname_registration_label")
        self.surname_label.setText("Фамилия")

        self.surname_edit = QtWidgets.QLineEdit(self.add_user_page)
        self.surname_edit.setGeometry(QtCore.QRect(360, 80, 281, 41))
        self.surname_edit.setStyleSheet("background-color: #fff;\n"
                                        "border-radius: 10px; \n"
                                        "padding-left: 5px;\n"
                                        "font-size: 15px;\n"
                                        "")
        self.surname_edit.setText("")
        self.surname_edit.setObjectName("surname_registration_edit")
        self.surname_edit.setPlaceholderText('Обязательное поле')
        self.surname_edit.textChanged.connect(self.reset_surname)

        self.patronic_label = QtWidgets.QLabel(self.add_user_page)
        self.patronic_label.setGeometry(QtCore.QRect(710, 40, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.patronic_label.setFont(font)
        self.patronic_label.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                          " padding-left: 5px;")
        self.patronic_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.patronic_label.setObjectName("patronic_registration_label")
        self.patronic_label.setText("Отчество")

        self.patronic_edit = QtWidgets.QLineEdit(self.add_user_page)
        self.patronic_edit.setGeometry(QtCore.QRect(710, 80, 291, 41))
        self.patronic_edit.setStyleSheet("background-color: #fff;\n"
                                         "border-radius: 10px; \n"
                                         "padding-left: 5px;\n"
                                         "font-size: 15px;\n"
                                         "")
        self.patronic_edit.setText("")
        self.patronic_edit.setObjectName("patronic_registration_edit")

        self.email_label = QtWidgets.QLabel(self.add_user_page)
        self.email_label.setGeometry(QtCore.QRect(230, 140, 611, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                       " padding-left: 5px;")
        self.email_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.email_label.setObjectName("email_registration_label")
        self.email_label.setText("Email")

        self.email_edit = QtWidgets.QLineEdit(self.add_user_page)
        self.email_edit.setGeometry(QtCore.QRect(230, 180, 611, 51))
        self.email_edit.setStyleSheet("background-color: #fff;\n"
                                      "border-radius: 10px; \n"
                                      "padding-left: 5px;\n"
                                      "font-size: 15px;\n"
                                      "")
        self.email_edit.setText("")
        self.email_edit.setObjectName("email_registration_edit")
        self.email_edit.setPlaceholderText('Обязательное поле')
        self.email_edit.textChanged.connect(self.reset_email)

        self.birthday_label = QtWidgets.QLabel(self.add_user_page)
        self.birthday_label.setGeometry(QtCore.QRect(70, 280, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.birthday_label.setFont(font)
        self.birthday_label.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                          " padding-left: 5px;")
        self.birthday_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.birthday_label.setObjectName("birthday_registration_label")
        self.birthday_label.setText("Дата рождения")

        self.birthday_edit = QtWidgets.QDateEdit(self.add_user_page)
        self.birthday_edit.setGeometry(QtCore.QRect(70, 320, 350, 41))
        self.birthday_edit.setStyleSheet("background-color: #fff;\n"
                                         "color: black;\n"
                                         "border-radius: 10px; \n"
                                         "padding-left: 5px;\n"
                                         "font-size: 15px;")
        self.birthday_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.birthday_edit.setCalendarPopup(True)
        self.birthday_edit.setObjectName("birthday_registration_edit")

        self.post_label = QtWidgets.QLabel(self.add_user_page)
        self.post_label.setGeometry(QtCore.QRect(600, 280, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.post_label.setFont(font)
        self.post_label.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                      " padding-left: 5px;")
        self.post_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.post_label.setObjectName("post_registration_label")
        self.post_label.setText("Пользователь")

        self.posts_edit = QtWidgets.QComboBox(self.add_user_page)
        self.posts_edit.setGeometry(QtCore.QRect(600, 320, 350, 41))
        self.posts_edit.setStyleSheet("background-color: #fff;\n"
                                      "border-radius: 10px; \n"
                                      "padding-left: 5px;\n"
                                      "font-size: 15px;\n"
                                      "")
        self.posts_edit.setObjectName("posts_registration_edit")
        if os.path.exists('config/db_config.bin'):
            self.db.cursor.execute("""SELECT unnest(enum_range(NULL::posts)) AS post_value""")
        else:
            self.db.cursor.execute("""SELECT name FROM posts""")
        select = [x[0] for x in self.db.cursor.fetchall()]
        self.posts_edit.addItems(select)
        self.posts_edit.currentTextChanged.connect(self.reset_posts)


        self.password_label = QtWidgets.QLabel(self.add_user_page)
        self.password_label.setGeometry(QtCore.QRect(40, 410, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                          " padding-left: 5px;")
        self.password_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.password_label.setObjectName("password_registration_label")
        self.password_label.setText("Пароль")

        self.password_edit = QtWidgets.QLineEdit(self.add_user_page)
        self.password_edit.setGeometry(QtCore.QRect(40, 450, 401, 41))
        self.password_edit.setStyleSheet("background-color: #fff;\n"
                                         "border-radius: 10px; \n"
                                         "padding-left: 5px;\n"
                                         "font-size: 15px;\n"
                                         "")
        self.password_edit.setText("")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_edit.setObjectName("password_registration_edit")
        self.password_edit.textChanged.connect(self.equal_passwd)

        self.confirm_password_label = QtWidgets.QLabel(self.add_user_page)
        self.confirm_password_label.setGeometry(QtCore.QRect(600, 410, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.confirm_password_label.setFont(font)
        self.confirm_password_label.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                                  " padding-left: 5px;")
        self.confirm_password_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.confirm_password_label.setObjectName("confirm_password_registration_label")
        self.confirm_password_label.setText("Повторите пароль")

        self.confirm_password_edit = QtWidgets.QLineEdit(self.add_user_page)
        self.confirm_password_edit.setGeometry(QtCore.QRect(600, 450, 401, 41))
        self.confirm_password_edit.setStyleSheet("background-color: #fff;\n"
                                                 "border-radius: 10px; \n"
                                                 "padding-left: 5px;\n"
                                                 "font-size: 15px;\n"
                                                 "")
        self.confirm_password_edit.setText("")
        self.confirm_password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password_edit.setObjectName("confirm_password_registration_edit")
        self.confirm_password_edit.textChanged.connect(self.equal_passwd)

        self.open_passwd = QtWidgets.QRadioButton(self.add_user_page)
        self.open_passwd.setGeometry(QtCore.QRect(440, 520, 171, 17))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.open_passwd.setFont(font)
        self.open_passwd.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                       " padding-left: 5px;")
        self.open_passwd.setObjectName("open_passwd")
        self.open_passwd.setText("Показать пароль")
        self.open_passwd.toggled.connect(self.view_passwd)

        self.alert = QtWidgets.QLabel(self.add_user_page)
        self.alert.setGeometry(QtCore.QRect(40, 560, 821, 201))
        self.alert.setStyleSheet("border-radius: 30px;")
        self.alert.setText("")
        self.alert.setObjectName("alert_registration")

        self.alert_title = QtWidgets.QLabel(self.add_user_page)
        self.alert_title.setGeometry(QtCore.QRect(40, 560, 961, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.alert_title.setFont(font)
        self.alert_title.setStyleSheet("border-top-left-radius: 30px;\n"
                                       "border-top-right-radius: 30px;\n"
                                       "background-color: rgb(227, 227, 227); \n"
                                       "color: rgb(179, 179, 179);")
        self.alert_title.setAlignment(QtCore.Qt.AlignCenter)
        self.alert_title.setObjectName("alert_registration_title")
        self.alert_title.setText("Предупреждение")

        self.alert_text = QtWidgets.QLabel(self.add_user_page)
        self.alert_text.setGeometry(QtCore.QRect(40, 620, 961, 141))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setUnderline(True)
        self.alert_text.setFont(font)
        self.alert_text.setStyleSheet("border-bottom-left-radius: 30px;\n"
                                      "border-bottom-right-radius: 30px;\n"
                                      "color: rgb(162, 162, 162);")
        self.alert_text.setAlignment(QtCore.Qt.AlignCenter)
        self.alert_text.setObjectName("alert_registration_text")

        self.hide_alert()

        self.button = QtWidgets.QPushButton(self.add_user_page)
        self.button.setGeometry(QtCore.QRect(70, 790, 901, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.button.setFont(font)
        self.button.setStyleSheet("border-radius: 10px;")
        self.button.setCheckable(False)
        self.button.setObjectName("button_registration")
        self.button.setText("Сохранить")
        self.button.clicked.connect(self.registration_user)

        if self.posts_edit.currentText() == 'Волочильщик':
            self.password_edit.setEnabled(False)
            self.confirm_password_edit.setEnabled(False)
            self.open_passwd.setEnabled(False)

        if self.main.burger_button.isChecked():
            self.open_sidebar()

    def registration_user(self):
        red_style = "background-color: #fff;\n border-radius: 10px; \n padding-left: 5px;\n font-size: 15px;\n border:2px solid red;\n"
        if not self.name_edit.text():
            self.alert_text.setText('Поле "Имя" обязательно к заполнению')
            self.show_alert()

            self.name_edit.setStyleSheet(red_style)

        elif not self.surname_edit.text():
            self.alert_text.setText('Поле "Фамилия" обязательно к заполнению')
            self.show_alert()

            self.surname_edit.setStyleSheet(red_style)
        elif not self.email_edit.text():
            self.alert_text.setText('Поле "Email" обязательно к заполнению')
            self.show_alert()
            self.email_edit.setStyleSheet(red_style)

        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.email_edit.text()):
            self.alert_text.setText('Невалидный email адрес')
            self.show_alert()
            self.email_edit.setStyleSheet(red_style)
        else:
            if self.posts_edit.currentText() == 'Волочильщик':
                if os.path.exists('config/db_config.bin'):
                    self.db.cursor.execute("""INSERT INTO users (first_name, last_name, patronymic, post, birthdate, email) 
                                            VALUES (%s, %s, %s, %s, %s, %s)""",(
                                        self.name_edit.text(), self.surname_edit.text(),
                                        self.patronic_edit.text(),
                                        self.posts_edit.currentText(),
                                        self.birthday_edit.text(), self.email_edit.text()))
                else:
                    date_from_edit = self.birthday_edit.date()
                    date_str = date_from_edit.toString("dd.MM.yyyy")
                    self.db.cursor.execute("""INSERT INTO users (first_name, last_name, patronymic, post, birthdate, email) 
                                            VALUES (?, ?, ?, ?, ?, ?)""",(
                                        self.name_edit.text(), self.surname_edit.text(),
                                        self.patronic_edit.text(),
                                        self.posts_edit.currentText(),
                                        date_str, self.email_edit.text()))
                self.db.connection.commit()
                self.alert_text.setText('Сохранено')
                self.show_alert()
            else:
                if self.password_edit.text() != self.confirm_password_edit.text():
                    self.alert_text.setText('Пароли не идентичны')
                    self.show_alert()

                elif len(self.password_edit.text()) < 8 and len(
                        self.confirm_password_edit.text()) < 8:
                    self.alert_text.setText('Пароль должен иметь 8 или больше символов')
                    self.password_edit.setStyleSheet(red_style)
                    self.confirm_password_edit.setStyleSheet(red_style)
                    self.show_alert()
                else:
                    if os.path.exists('config/db_config.bin'):
                        postgres_insert_query = """INSERT INTO users (first_name, last_name, patronymic, post, birthdate, email, passwd) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                        record_to_insert = (self.name_edit.text(), self.surname_edit.text(),
                                            self.patronic_edit.text(),
                                            self.posts_edit.currentText(),
                                            self.birthday_edit.text(), self.email_edit.text(),
                                            hash_passwd.hash_password(self.password_edit.text()))
                        self.db.cursor.execute(postgres_insert_query, record_to_insert)
                    else:
                        date_from_edit = self.birthday_edit.date()
                        date_str = date_from_edit.toString("dd.MM.yyyy")
                        self.db.cursor.execute("""INSERT INTO users (first_name, last_name, patronymic, post, birthdate, email, passwd) 
                                VALUES (?, ?, ?, ?, ?, ?, ?)""",(self.name_edit.text(), self.surname_edit.text(),
                                            self.patronic_edit.text(),
                                            self.posts_edit.currentText(),
                                            date_str, self.email_edit.text(),
                                            hash_passwd.hash_password(self.password_edit.text())))
                    self.db.connection.commit()
                    self.alert_text.setText('Сохранено')
                    self.show_alert()

    def closeEvent(self, event):
        self.main.db.disconnection_database()
        event.accept()

    def reset_posts(self, text):
        if text == 'Технолог':
            self.password_edit.setEnabled(True)
            self.confirm_password_edit.setEnabled(True)
            self.open_passwd.setEnabled(True)
        else:
            self.password_edit.setEnabled(False)
            self.confirm_password_edit.setEnabled(False)
            self.open_passwd.setEnabled(False)

    def view_passwd(self, selected):
        if selected:
            self.password_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
            self.confirm_password_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.password_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
            self.confirm_password_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def equal_passwd(self):
        red_style = "background-color: #fff;\n border-radius: 10px; \n padding-left: 5px;\n font-size: 15px;\n border:2px solid red;\n"
        green_style = "background-color: #fff;\n border-radius: 10px; \n padding-left: 5px;\n font-size: 15px;\n border:2px solid green;\n"

        if (self.password_edit.text() != self.confirm_password_edit.text()) or \
                (len(self.password_edit.text()) < 8 and len(self.confirm_password_edit.text()) < 8):
            self.password_edit.setStyleSheet(red_style)
            self.confirm_password_edit.setStyleSheet(red_style)
        else:
            self.password_edit.setStyleSheet(green_style)
            self.confirm_password_edit.setStyleSheet(green_style)

    def reset_name(self):
        self.name_edit.setStyleSheet(
            "background-color: #fff; border-radius: 10px; padding-left: 5px; font-size: 15px;\n")

    def reset_surname(self):
        self.surname_edit.setStyleSheet(
            "background-color: #fff; border-radius: 10px; padding-left: 5px; font-size: 15px;\n")

    def reset_email(self):
        self.email_edit.setStyleSheet(
            "background-color: #fff; border-radius: 10px; padding-left: 5px; font-size: 15px;\n")

    def open_sidebar(self):
        self.content_registration.setGeometry(QtCore.QRect(10, 10, 881, 861))
        self.name_label.setGeometry(QtCore.QRect(40, 40, 201, 31))
        self.name_edit.setGeometry(QtCore.QRect(40, 80, 201, 41))
        self.surname_label.setGeometry(QtCore.QRect(270, 40, 271, 31))
        self.surname_edit.setGeometry(QtCore.QRect(270, 80, 281, 41))
        self.patronic_label.setGeometry(QtCore.QRect(570, 40, 291, 31))
        self.patronic_edit.setGeometry(QtCore.QRect(570, 80, 291, 41))
        self.email_edit.setGeometry(QtCore.QRect(150, 190, 611, 51))
        self.email_label.setGeometry(QtCore.QRect(150, 150, 611, 31))
        self.birthday_label.setGeometry(QtCore.QRect(40, 280, 351, 31))
        self.birthday_edit.setGeometry(QtCore.QRect(40, 320, 350, 41))
        self.post_label.setGeometry(QtCore.QRect(510, 280, 351, 31))
        self.posts_edit.setGeometry(QtCore.QRect(510, 320, 350, 41))
        self.confirm_password_label.setGeometry(QtCore.QRect(510, 410, 351, 31))
        self.password_label.setGeometry(QtCore.QRect(40, 410, 351, 31))
        self.confirm_password_edit.setGeometry(QtCore.QRect(510, 450, 350, 41))
        self.password_edit.setGeometry(QtCore.QRect(40, 450, 350, 41))
        self.open_passwd.setGeometry(QtCore.QRect(370, 520, 171, 17))
        self.alert.setGeometry(QtCore.QRect(40, 560, 821, 201))
        self.alert_text.setGeometry(QtCore.QRect(40, 620, 821, 141))
        self.alert_title.setGeometry(QtCore.QRect(40, 560, 821, 61))
        self.button.setGeometry(QtCore.QRect(70, 790, 751, 61))

    def close_sidebar(self):
        self.content_registration.setGeometry(QtCore.QRect(10, 10, 1021, 861))
        self.name_label.setGeometry(QtCore.QRect(60, 40, 201, 31))
        self.name_edit.setGeometry(QtCore.QRect(60, 80, 201, 41))
        self.surname_label.setGeometry(QtCore.QRect(360, 40, 271, 31))
        self.surname_edit.setGeometry(QtCore.QRect(360, 80, 281, 41))
        self.patronic_label.setGeometry(QtCore.QRect(710, 40, 291, 31))
        self.patronic_edit.setGeometry(QtCore.QRect(710, 80, 291, 41))
        self.email_edit.setGeometry(QtCore.QRect(230, 180, 611, 51))
        self.email_label.setGeometry(QtCore.QRect(230, 140, 611, 31))
        self.birthday_label.setGeometry(QtCore.QRect(70, 280, 351, 31))
        self.birthday_edit.setGeometry(QtCore.QRect(70, 320, 350, 41))
        self.post_label.setGeometry(QtCore.QRect(600, 280, 351, 31))
        self.posts_edit.setGeometry(QtCore.QRect(600, 320, 350, 41))
        self.confirm_password_label.setGeometry(QtCore.QRect(600, 410, 401, 31))
        self.password_label.setGeometry(QtCore.QRect(40, 410, 391, 31))
        self.confirm_password_edit.setGeometry(QtCore.QRect(600, 450, 401, 41))
        self.password_edit.setGeometry(QtCore.QRect(40, 450, 401, 41))
        self.open_passwd.setGeometry(QtCore.QRect(440, 520, 171, 17))
        self.alert.setGeometry(QtCore.QRect(40, 560, 821, 201))
        self.alert_text.setGeometry(QtCore.QRect(40, 620, 961, 141))
        self.alert_title.setGeometry(QtCore.QRect(40, 560, 961, 61))
        self.button.setGeometry(QtCore.QRect(70, 790, 901, 61))
