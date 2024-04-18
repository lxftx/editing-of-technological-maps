# -*- coding: utf-8 -*-
import datetime
import random
import re
import ssl
from email.message import EmailMessage
import smtplib
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

import hash_passwd




class ResetPassword(QWidget):
    def __init__(self, db, auth, email, passwd):
        super().__init__()

        self.db = None
        self.time_obj = datetime.datetime.now().strftime('%X')
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.remaining_time = 0
        self.numbers = [x for x in range(100000, 1000000)]

        self.db = db
        self.auth = auth
        self.dec_email = email
        self.dec_passwd = passwd
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.setFixedSize(641, 662)
        self.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.container = QtWidgets.QLabel(self)
        self.container.setGeometry(QtCore.QRect(30, 20, 581, 621))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setUnderline(True)
        self.container.setFont(font)
        self.container.setStyleSheet("background-color: #fff; border-radius: 30px;")
        self.container.setText("")
        self.container.setObjectName("container")
        self.header = QtWidgets.QLabel(self)
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
        self.email = QtWidgets.QLabel(self)
        self.email.setGeometry(QtCore.QRect(40, 180, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.email.setFont(font)
        self.email.setStyleSheet("background-color: #fff;\n"
                                 "padding: 0 10px;")
        self.email.setObjectName("email")
        self.email_edit = QtWidgets.QLineEdit(self)
        self.email_edit.setGeometry(QtCore.QRect(40, 230, 541, 41))
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
        self.email_edit.textChanged.connect(self.changed_text_email)

        self.code = QtWidgets.QLabel(self)
        self.code.setGeometry(QtCore.QRect(40, 340, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.code.setFont(font)
        self.code.setStyleSheet("background-color: #fff;\n"
                                "padding: 0 10px;")
        self.code.setObjectName("code")
        self.code_edit = QtWidgets.QLineEdit(self)
        self.code_edit.setGeometry(QtCore.QRect(40, 390, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(15)
        self.code_edit.setFont(font)
        self.code_edit.setStyleSheet("background-color: #fff;\n"
                                     "border: 2px solid #bdbdbd;\n"
                                     "border-radius: 10px;\n"
                                     "padding: 0 10px;\n"
                                     "")
        self.code_edit.setText("")
        self.code_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.code_edit.setObjectName("code_edit")
        self.code_edit.setEnabled(False)
        self.code_edit.textChanged.connect(self.confirm_code)

        self.button = QtWidgets.QPushButton(self)
        self.button.setGeometry(QtCore.QRect(90, 530, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        self.button.setFont(font)
        self.button.setStyleSheet("QPushButton#button {\n"
                                  "    background-color: #bdbdbd; \n"
                                  "    color: white;\n"
                                  "    border-radius: 10px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#button:hover {\n"
                                  "    background-color: #474744;\n"
                                  "}")
        self.button.setObjectName("button")
        self.button.setEnabled(False)
        self.button.clicked.connect(self.update_pswd)

        self.feedback = QtWidgets.QLabel(self)
        self.feedback.setGeometry(QtCore.QRect(40, 460, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.feedback.setFont(font)
        self.feedback.setStyleSheet("background-color: #fff;\n"
                                    "padding: 0 10px; color: red;")
        self.feedback.setText("")
        self.feedback.setObjectName("feedback")

        self.button_code = QtWidgets.QPushButton(self)
        self.button_code.setGeometry(QtCore.QRect(190, 280, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.button_code.setFont(font)
        self.button_code.setStyleSheet("QPushButton#button_code {\n"
                                       "    background-color: black; \n"
                                       "    color: white;\n"
                                       "    border-radius: 10px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#button_code:hover {\n"
                                       "    background-color: #474744;\n"
                                       "}")
        self.button_code.setObjectName("button_code")
        self.button_code.clicked.connect(self.send_message)

        self.new_password = QtWidgets.QLabel(self)
        self.new_password.setText("Новый пароль:")
        self.new_password.setGeometry(QtCore.QRect(40, 180, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.new_password.setFont(font)
        self.new_password.setStyleSheet("background-color: #fff;\n"
                                        "padding: 0 10px;")
        self.new_password.setObjectName("new_password")
        self.new_password.setVisible(False)

        self.new_password_edit = QtWidgets.QLineEdit(self)
        self.new_password_edit.setGeometry(QtCore.QRect(40, 230, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(15)
        self.new_password_edit.setFont(font)
        self.new_password_edit.setStyleSheet("background-color: #fff;\n"
                                             "border: 2px solid black;\n"
                                             "border-radius: 10px;\n"
                                             "padding: 0 10px;\n"
                                             "")
        self.new_password_edit.setText("")
        self.new_password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_password_edit.setObjectName("new_password_edit")
        self.new_password_edit.setVisible(False)
        self.new_password_edit.textChanged.connect(self.check_password)

        self.view_password = QtWidgets.QRadioButton(self)
        self.view_password.setText("Посмотреть пароль")
        self.view_password.setGeometry(QtCore.QRect(50, 280, 511, 31))
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
        self.view_password.setVisible(False)
        self.view_password.toggled.connect(self.show_password)

        self.new_password_confim = QtWidgets.QLabel(self)
        self.new_password_confim.setText("Подтверждение пароля:")
        self.new_password_confim.setGeometry(QtCore.QRect(40, 340, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.new_password_confim.setFont(font)
        self.new_password_confim.setStyleSheet("background-color: #fff;\n"
                                               "padding: 0 10px;")
        self.new_password_confim.setObjectName("new_password_confim")
        self.new_password_confim.setVisible(False)

        self.new_password_confim_edit = QtWidgets.QLineEdit(self)
        self.new_password_confim_edit.setGeometry(QtCore.QRect(40, 390, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(15)
        self.new_password_confim_edit.setFont(font)
        self.new_password_confim_edit.setStyleSheet("background-color: #fff;\n"
                                                    "border: 2px solid black;\n"
                                                    "border-radius: 10px;\n"
                                                    "padding: 0 10px;\n"
                                                    "")
        self.new_password_confim_edit.setText("")
        self.new_password_confim_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_password_confim_edit.setObjectName("new_password_confim_edit")
        self.new_password_confim_edit.setVisible(False)
        self.new_password_confim_edit.textChanged.connect(self.check_password)

        self.button_new_password = QtWidgets.QPushButton(self)
        self.button_new_password.setText("Изменить пароль")
        self.button_new_password.setGeometry(QtCore.QRect(90, 530, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        self.button_new_password.setFont(font)
        self.button_new_password.setStyleSheet("QPushButton#button_new_password {\n"
                                               "    background-color: black; \n"
                                               "    color: white;\n"
                                               "    border-radius: 10px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton#button_new_password:hover {\n"
                                               "    background-color: #474744;\n"
                                               "}")
        self.button_new_password.setObjectName("button_new_password")
        self.button_new_password.setVisible(False)
        self.button_new_password.clicked.connect(self.update_pswd_user)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle("Form")
        self.header.setText( "Забыли пароль?")
        self.email.setText("Email пользователя:")
        self.email_edit.setPlaceholderText("example@<domain>.[ru/com]")
        self.code.setText("Код подтверждения:")
        self.button.setText("Подтвердить код")
        self.button_code.setText( "Отправить код")

    def show_password(self, event):
        if event:
            self.new_password_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
            self.new_password_confim_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.new_password_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
            self.new_password_confim_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def check_password(self):
        red_stylesheet = "background-color: #fff; border: 2px solid red; border-radius: 10px; padding: 0 10px;"
        green_stylesheet = "background-color: #fff; border: 2px solid green; border-radius: 10px; padding: 0 10px;"
        pswd_list = [self.new_password_edit.text(), self.new_password_confim_edit.text()]
        if any([True for x in pswd_list if len(x) < 7]):
            self.new_password_edit.setStyleSheet(red_stylesheet)
            self.new_password_confim_edit.setStyleSheet(red_stylesheet)
        elif self.new_password_edit.text() != self.new_password_confim_edit.text():
            self.new_password_edit.setStyleSheet(red_stylesheet)
            self.new_password_confim_edit.setStyleSheet(red_stylesheet)
        elif any([True for x in pswd_list if ' ' in x]):
            self.new_password_edit.setStyleSheet(red_stylesheet)
            self.new_password_confim_edit.setStyleSheet(red_stylesheet)
        elif any([True for x in pswd_list if re.search('[а-яА-Я]', x)]):
            self.new_password_edit.setStyleSheet(red_stylesheet)
            self.new_password_confim_edit.setStyleSheet(red_stylesheet)
        else:
            self.new_password_edit.setStyleSheet(green_stylesheet)
            self.new_password_confim_edit.setStyleSheet(green_stylesheet)
        self.feedback.clear()

    def send_message(self):
        if self.email_edit.text():
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.email_edit.text()):
                self.db.cursor.execute("""SELECT * FROM users WHERE email = %s""",
                                       (self.email_edit.text(),))
                select = self.db.cursor.fetchone()
                if select:
                    if select[4] != 'Волочильщик':
                        self.remaining_time = 60
                        self.button_code.setEnabled(False)
                        self.button_code.setStyleSheet("background-color: #bdbdbd; color: white; border-radius: 10px;")

                        random_number = random.choice(self.numbers)

                        postgres_insert_query = """UPDATE users SET code=%s WHERE user_id=%s"""
                        record_to_insert = (random_number, select[0])
                        self.db.cursor.execute(postgres_insert_query, record_to_insert)
                        self.db.connection.commit()

                        email_sender = f'{self.dec_email}'
                        email_password = f'{self.dec_passwd}'
                        email_receiver = self.email_edit.text()

                        subject = 'Подтверждение почты пользователя'

                        em = EmailMessage()
                        em['From'] = email_sender
                        em['To'] = email_receiver
                        em['Subject'] = subject

                        body_text = f"Код подтверждения - {random_number}"

                        html_content = """
                        <!DOCTYPE html>
                        <html>
                        <head>
                            <style>
                                body {{
                                    font-family: Arial, sans-serif;
                                    background-color: #f4f4f4;
                                    padding: 20px;
                                }}
                                .container {{
                                    max-width: 600px;
                                    margin: auto;
                                    padding: 20px;
                                    border: 1px solid #ccc;
                                    border-radius: 10px;
                                    background-color: #fff;
                                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                                }}
                                h1 {{
                                    color: #333;
                                    text-align: center;
                                }}
                                p {{
                                    color: #666;
                                    margin-bottom: 20px;
                                }}
                                .code {{
                                    font-size: 24px;
                                    color: #007bff;
                                    text-align: center;
                                    margin-top: 20px;
                                }}
                            </style>
                        </head>
                        <body>
                            <div class="container">
                                <h1>Привет, {} {} {}!</h1>
                                <p>Это письмо с кодом, для восстановления пароля.</p>
                                <p>Ниже приведен ваш код подтверждения:</p>
                                <div class="code">{}</div>
                            </div>
                        </body>
                        </html>
                        """.format(select[2], select[1], select[3], body_text)

                        # Добавляем HTML содержимое в сообщение
                        em.add_alternative(html_content, subtype='html')

                        context = ssl.create_default_context()

                        with smtplib.SMTP_SSL('smtp.mail.ru', 465, context=context) as smtp:
                            smtp.login(email_sender, email_password)
                            smtp.sendmail(email_sender, email_receiver, em.as_string())

                        self.code_edit.setEnabled(True)
                        self.code_edit.setStyleSheet("background-color: #fff;\n"
                                                     "border: 2px solid black;\n"
                                                     "border-radius: 10px;\n"
                                                     "padding: 0 10px;\n"
                                                     "")

                        self.timer.start(1000)  # 1000 milliseconds = 1 second

                    else:
                        self.feedback.setText('Волочильщик не имеет доступа к смене пароля')
                else:
                    self.feedback.setText('Пользователя с таким email не найден')
                    self.email_edit.setStyleSheet("background-color: #fff;\n"
                                                  "border: 2px solid red;\n"
                                                  "border-radius: 10px;\n"
                                                  "padding: 0 10px;\n"
                                                  "")
            else:
                self.feedback.setText('Невалидный email адрес')
                self.email_edit.setStyleSheet("background-color: #fff;\n"
                                              "border: 2px solid red;\n"
                                              "border-radius: 10px;\n"
                                              "padding: 0 10px;\n"
                                              "")
        else:
            self.feedback.setText('Укажите Email пользователя')
            self.email_edit.setStyleSheet("background-color: #fff;\n"
                                          "border: 2px solid red;\n"
                                          "border-radius: 10px;\n"
                                          "padding: 0 10px;\n"
                                          "")

    def update_timer(self):
        self.remaining_time -= 1
        if self.remaining_time <= 0:
            self.timer.stop()
            self.button_code.setEnabled(True)
            self.button_code.setText("Отправить код")
            self.button_code.setStyleSheet("background-color: black; color: white; border-radius: 10px;")
        else:
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.button_code.setText(f"Отправить код ({minutes:02}:{seconds:02})")

    def changed_text_email(self):
        self.feedback.clear()
        self.email_edit.setStyleSheet("background-color: #fff;\n"
                                      "border: 2px solid black;\n"
                                      "border-radius: 10px;\n"
                                      "padding: 0 10px;\n"
                                      "")

    def confirm_code(self):
        self.button.setEnabled(True)
        self.button.setStyleSheet("QPushButton#button {\n"
                                  "    background-color: black; \n"
                                  "    color: white;\n"
                                  "    border-radius: 10px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#button:hover {\n"
                                  "    background-color: #474744;\n"
                                  "}")

    def update_pswd(self):
        try:
            self.db.cursor.execute("""SELECT * FROM users WHERE email = %s""", (self.email_edit.text(),))
            select = self.db.cursor.fetchone()
            print(select[8])
            if str(select[8]) == self.code_edit.text():
                self.new_password.setVisible(True)
                self.new_password_edit.setVisible(True)
                self.view_password.setVisible(True)
                self.new_password_confim.setVisible(True)
                self.new_password_confim_edit.setVisible(True)
                self.button_new_password.setVisible(True)
                self.button_code.setVisible(False)
            else:
                self.feedback.setText("Код не верный")
        except Exception as e:
            print("Error in update_pswd:", e)

    def update_pswd_user(self):
        pswd_list = [self.new_password_edit.text(), self.new_password_confim_edit.text()]
        if any([True for x in pswd_list if len(x) < 7]):
            self.feedback.setText("Пароли должны быть 8 и более символов.")
        elif self.new_password_edit.text() != self.new_password_confim_edit.text():
            self.feedback.setText("Пароли не соответствуют друг другу.")
        elif any([True for x in pswd_list if ' ' in x]):
            self.feedback.setText("В пароле не должны содержаться пробелы.")
        elif any([True for x in pswd_list if re.search('[а-яА-Я]', x)]):
            self.feedback.setText("Пароль должен содержать только Латинские символы")
        else:
            postgres_insert_query = """UPDATE users SET passwd=%s WHERE email=%s"""
            record_to_insert = (hash_passwd.hash_password(self.new_password_edit.text()), self.email_edit.text())
            self.db.cursor.execute(postgres_insert_query, record_to_insert)
            self.db.connection.commit()
            self.feedback.setText('Сохранено')

    def closeEvent(self, event):
        self.auth.show()
        self.db.disconnection_database()
        event.accept()