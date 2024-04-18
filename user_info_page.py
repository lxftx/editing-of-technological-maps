import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

import hash_passwd
from alert import AlertMessage


class UserInfoPage(QWidget, AlertMessage):
    def __init__(self, db, user, main):
        super().__init__()

        self.db = db
        self.user = user
        self.main = main
        self.user_info_page = self

        self.content_info = QtWidgets.QLabel(self.user_info_page)
        self.content_info.setGeometry(QtCore.QRect(10, 10, 1021, 861))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.content_info.setFont(font)
        self.content_info.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                        "border-radius: 30px;\n"
                                        "color: rgb(255, 255, 17);")
        self.content_info.setText("")
        self.content_info.setObjectName("content_info")

        self.name_label = QtWidgets.QLabel(self.user_info_page)
        self.name_label.setGeometry(QtCore.QRect(30, 20, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                      " padding-left: 5px;")
        self.name_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.name_label.setObjectName("name_info_label")
        self.name_label.setText("Имя")

        self.name_edit = QtWidgets.QLineEdit(self.user_info_page)
        self.name_edit.setGeometry(QtCore.QRect(30, 60, 431, 41))
        self.name_edit.setStyleSheet("background-color: #fff;\n"
                                     "border-radius: 10px; \n"
                                     "padding-left: 5px;\n"
                                     "font-size: 15px;\n"
                                     "")
        self.name_edit.setText(self.user.name)
        self.name_edit.setObjectName("name_info_edit")
        self.name_edit.textChanged.connect(self.text_changed_name)

        self.surname_label = QtWidgets.QLabel(self.user_info_page)
        self.surname_label.setGeometry(QtCore.QRect(560, 20, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.surname_label.setFont(font)
        self.surname_label.setStyleSheet("background-color:rgb(240, 240, 240); padding-left: 5px;")
        self.surname_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.surname_label.setObjectName("surname_info_label")
        self.surname_label.setText("Фамилия")

        self.surname_edit = QtWidgets.QLineEdit(self.user_info_page)
        self.surname_edit.setGeometry(QtCore.QRect(560, 60, 441, 41))
        self.surname_edit.setStyleSheet("background-color: #fff;\n"
                                        "border-radius: 10px; \n"
                                        "padding-left: 5px;\n"
                                        "font-size: 15px;\n"
                                        "")
        self.surname_edit.setText(self.user.surname)
        self.surname_edit.setObjectName("surname_info_edit")
        self.surname_edit.textChanged.connect(self.text_changed_surname)

        self.patronic_label = QtWidgets.QLabel(self.user_info_page)
        self.patronic_label.setGeometry(QtCore.QRect(30, 140, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.patronic_label.setFont(font)
        self.patronic_label.setStyleSheet("background-color:rgb(240, 240, 240); padding-left: 5px")
        self.patronic_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.patronic_label.setObjectName("patronic_info_label")
        self.patronic_label.setText("Отчество")

        self.patronic_edit = QtWidgets.QLineEdit(self.user_info_page)
        self.patronic_edit.setGeometry(QtCore.QRect(30, 180, 431, 41))
        self.patronic_edit.setStyleSheet("background-color: #fff;\n"
                                         "border-radius: 10px; \n"
                                         "padding-left: 5px;\n"
                                         "font-size: 15px;\n"
                                         "")
        self.patronic_edit.setText(self.user.patronic)
        self.patronic_edit.setObjectName("patronic_info_edit")

        self.email_label = QtWidgets.QLabel(self.user_info_page)
        self.email_label.setGeometry(QtCore.QRect(560, 140, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("background-color:rgb(240, 240, 240); padding-left: 5px")
        self.email_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.email_label.setObjectName("email_info_label")
        self.email_label.setText("Email")

        self.email_edit = QtWidgets.QLineEdit(self.user_info_page)
        self.email_edit.setGeometry(QtCore.QRect(560, 180, 441, 41))
        self.email_edit.setStyleSheet("background-color: #fff;\n"
                                      "border-radius: 10px; \n"
                                      "padding-left: 5px;\n"
                                      "font-size: 15px;\n"
                                      "")
        self.email_edit.setText(self.user.email)
        self.email_edit.setObjectName("email_info_edit")
        self.email_edit.setEnabled(False)

        self.birthday_label = QtWidgets.QLabel(self.user_info_page)
        self.birthday_label.setGeometry(QtCore.QRect(30, 260, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.birthday_label.setFont(font)
        self.birthday_label.setStyleSheet("background-color:rgb(240, 240, 240); padding-left: 5px")
        self.birthday_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.birthday_label.setObjectName("birthday_info_label")
        self.birthday_label.setText("Дата рождения")

        self.birthday_edit = QtWidgets.QDateEdit(self.user_info_page)
        self.birthday_edit.setGeometry(QtCore.QRect(30, 300, 431, 41))
        self.birthday_edit.setStyleSheet("background-color: #fff;\n"
                                         "color: black;\n"
                                         "border-radius: 10px; \n"
                                         "padding-left: 5px;\n"
                                         "font-size: 15px;")
        self.birthday_edit.setCalendarPopup(True)
        self.birthday_edit.setDate(self.user.birthday)
        self.birthday_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.birthday_edit.setObjectName("birthday_info_edit")

        self.post_label = QtWidgets.QLabel(self.user_info_page)
        self.post_label.setGeometry(QtCore.QRect(560, 260, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.post_label.setFont(font)
        self.post_label.setStyleSheet("background-color:rgb(240, 240, 240); padding-left: 5px")
        self.post_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.post_label.setObjectName("post_info_label")
        self.post_label.setText("Должность")

        self.post_edit = QtWidgets.QLineEdit(self.user_info_page)
        self.post_edit.setGeometry(QtCore.QRect(560, 300, 441, 41))
        self.post_edit.setStyleSheet("background-color: #fff;\n"
                                     "border-radius: 10px; \n"
                                     "padding-left: 5px;\n"
                                     "font-size: 15px;\n"
                                     "")
        self.post_edit.setText(self.user.posts)
        self.post_edit.setObjectName("post_info_edit")
        self.post_edit.setEnabled(False)

        self.password_label = QtWidgets.QLabel(self.user_info_page)
        self.password_label.setGeometry(QtCore.QRect(30, 380, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("background-color:rgb(240, 240, 240); padding-left: 5px")
        self.password_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.password_label.setObjectName("password_info_label")
        self.password_label.setText("Пароль")

        self.password_edit = QtWidgets.QLineEdit(self.user_info_page)
        self.password_edit.setGeometry(QtCore.QRect(30, 420, 431, 41))
        self.password_edit.setStyleSheet("background-color: #fff;\n"
                                         "border-radius: 10px; \n"
                                         "padding-left: 5px;\n"
                                         "font-size: 15px;\n"
                                         "")
        self.password_edit.setText("")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_edit.setObjectName("password_info_edit")
        self.password_edit.textChanged.connect(self.equal_password)

        self.confirm_password_label = QtWidgets.QLabel(self.user_info_page)
        self.confirm_password_label.setGeometry(QtCore.QRect(560, 380, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.confirm_password_label.setFont(font)
        self.confirm_password_label.setStyleSheet("background-color:rgb(240, 240, 240); padding-left: 5px")
        self.confirm_password_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.confirm_password_label.setObjectName("confirm_info_password_label")
        self.confirm_password_label.setText('Повторите пароль')

        self.confirm_password_edit = QtWidgets.QLineEdit(self.user_info_page)
        self.confirm_password_edit.setGeometry(QtCore.QRect(560, 420, 441, 41))
        self.confirm_password_edit.setStyleSheet("background-color: #fff;\n"
                                                 "border-radius: 10px; \n"
                                                 "padding-left: 5px;\n"
                                                 "font-size: 15px;\n"
                                                 "")
        self.confirm_password_edit.setText("")
        self.confirm_password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password_edit.setObjectName("confirm_info_password_edit")
        self.confirm_password_edit.textChanged.connect(self.equal_password)

        self.alert = QtWidgets.QLabel(self.user_info_page)
        self.alert.setGeometry(QtCore.QRect(40, 520, 821, 201))
        self.alert.setStyleSheet("border-radius: 30px;")
        self.alert.setText("")
        self.alert.setObjectName("alert_info")

        self.alert_title = QtWidgets.QLabel(self.user_info_page)
        self.alert_title.setGeometry(QtCore.QRect(40, 520, 961, 61))
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
        self.alert_title.setObjectName("alert_info_title")
        self.alert_title.setText("Предупреждение")

        self.alert_text = QtWidgets.QLabel(self.user_info_page)
        self.alert_text.setGeometry(QtCore.QRect(40, 580, 961, 141))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setUnderline(True)
        self.alert_text.setFont(font)
        self.alert_text.setStyleSheet("border-bottom-left-radius: 30px;\n"
                                      "border-bottom-right-radius: 30px;\n"
                                      "color: rgb(162, 162, 162);")
        self.alert_text.setAlignment(QtCore.Qt.AlignCenter)
        self.alert_text.setObjectName("alert_info_text")
        self.alert_text.setText("Пароли должны совпадать")
        self.hide_alert()

        self.button = QtWidgets.QPushButton(self.user_info_page)
        self.button.setGeometry(QtCore.QRect(70, 770, 891, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.button.setFont(font)
        self.button.setStyleSheet("border-radius: 10px;")
        self.button.setCheckable(False)
        self.button.setObjectName("button_info")
        self.button.setText("Сохранить")
        self.button.clicked.connect(self.on_clicked)

        if self.user.posts == 'Волочильщик':
            self.password_edit.setEnabled(False)
            self.confirm_password_edit.setEnabled(False)
        if self.main.burger_button.isChecked():
            self.open_sidebar()

    def on_clicked(self):
        if not self.name_edit.text():
            self.name_edit.setStyleSheet(
                "background-color: #fff;\n border-radius: 10px; \n padding-left: 5px;\n font-size: 15px;\n border:2px solid red;\n")
            self.alert_text.setText('Поле "Имя" обязательно к заполнению')
            self.show_alert()
        elif not self.surname_edit.text():
            self.surname_edit.setStyleSheet(
                "background-color: #fff;\n border-radius: 10px; \n padding-left: 5px;\n font-size: 15px;\n border:2px solid red;\n")
            self.alert_text.setText('Поле "Фамилия" обязательно к заполнению')
            self.show_alert()
        else:
            if self.password_edit.text() and self.confirm_password_edit.text():
                if self.password_edit.text() != self.confirm_password_edit.text():
                    self.alert_text.setText(f'Пароли не соответствуют друг другу')
                    self.show_alert()
                elif len(self.password_edit.text()) < 8 and len(self.confirm_password_edit.text()) < 8:
                    self.alert_text.setText(f'Кол-во символов в пароле должно быть 8 или больше')
                    self.show_alert()
                else:
                    postgres_update_query = """UPDATE users SET first_name=%s, last_name=%s, patronymic=%s, birthdate=%s, 
                                email=%s, passwd=%s WHERE user_id=%s"""
                    record_to_update = (
                        self.name_edit.text(), self.surname_edit.text(), self.patronic_edit.text(),
                        self.birthday_edit.text(),
                        self.email_edit.text(), hash_passwd.hash_password(self.password_edit.text()), self.user.id)
                    self.user.update((self.user.id, self.name_edit.text(), self.surname_edit.text(), self.patronic_edit.text(), self.user.posts, self.birthday_edit.text(), self.user.email, hash_passwd.hash_password(self.user.password), self.user.code))
                    self.db.cursor.execute(postgres_update_query, record_to_update)
                    self.db.connection.commit()
                    self.alert_text.setText('Сохранено')
                    self.show_alert()
            elif self.password_edit.text() or self.confirm_password_edit.text():
                self.alert_text.setText("Заполните другую колонку с паролем")
                self.show_alert()
            else:
                postgres_insert_query = """UPDATE users SET first_name=%s, last_name=%s, patronymic=%s, birthdate=%s, 
                                email=%s WHERE user_id=%s"""
                record_to_insert = (
                    self.name_edit.text(), self.surname_edit.text(), self.patronic_edit.text(),
                    self.birthday_edit.text(), self.email_edit.text(), self.user.id)
                self.user.update((self.user.id, self.name_edit.text(), self.surname_edit.text(),
                                  self.patronic_edit.text(), self.user.posts, eval(f'datetime.date({self.birthday_edit.date().year()}, {self.birthday_edit.date().month()}, {self.birthday_edit.date().day()})'),
                                  self.user.email, self.user.password, self.user.code))
                self.db.cursor.execute(postgres_insert_query, record_to_insert)
                # f'datetime.date({self.birthday_edit.date().year()}, {self.birthday_edit.date().month()}, {self.birthday_edit.date().day()})'
                print(self.user.__dict__)
                self.db.connection.commit()
                self.alert_text.setText('Сохранено')
                self.show_alert()

    def equal_password(self):
        style_red = "background-color: #fff;\n border-radius: 10px; \n padding-left: 5px;\n font-size: 15px;\n border:2px solid red;\n"
        style_green = "background-color: #fff;\n border-radius: 10px; \n padding-left: 5px;\n font-size: 15px;\n border:2px solid green;\n"
        if self.password_edit.text() != self.confirm_password_edit.text():
            self.password_edit.setStyleSheet(style_red)
            self.confirm_password_edit.setStyleSheet(style_red)
            self.hide_alert()
        elif len(self.password_edit.text()) < 8 and len(self.confirm_password_edit.text()) < 8:
            self.password_edit.setStyleSheet(style_red)
            self.confirm_password_edit.setStyleSheet(style_red)
        else:
            self.password_edit.setStyleSheet(style_green)
            self.confirm_password_edit.setStyleSheet(style_green)

    def text_changed_name(self):
        self.hide_alert()
        self.name_edit.setStyleSheet(
            "background-color: #fff;\n border-radius: 10px; \n padding-left: 5px;\n font-size: 15px;\n")

    def text_changed_surname(self):
        self.hide_alert()
        self.surname_edit.setStyleSheet(
            "background-color: #fff;\n border-radius: 10px; \n padding-left: 5px;\n font-size: 15px;\n")


    def closeEvent(self, event):
        self.main.db.disconnection_database()
        event.accept()

    def open_sidebar(self):
        self.content_info.setGeometry(QtCore.QRect(10, 10, 881, 861))
        self.name_label.setGeometry(QtCore.QRect(30, 20, 371, 31))
        self.name_edit.setGeometry(QtCore.QRect(30, 60, 371, 41))
        self.surname_label.setGeometry(QtCore.QRect(490, 20, 371, 31))
        self.surname_edit.setGeometry(QtCore.QRect(490, 60, 391, 41))
        self.patronic_label.setGeometry(QtCore.QRect(30, 140, 361, 31))
        self.patronic_edit.setGeometry(QtCore.QRect(30, 180, 371, 41))
        self.password_edit.setGeometry(QtCore.QRect(30, 420, 371, 41))
        self.birthday_label.setGeometry(QtCore.QRect(30, 260, 361, 31))
        self.email_label.setGeometry(QtCore.QRect(490, 140, 391, 31))
        self.birthday_edit.setGeometry(QtCore.QRect(30, 300, 371, 41))
        self.email_edit.setGeometry(QtCore.QRect(490, 180, 391, 41))
        self.button.setGeometry(QtCore.QRect(70, 770, 751, 61))
        self.password_label.setGeometry(QtCore.QRect(30, 380, 371, 31))
        self.confirm_password_edit.setGeometry(QtCore.QRect(490, 410, 391, 41))
        self.confirm_password_label.setGeometry(QtCore.QRect(490, 370, 391, 31))
        self.post_label.setGeometry(QtCore.QRect(500, 260, 371, 31))
        self.post_edit.setGeometry(QtCore.QRect(490, 300, 391, 41))
        self.alert.setGeometry(QtCore.QRect(40, 520, 821, 201))
        self.alert_title.setGeometry(QtCore.QRect(40, 520, 821, 61))
        self.alert_text.setGeometry(QtCore.QRect(40, 580, 821, 141))

    def close_sidebar(self):
        self.content_info.setGeometry(QtCore.QRect(10, 10, 1021, 861))
        self.name_label.setGeometry(QtCore.QRect(30, 20, 431, 31))
        self.name_edit.setGeometry(QtCore.QRect(30, 60, 431, 41))
        self.surname_label.setGeometry(QtCore.QRect(560, 20, 441, 31))
        self.surname_edit.setGeometry(QtCore.QRect(560, 60, 441, 41))
        self.patronic_label.setGeometry(QtCore.QRect(30, 140, 431, 31))
        self.patronic_edit.setGeometry(QtCore.QRect(30, 180, 431, 41))
        self.password_edit.setGeometry(QtCore.QRect(30, 420, 431, 41))
        self.birthday_label.setGeometry(QtCore.QRect(30, 260, 431, 31))
        self.email_label.setGeometry(QtCore.QRect(560, 140, 441, 31))
        self.birthday_edit.setGeometry(QtCore.QRect(30, 300, 431, 41))
        self.email_edit.setGeometry(QtCore.QRect(560, 180, 441, 41))
        self.button.setGeometry(QtCore.QRect(70, 770, 891, 61))
        self.password_label.setGeometry(QtCore.QRect(30, 380, 431, 31))
        self.confirm_password_edit.setGeometry(QtCore.QRect(560, 420, 441, 41))
        self.confirm_password_label.setGeometry(QtCore.QRect(560, 380, 431, 31))
        self.post_label.setGeometry(QtCore.QRect(560, 260, 431, 31))
        self.post_edit.setGeometry(QtCore.QRect(560, 300, 441, 41))
        self.alert.setGeometry(QtCore.QRect(40, 520, 821, 201))
        self.alert_title.setGeometry(QtCore.QRect(40, 520, 961, 61))
        self.alert_text.setGeometry(QtCore.QRect(40, 580, 961, 141))