import os
import ctypes

from PyQt5.QtCore import QTimer
from cryptography.fernet import Fernet

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QFileDialog
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from alert import AlertMessage


class SettingsPage(QWidget, AlertMessage):
    def __init__(self, main):
        super().__init__()
        self.settings_page = self
        self.main = main
        self.paswd = None
        self.timer = QTimer()

        self.content_settings = QtWidgets.QLabel(self.settings_page)
        self.content_settings.setGeometry(QtCore.QRect(10, 10, 1021, 861))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.content_settings.setFont(font)
        self.content_settings.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                            "border-radius: 30px;\n"
                                            "color: rgb(255, 255, 17);")
        self.content_settings.setObjectName("content_settings")

        self.line_1 = QtWidgets.QLabel(self.settings_page)
        self.line_1.setGeometry(QtCore.QRect(10, 167, 1021, 5))
        self.line_1.setStyleSheet("background-color: black;")
        self.line_1.setObjectName("line_1")

        self.line_2 = QtWidgets.QLabel(self.settings_page)
        self.line_2.setGeometry(QtCore.QRect(10, 410, 1021, 5))
        self.line_2.setStyleSheet("background-color: black;")
        self.line_2.setObjectName("line_2")

        self.path = QtWidgets.QLabel(self.settings_page)
        self.path.setGeometry(QtCore.QRect(20, 40, 991, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.path.setFont(font)
        self.path.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                " padding-left: 5px;")
        self.path.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.path.setObjectName("path")
        self.path.setText('Укажите путь до директории с тех.картами')

        self.path_to_dir_edit = QtWidgets.QLineEdit(self.settings_page)
        self.path_to_dir_edit.setGeometry(QtCore.QRect(28, 80, 881, 41))
        self.path_to_dir_edit.setStyleSheet("background-color: #fff;\n"
                                            "border-radius: 10px; \n"
                                            "padding-left: 5px;\n"
                                            "font-size: 15px;\n"
                                            "")
        self.path_to_dir_edit.setText("")
        self.path_to_dir_edit.setObjectName("path_to_dir_edit")

        self.path_button = QtWidgets.QPushButton(self.settings_page)
        self.path_button.setGeometry(QtCore.QRect(920, 80, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.path_button.setFont(font)
        self.path_button.setStyleSheet("QPushButton#path_button {border-radius: 10px; background-color: white;} QPushButton#path_button:hover {background-color: rgb(184, 184, 184);}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icon/path_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.path_button.setIcon(icon1)
        self.path_button.setIconSize(QtCore.QSize(24, 24))
        self.path_button.setObjectName("path_button")
        self.path_button.clicked.connect(self.open_dialog)

        self.count_file = QtWidgets.QLabel(self.settings_page)
        self.count_file.setGeometry(QtCore.QRect(20, 130, 991, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.count_file.setFont(font)
        self.count_file.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                      " padding-left: 5px;")
        self.count_file.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.count_file.setObjectName("count_file")
        self.count_file.setText('Кол-во docx файлов в этой директории:')

        self.email_label = QtWidgets.QLabel(self.settings_page)
        self.email_label.setGeometry(QtCore.QRect(20, 172, 851, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                       " padding-left: 5px;")
        self.email_label.setText("Укажите корпоративную почту:")
        self.email_label.setObjectName("email_label")

        self.email_edit = QtWidgets.QLineEdit(self.settings_page)
        self.email_edit.setGeometry(QtCore.QRect(30, 210, 881, 41))
        self.email_edit.setStyleSheet("background-color: #fff;\n"
                                      "border-radius: 10px; \n"
                                      "padding-left: 5px;\n"
                                      "font-size: 15px;\n"
                                      "")
        self.email_edit.setPlaceholderText('example@mail.ru')
        self.email_edit.setObjectName("email_edit")

        self.password_label = QtWidgets.QLabel(self.settings_page)
        self.password_label.setGeometry(QtCore.QRect(20, 260, 851, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                          " padding-left: 5px;")
        self.password_label.setText("Укажите пароль от почты:")
        self.password_label.setObjectName("password_label")

        self.password_edit = QtWidgets.QLineEdit(self.settings_page)
        self.password_edit.setGeometry(QtCore.QRect(30, 300, 991, 41))
        self.password_edit.setStyleSheet("background-color: #fff;\n"
                                         "border-radius: 10px; \n"
                                         "padding-left: 5px;\n"
                                         "font-size: 15px;\n"
                                         "")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_edit.setObjectName("password_edit")

        self.hint_window = QtWidgets.QLabel(self.settings_page)
        self.hint_window.setGeometry(QtCore.QRect(690, 260, 331, 171))
        self.hint_window.setStyleSheet("border-radius: 30px;")
        self.hint_window.setObjectName("hint_window")
        self.hint_window.setVisible(False)

        self.hint_title = QtWidgets.QLabel(self.settings_page)
        self.hint_title.setGeometry(QtCore.QRect(700, 270, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.hint_title.setFont(font)
        self.hint_title.setAlignment(QtCore.Qt.AlignCenter)
        self.hint_title.setText("Для чего это?")
        self.hint_title.setObjectName("hint_title")
        self.hint_title.setVisible(False)

        self.hint_text = QtWidgets.QLabel(self.settings_page)
        self.hint_text.setGeometry(QtCore.QRect(710, 290, 301, 131))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.hint_text.setFont(font)
        self.hint_text.setText("При потере доступа к своему аккаунту, мож-\n"
"но будет восстановить аккаунт при помощи\n"
"сброса пароля. Указав почту и пароль,\n"
"сотрудники смогут получить код подтвер-\n"
"ждения на своей email и сбросить свой забытый\n"
"пароль!")
        self.hint_text.setObjectName("hint_text")
        self.hint_text.setVisible(False)

        self.hint_button = QtWidgets.QPushButton(self.settings_page)
        self.hint_button.setGeometry(QtCore.QRect(920, 210, 101, 41))
        self.hint_button.setStyleSheet("border-radius: 10px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icon/bulb_out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hint_button.setIcon(icon2)
        self.hint_button.setIconSize(QtCore.QSize(24, 24))
        self.hint_button.setObjectName("hint_button")

        self.save_button = QtWidgets.QPushButton(self.settings_page)
        self.save_button.setGeometry(QtCore.QRect(30, 360, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("QPushButton{\n"
                                       "    border-radius: 10px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: black;\n"
                                       "    color: white;\n"
                                       "}")
        self.save_button.setText("Сохранить")
        self.save_button.setObjectName("save_button")
        self.save_button.clicked.connect(self.save_email)

        self.show_password = QtWidgets.QRadioButton(self.settings_page)
        self.show_password.setGeometry(QtCore.QRect(300, 360, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.show_password.setFont(font)
        self.show_password.setStyleSheet("background-color:rgb(240, 240, 240);")
        self.show_password.setText("Показать пароль")
        self.show_password.setObjectName("show_password")
        self.show_password.clicked.connect(self.show_paswd)

        self.name_user_db_label = QtWidgets.QLabel(self.settings_page)
        self.name_user_db_label.setGeometry(QtCore.QRect(20, 422, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.name_user_db_label.setFont(font)
        self.name_user_db_label.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                              " padding-left: 5px;")
        self.name_user_db_label.setText("Имя пользователя:")
        self.name_user_db_label.setObjectName("name_user_db_label")

        self.name_user_db_edit = QtWidgets.QLineEdit(self.settings_page)
        self.name_user_db_edit.setGeometry(QtCore.QRect(30, 460, 271, 41))
        self.name_user_db_edit.setStyleSheet("background-color: #fff;\n"
                                             "border-radius: 10px; \n"
                                             "padding-left: 5px;\n"
                                             "font-size: 15px;\n"
                                             "")
        self.name_user_db_edit.setObjectName("name_user_db_edit")
        self.name_user_db_edit.textChanged.connect(self.default_edit)

        self.hint_button_2 = QtWidgets.QPushButton(self.settings_page)
        self.hint_button_2.setGeometry(QtCore.QRect(310, 460, 101, 41))
        self.hint_button_2.setStyleSheet("border-radius: 10px;")
        self.hint_button_2.setIcon(icon2)
        self.hint_button_2.setIconSize(QtCore.QSize(24, 24))
        self.hint_button_2.setObjectName("hint_button_2")

        self.password_db_label = QtWidgets.QLabel(self.settings_page)
        self.password_db_label.setGeometry(QtCore.QRect(420, 422, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.password_db_label.setFont(font)
        self.password_db_label.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                             " padding-left: 5px;")
        self.password_db_label.setText("Пароль:")
        self.password_db_label.setObjectName("password_db_label")

        self.password_db_edit = QtWidgets.QLineEdit(self.settings_page)
        self.password_db_edit.setGeometry(QtCore.QRect(430, 460, 271, 41))
        self.password_db_edit.setStyleSheet("background-color: #fff;\n"
                                            "border-radius: 10px; \n"
                                            "padding-left: 5px;\n"
                                            "font-size: 15px;\n"
                                            "")
        self.password_db_edit.setObjectName("password_db_edit")
        self.password_db_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_db_edit.textChanged.connect(self.default_edit)

        self.hint_button_3 = QtWidgets.QPushButton(self.settings_page)
        self.hint_button_3.setGeometry(QtCore.QRect(710, 460, 101, 41))
        self.hint_button_3.setStyleSheet("border-radius: 10px;")
        self.hint_button_3.setIcon(icon2)
        self.hint_button_3.setIconSize(QtCore.QSize(24, 24))
        self.hint_button_3.setObjectName("hint_button_3")

        self.host_db_label = QtWidgets.QLabel(self.settings_page)
        self.host_db_label.setGeometry(QtCore.QRect(20, 522, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.host_db_label.setFont(font)
        self.host_db_label.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                         " padding-left: 5px;")
        self.host_db_label.setText("Имя хоста:")
        self.host_db_label.setObjectName("host_db_label")

        self.host_db_edit = QtWidgets.QLineEdit(self.settings_page)
        self.host_db_edit.setGeometry(QtCore.QRect(30, 560, 271, 41))
        self.host_db_edit.setStyleSheet("background-color: #fff;\n"
                                        "border-radius: 10px; \n"
                                        "padding-left: 5px;\n"
                                        "font-size: 15px;\n"
                                        "")
        self.host_db_edit.setObjectName("host_db_edit")
        self.host_db_edit.textChanged.connect(self.default_edit)

        self.hint_button_4 = QtWidgets.QPushButton(self.settings_page)
        self.hint_button_4.setGeometry(QtCore.QRect(310, 560, 101, 41))
        self.hint_button_4.setStyleSheet("border-radius: 10px;")
        self.hint_button_4.setIcon(icon2)
        self.hint_button_4.setIconSize(QtCore.QSize(24, 24))
        self.hint_button_4.setObjectName("hint_button_4")

        self.port_db_label = QtWidgets.QLabel(self.settings_page)
        self.port_db_label.setGeometry(QtCore.QRect(420, 520, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.port_db_label.setFont(font)
        self.port_db_label.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                         " padding-left: 5px;")
        self.port_db_label.setText("Порт:")
        self.port_db_label.setObjectName("port_db_label")

        self.port_db_edit = QtWidgets.QLineEdit(self.settings_page)
        self.port_db_edit.setGeometry(QtCore.QRect(430, 558, 271, 41))
        self.port_db_edit.setStyleSheet("background-color: #fff;\n"
                                        "border-radius: 10px; \n"
                                        "padding-left: 5px;\n"
                                        "font-size: 15px;\n"
                                        "")
        self.port_db_edit.setObjectName("port_db_edit")
        self.port_db_edit.textChanged.connect(self.default_edit)

        self.name_db_label = QtWidgets.QLabel(self.settings_page)
        self.name_db_label.setGeometry(QtCore.QRect(730, 522, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.name_db_label.setFont(font)
        self.name_db_label.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                         " padding-left: 5px;")
        self.name_db_label.setText("Имя базы данных:")
        self.name_db_label.setObjectName("name_db_label")

        self.name_db_edit = QtWidgets.QLineEdit(self.settings_page)
        self.name_db_edit.setGeometry(QtCore.QRect(740, 560, 271, 41))
        self.name_db_edit.setStyleSheet("background-color: #fff;\n"
                                        "border-radius: 10px; \n"
                                        "padding-left: 5px;\n"
                                        "font-size: 15px;\n"
                                        "")
        self.name_db_edit.setObjectName("name_db_edit")
        self.name_db_edit.setPlaceholderText('По умолчанию:diplom')
        self.name_db_edit.textChanged.connect(self.default_edit)

        self.name_table_label = QtWidgets.QLabel(self.settings_page)
        self.name_table_label.setGeometry(QtCore.QRect(730, 602, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.name_table_label.setFont(font)
        self.name_table_label.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                            " padding-left: 5px;")
        self.name_table_label.setText("Имя таблицы:")
        self.name_table_label.setObjectName("name_table_label")

        self.name_table_edit = QtWidgets.QLineEdit(self.settings_page)
        self.name_table_edit.setGeometry(QtCore.QRect(740, 640, 271, 41))
        self.name_table_edit.setStyleSheet("background-color: #fff;\n"
                                           "border-radius: 10px; \n"
                                           "padding-left: 5px;\n"
                                           "font-size: 15px;\n"
                                           "")
        self.name_table_edit.setPlaceholderText('По умолчанию:users')
        self.name_table_edit.setObjectName("name_table_edit")

        self.save_info_db_connect_button = QtWidgets.QPushButton(self.settings_page)
        self.save_info_db_connect_button.setGeometry(QtCore.QRect(30, 620, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.save_info_db_connect_button.setFont(font)
        self.save_info_db_connect_button.setStyleSheet("QPushButton{\n"
                                                       "    border-radius: 10px;\n"
                                                       "}\n"
                                                       "\n"
                                                       "QPushButton:hover {\n"
                                                       "    background-color: black;\n"
                                                       "    color: white;\n"
                                                       "}")
        self.save_info_db_connect_button.setText("Сохранить")
        self.save_info_db_connect_button.setObjectName("save_info_db_connect_button")
        self.save_info_db_connect_button.clicked.connect(self.save_info_db)

        self.check_connect_button = QtWidgets.QPushButton(self.settings_page)
        self.check_connect_button.setGeometry(QtCore.QRect(290, 620, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.check_connect_button.setFont(font)
        self.check_connect_button.setStyleSheet("QPushButton{\n"
                                                "    border-radius: 10px;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: black;\n"
                                                "    color: white;\n"
                                                "}")
        self.check_connect_button.setText("Проверить подключение к БД")
        self.check_connect_button.setObjectName("check_connect_button")
        self.check_connect_button.clicked.connect(self.connect_database)

        self.create_db_button = QtWidgets.QPushButton(self.settings_page)
        self.create_db_button.setGeometry(QtCore.QRect(550, 620, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.create_db_button.setFont(font)
        self.create_db_button.setStyleSheet("QPushButton{\n"
                                            "    border-radius: 10px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: black;\n"
                                            "    color: white;\n"
                                            "}")
        self.create_db_button.setText("Создать БД")
        self.create_db_button.setObjectName("create_db_button")
        self.create_db_button.clicked.connect(self.create_db)

        self.create_table_button = QtWidgets.QPushButton(self.settings_page)
        self.create_table_button.setGeometry(QtCore.QRect(550, 660, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.create_table_button.setFont(font)
        self.create_table_button.setStyleSheet("QPushButton{\n"
                                               "    border-radius: 10px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                               "    background-color: black;\n"
                                               "    color: white;\n"
                                               "}")
        self.create_table_button.setText("Создать таблицу")
        self.create_table_button.setObjectName("create_table_button")
        self.create_table_button.clicked.connect(self.create_table)

        self.path_sqliite_label = QtWidgets.QLabel(self.settings_page)
        self.path_sqliite_label.setGeometry(QtCore.QRect(20, 740, 981, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.path_sqliite_label.setFont(font)
        self.path_sqliite_label.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                              " padding-left: 5px;")
        self.path_sqliite_label.setObjectName("path_sqliite_label")
        self.path_sqliite_label.setText("Расположение базы данных SQLite")

        self.path_to_sqllite_edit = QtWidgets.QLineEdit(self.settings_page)
        self.path_to_sqllite_edit.setGeometry(QtCore.QRect(28, 780, 881, 41))
        self.path_to_sqllite_edit.setStyleSheet("background-color: #fff;\n"
                                                "border-radius: 10px; \n"
                                                "padding-left: 5px;\n"
                                                "font-size: 15px;\n"
                                                "")
        self.path_to_sqllite_edit.setPlaceholderText("По умолчанию внутри проекта")
        self.path_to_sqllite_edit.setObjectName("path_to_sqllite_edit")

        self.path_sqllite_button = QtWidgets.QPushButton(self.settings_page)
        self.path_sqllite_button.setGeometry(QtCore.QRect(920, 780, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.path_sqllite_button.setFont(font)
        self.path_sqllite_button.setStyleSheet("border-radius: 10px;")
        self.path_sqllite_button.setText("")
        self.path_sqllite_button.setIcon(icon2)
        self.path_sqllite_button.setIconSize(QtCore.QSize(24, 24))
        self.path_sqllite_button.setObjectName("path_sqllite_button")
        self.path_sqllite_button.clicked.connect(self.path_sqllite)

        self.hint_window_2 = QtWidgets.QLabel(self.settings_page)
        self.hint_window_2.setGeometry(QtCore.QRect(80, 510, 331, 91))
        self.hint_window_2.setStyleSheet("border-radius: 30px;")
        self.hint_window_2.setObjectName("hint_window_2")
        self.hint_window_2.setVisible(False)

        self.hint_title_2 = QtWidgets.QLabel(self.settings_page)
        self.hint_title_2.setGeometry(QtCore.QRect(90, 520, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.hint_title_2.setFont(font)
        self.hint_title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.hint_title_2.setText("Для чего это?")
        self.hint_title_2.setObjectName("hint_title_2")
        self.hint_title_2.setVisible(False)

        self.hint_text_2 = QtWidgets.QLabel(self.settings_page)
        self.hint_text_2.setGeometry(QtCore.QRect(90, 540, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.hint_text_2.setFont(font)
        self.hint_text_2.setText("Имя пользователя: значение по умолчанию\nдля базы данных PostgreSQL – postgres.")
        self.hint_text_2.setObjectName("hint_text_2")
        self.hint_text_2.setVisible(False)

        self.hint_window_3 = QtWidgets.QLabel(self.settings_page)
        self.hint_window_3.setGeometry(QtCore.QRect(480, 510, 331, 91))
        self.hint_window_3.setStyleSheet("border-radius: 30px;")
        self.hint_window_3.setObjectName("hint_window_3")
        self.hint_window_3.setVisible(False)

        self.hint_title_3 = QtWidgets.QLabel(self.settings_page)
        self.hint_title_3.setGeometry(QtCore.QRect(490, 520, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.hint_title_3.setFont(font)
        self.hint_title_3.setAlignment(QtCore.Qt.AlignCenter)
        self.hint_title_3.setText("Для чего это?")
        self.hint_title_3.setObjectName("hint_title_3")
        self.hint_title_3.setVisible(False)

        self.hint_text_3 = QtWidgets.QLabel(self.settings_page)
        self.hint_text_3.setGeometry(QtCore.QRect(490, 540, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.hint_text_3.setFont(font)
        self.hint_text_3.setText("Пароль: пользователь получает пароль\nпри установке PostgreSQL.")
        self.hint_text_3.setObjectName("hint_text_3")
        self.hint_text_3.setVisible(False)

        self.hint_window_4 = QtWidgets.QLabel(self.settings_page)
        self.hint_window_4.setGeometry(QtCore.QRect(80, 610, 331, 91))
        self.hint_window_4.setStyleSheet("border-radius: 30px;")
        self.hint_window_4.setObjectName("hint_window_4")
        self.hint_window_4.setVisible(False)

        self.hint_title_4 = QtWidgets.QLabel(self.settings_page)
        self.hint_title_4.setGeometry(QtCore.QRect(90, 620, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.hint_title_4.setFont(font)
        self.hint_title_4.setAlignment(QtCore.Qt.AlignCenter)
        self.hint_title_4.setText("Для чего это?")
        self.hint_title_4.setObjectName("hint_title_4")
        self.hint_title_4.setVisible(False)

        self.hint_text_4 = QtWidgets.QLabel(self.settings_page)
        self.hint_text_4.setGeometry(QtCore.QRect(90, 640, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.hint_text_4.setFont(font)
        self.hint_text_4.setText(
            "Имя хоста: имя сервера или IP-адрес, на котором работает\nбаза данных. Если она запущена локально,\nто нужно использовать localhost или 127.0.0.0.")
        self.hint_text_4.setObjectName("hint_text_4")
        self.hint_text_4.setVisible(False)

        self.safety_window = QtWidgets.QLabel(self.settings_page)
        self.safety_window.setGeometry(QtCore.QRect(240, 300, 451, 151))
        self.safety_window.setStyleSheet("border-radius: 30px;")
        self.safety_window.setObjectName("safety_window")
        self.safety_window.setVisible(False)

        self.safety_title = QtWidgets.QLabel(self.settings_page)
        self.safety_title.setGeometry(QtCore.QRect(250, 310, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.safety_title.setFont(font)
        self.safety_title.setObjectName("safety_title")
        self.safety_title.setVisible(False)

        self.safety_password_edit = QtWidgets.QLineEdit(self.settings_page)
        self.safety_password_edit.setGeometry(QtCore.QRect(250, 350, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.safety_password_edit.setFont(font)
        self.safety_password_edit.setStyleSheet("background-color: #fff;\n"
                                                "border-radius: 10px; \n"
                                                "padding-left: 5px;\n"
                                                "font-size: 15px;\n"
                                                "border:1px solid black;\n"
                                                "color:black;\n"
                                                "")
        self.safety_password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.safety_password_edit.setObjectName("safety_password_edit")
        self.safety_password_edit.setVisible(False)
        self.safety_password_edit.textChanged.connect(self.saf_paswd_style)

        self.save_button_safety = QtWidgets.QPushButton(self.settings_page)
        self.save_button_safety.setGeometry(QtCore.QRect(260, 400, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.save_button_safety.setFont(font)
        self.save_button_safety.setStyleSheet("QPushButton{\n"
                                              "    border-radius: 10px;\n"
                                              "    border: 1px solid black;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: black;\n"
                                              "    color: white;\n"
                                              "}")
        self.save_button_safety.setText("Далее")
        self.save_button_safety.setObjectName("save_button_safety")
        self.save_button_safety.setVisible(False)
        self.save_button_safety.clicked.connect(self.save_password)

        self.cancel_button_safety = QtWidgets.QPushButton(self.settings_page)
        self.cancel_button_safety.setGeometry(QtCore.QRect(480, 400, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.cancel_button_safety.setFont(font)
        self.cancel_button_safety.setStyleSheet("QPushButton{\n"
                                                "    border-radius: 10px;\n"
                                                "    border: 1px solid black;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: black;\n"
                                                "    color: white;\n"
                                                "}")
        self.cancel_button_safety.setText("Отмена")
        self.cancel_button_safety.setVisible(False)
        self.cancel_button_safety.setObjectName("cancel_button_safety")
        self.cancel_button_safety.clicked.connect(self.cancel)

        self.alert = QtWidgets.QLabel(self.settings_page)
        self.alert.setGeometry(QtCore.QRect(40, 270, 821, 201))
        self.alert.setStyleSheet("border-radius: 30px;")
        self.alert.setObjectName("alert_info")
        self.alert.setVisible(False)

        self.alert_title = QtWidgets.QLabel(self.settings_page)
        self.alert_title.setGeometry(QtCore.QRect(40, 270, 961, 61))
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
        self.alert_title.setVisible(False)

        self.alert_text = QtWidgets.QLabel(self.settings_page)
        self.alert_text.setGeometry(QtCore.QRect(40, 330, 961, 141))
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
        self.alert_text.setVisible(False)

        if not os.path.exists('config'):
            os.makedirs('config')

        if not self.is_folder_hidden('config'):
            self.hide_folder(b'config')
        self.read_file()
        self.read_file_email()
        self.read_file_db()
        self.read_file_db_table()
        self.read_path_sqlite()
        if self.main.burger_button.isChecked():
            self.open_sidebar()

        self.hint_button.installEventFilter(self)
        self.hint_button_2.installEventFilter(self)
        self.hint_button_3.installEventFilter(self)
        self.hint_button_4.installEventFilter(self)

    def closeEvent(self, event):
        self.main.db.disconnection_database()
        event.accept()

    def eventFilter(self, watched, event):
        icon = QtGui.QIcon()
        if (event.type() == QtCore.QEvent.Enter) and (watched == self.hint_button):
            icon.addPixmap(QtGui.QPixmap("images/icon/bulb_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.hint_button.setIcon(icon)
            self.hint_window.setVisible(True)
            self.hint_title.setVisible(True)
            self.hint_text.setVisible(True)

        elif (event.type() == QtCore.QEvent.Leave) and (watched == self.hint_button):
            icon.addPixmap(QtGui.QPixmap("images/icon/bulb_out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.hint_button.setIcon(icon)
            self.hint_window.setVisible(False)
            self.hint_title.setVisible(False)
            self.hint_text.setVisible(False)

        elif (event.type() == QtCore.QEvent.Enter) and (watched == self.hint_button_2):
            icon.addPixmap(QtGui.QPixmap("images/icon/bulb_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.hint_button_2.setIcon(icon)
            self.hint_window_2.setVisible(True)
            self.hint_title_2.setVisible(True)
            self.hint_text_2.setVisible(True)

        elif (event.type() == QtCore.QEvent.Leave) and (watched == self.hint_button_2):
            icon.addPixmap(QtGui.QPixmap("images/icon/bulb_out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.hint_button_2.setIcon(icon)
            self.hint_window_2.setVisible(False)
            self.hint_title_2.setVisible(False)
            self.hint_text_2.setVisible(False)

        elif (event.type() == QtCore.QEvent.Enter) and (watched == self.hint_button_3):
            icon.addPixmap(QtGui.QPixmap("images/icon/bulb_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.hint_button_3.setIcon(icon)
            self.hint_window_3.setVisible(True)
            self.hint_title_3.setVisible(True)
            self.hint_text_3.setVisible(True)

        elif (event.type() == QtCore.QEvent.Leave) and (watched == self.hint_button_3):
            icon.addPixmap(QtGui.QPixmap("images/icon/bulb_out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.hint_button_3.setIcon(icon)
            self.hint_window_3.setVisible(False)
            self.hint_title_3.setVisible(False)
            self.hint_text_3.setVisible(False)

        elif (event.type() == QtCore.QEvent.Enter) and (watched == self.hint_button_4):
            icon.addPixmap(QtGui.QPixmap("images/icon/bulb_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.hint_button_4.setIcon(icon)
            self.hint_window_4.setVisible(True)
            self.hint_title_4.setVisible(True)
            self.hint_text_4.setVisible(True)

        elif (event.type() == QtCore.QEvent.Leave) and (watched == self.hint_button_4):
            icon.addPixmap(QtGui.QPixmap("images/icon/bulb_out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.hint_button_4.setIcon(icon)
            self.hint_window_4.setVisible(False)
            self.hint_title_4.setVisible(False)
            self.hint_text_4.setVisible(False)

        return super().eventFilter(watched, event)

    def read_path_sqlite(self):
        if os.path.exists('config/path_sqlite.bin'):
            with open('config/path_sqlite.bin', 'rb') as file:
                lines = file.readlines()
                key = lines[0].strip()
                enc_path_sqllite = lines[1]
            fernet = Fernet(key)
            dec_path_sqllite = fernet.decrypt(enc_path_sqllite).decode()
            self.path_to_sqllite_edit.setText(dec_path_sqllite)
        else:
            self.path_to_sqllite_edit.setText("")

    def path_sqllite(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать файл", "", "Файлы SQLite (*.db)")
        if file_path:
            self.path_to_sqllite_edit.setText(file_path)
            key = Fernet.generate_key()
            fernet = Fernet(key)
            enc_path_sql_db = fernet.encrypt(file_path.strip().encode())
            with open('config/path_sqlite.bin', 'wb') as file:
                file.write(key + b'\n')
                file.write(enc_path_sql_db)
            self.main.auth.show()
            self.main.close()


    def create_db(self):
        try:
            if self.red_style_edit([self.name_user_db_edit.text().strip(), self.password_db_edit.text().strip(), self.host_db_edit.text().strip(),
                   self.port_db_edit.text().strip()]):
                answer = self.main.db.connect_database(user=self.name_user_db_edit.text().strip(),
                                                       password=self.password_db_edit.text().strip(),
                                                       host=self.host_db_edit.text().strip(),
                                                       port=self.port_db_edit.text().strip(),)
                if answer:
                    name = self.name_db_edit.text().strip()
                    self.main.db.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                    if name:
                        self.main.db.cursor.execute(f"CREATE DATABASE {name}")
                        self.main.db.connection.commit()
                    else:
                        placeholder_text = self.name_db_edit.placeholderText().split(':')[1].strip()
                        self.main.db.cursor.execute(f"CREATE DATABASE {placeholder_text}")
                        self.main.db.connection.commit()
                    self.show_alert()
                    self.alert_text.setText(
                        f"База данных  с именем {self.name_db_edit.text().strip() if self.name_db_edit.text().strip() else self.name_db_edit.placeholderText().split(':')[1].strip()} была создана")
                    self.timer.setSingleShot(True)
                    self.timer.timeout.connect(self.hide_alert)
                    self.timer.start(3000)
                else:
                    self.show_alert()
                    self.alert_text.setText(answer[1])
                    self.timer.setSingleShot(True)
                    self.timer.timeout.connect(self.hide_alert)
                    self.timer.start(3000)
        except Exception as ex:
            print(ex)

    def read_file_db_table(self):
        if os.path.exists('config/name_table.bin'):
            with open('config/name_table.bin', 'rb') as file:
                lines = file.readlines()
                key = lines[0].strip()
                enc_name_table_db = lines[1]
            fernet = Fernet(key)
            dec_name_table_db = fernet.decrypt(enc_name_table_db).decode()
            self.name_table_edit.setText(dec_name_table_db)
        else:
            self.name_table_edit.setText("")

    def create_table(self):
        if self.connect_database()[0]:
            name = self.name_table_edit.text().strip()
            if name:
                with open('sql/SQL.sql', 'r') as sql_file:
                    sql_script = sql_file.read()
                new_content = sql_script.replace('users', self.name_table_edit.text().strip())
                self.main.db.cursor.execute(new_content)
                self.main.db.connection.commit()
            else:
                placeholder_text = self.name_table_edit.placeholderText().split(':')[1].strip()
                with open('sql/SQL.sql', 'r') as sql_file:
                    sql_script = sql_file.read()
                new_content = sql_script.replace('users', placeholder_text)
                self.main.db.cursor.execute(new_content)
                self.main.db.connection.commit()
            key = Fernet.generate_key()
            fernet = Fernet(key)
            enc_name_table_db = fernet.encrypt(self.name_table_edit.text().strip().encode())
            with open('config/name_table.bin', 'wb') as file:
                file.write(key + b'\n')
                file.write(enc_name_table_db)
            self.show_alert()
            self.alert_text.setText(
                f"Таблица с именем {self.name_table_edit.text().strip() if self.name_table_edit.text().strip() else self.name_table_edit.placeholderText().split(':')[1].strip()} была создана")
            self.timer.setSingleShot(True)
            self.timer.timeout.connect(self.hide_alert)
            self.timer.start(3000)




    def read_file_db(self):
        if os.path.exists('config/db_config.bin'):
            with open('config/db_config.bin', 'rb') as file:
                lines = file.readlines()
                key = lines[0].strip()
                enc_name_user_db = lines[1].strip()
                enc_passwd_db = lines[2].strip()
                enc_host_db = lines[3].strip()
                enc_port_db = lines[4].strip()
                enc_name_db = lines[5].strip()
            fernet = Fernet(key)
            dec_name_user_db = fernet.decrypt(enc_name_user_db).decode()
            dec_passwd_db = fernet.decrypt(enc_passwd_db).decode()
            dec_host_db = fernet.decrypt(enc_host_db).decode()
            dec_port_db = fernet.decrypt(enc_port_db).decode()
            dec_name_db = fernet.decrypt(enc_name_db).decode()
            self.name_user_db_edit.setText(dec_name_user_db)
            self.password_db_edit.setText(dec_passwd_db)
            self.host_db_edit.setText(dec_host_db)
            self.port_db_edit.setText(dec_port_db)
            self.name_db_edit.setText(dec_name_db)
        else:
            self.name_user_db_edit.setText("")
            self.password_db_edit.setText("")
            self.host_db_edit.setText("")
            self.port_db_edit.setText("")
            self.name_db_edit.setText("")

    def save_info_db(self):
        if self.connect_database()[0]:
            key = Fernet.generate_key()
            fernet = Fernet(key)
            enc_name_user_db = fernet.encrypt(self.name_user_db_edit.text().strip().encode())
            enc_passwd_db = fernet.encrypt(self.password_db_edit.text().strip().encode())
            enc_host_db = fernet.encrypt(self.host_db_edit.text().strip().encode())
            enc_port_db = fernet.encrypt(self.port_db_edit.text().strip().encode())
            enc_name_db = fernet.encrypt(self.name_db_edit.text().strip().encode())
            with open('config/db_config.bin', 'wb') as file:
                file.write(key + b'\n')
                file.write(enc_name_user_db + b'\n')
                file.write(enc_passwd_db + b'\n')
                file.write(enc_host_db + b'\n')
                file.write(enc_port_db + b'\n')
                file.write(enc_name_db)

    def connect_database(self):
        if self.name_db_edit.text().strip():
            lst = [self.name_user_db_edit.text().strip(), self.password_db_edit.text().strip(),
             self.host_db_edit.text().strip(),
             self.port_db_edit.text().strip(), self.name_db_edit.text().strip()]
        else:
            lst = [self.name_user_db_edit.text().strip(), self.password_db_edit.text().strip(), self.host_db_edit.text().strip(),
               self.port_db_edit.text().strip()]
        if self.red_style_edit(lst):
            answer = self.main.db.connect_database(user=self.name_user_db_edit.text().strip(), password=self.password_db_edit.text().strip(),
                                          host=self.host_db_edit.text().strip(), port=self.port_db_edit.text().strip(),
                                            database=self.name_db_edit.text().strip()) if len(lst) == 5 else self.main.db.connect_database(user=self.name_user_db_edit.text().strip(), password=self.password_db_edit.text().strip(),
                                          host=self.host_db_edit.text().strip(), port=self.port_db_edit.text().strip())
            if answer[0]:
                self.show_alert()
                self.alert_text.setText(answer[1])
                self.timer.setSingleShot(True)
                self.timer.timeout.connect(self.hide_alert)
                self.timer.start(3000)
                return answer
            else:
                self.show_alert()
                self.alert_text.setText(answer[1])
                self.timer.setSingleShot(True)
                self.timer.timeout.connect(self.hide_alert)
                self.timer.start(3000)
                return answer


    def red_style_edit(self, lst):
        tp = True
        red_background = "background-color: #fff;\n" \
                         "border-radius: 10px; \n" \
                         "padding-left: 5px;\n" \
                         "font-size: 15px;\n" \
                         "border:1px solid red;\n" \
                         ""
        for x, txt in enumerate(lst):
            if not txt:
                tp = False
                match x:
                    case 0:
                        self.name_user_db_edit.setStyleSheet(red_background)
                    case 1:
                        self.password_db_edit.setStyleSheet(red_background)
                    case 2:
                        self.host_db_edit.setStyleSheet(red_background)
                    case 3:
                        self.port_db_edit.setStyleSheet(red_background)
                    case 4:
                        self.name_db_edit.setStyleSheet(red_background)
                    case _:
                        ...
        return tp

    def default_edit(self):
        sender_widget = self.sender()
        if sender_widget is not None:
            sender_widget.setStyleSheet("background-color: #fff;\n"
                         "border-radius: 10px; \n"
                         "padding-left: 5px;\n"
                         "font-size: 15px;\n"
                         "")


    def cancel(self):
        self.widget_safyte_visible(False)
        self.safety_password_edit.clear()

    def show_paswd(self, evt):
        if evt:
            if self.paswd:
                self.password_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
                self.show_password.setChecked(evt)
            else:
                self.password_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
                self.save_email()
        else:
            self.password_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
            self.show_password.setChecked(False)

    def saf_paswd_style(self):
        self.safety_password_edit.setStyleSheet("background-color: #fff;\n"
                                                "border-radius: 10px; \n"
                                                "padding-left: 5px;\n"
                                                "font-size: 15px;\n"
                                                "border:1px solid black;\n"
                                                "color:black;\n"
                                                "")

    def widget_safyte_visible(self, bool):
        self.safety_window.setVisible(bool)
        self.safety_title.setVisible(bool)
        self.safety_password_edit.setVisible(bool)
        self.save_button_safety.setVisible(bool)
        self.cancel_button_safety.setVisible(bool)

    def save_password(self):
        if os.path.exists('config/auth.bin'):
            with open('config/auth.bin', 'rb') as file:
                key = file.readline().strip()
                enc_message = file.read()
                fernet = Fernet(key)
                dec_message = fernet.decrypt(enc_message).decode()
                if self.safety_password_edit.text() == dec_message:
                    self.paswd = True
                    self.widget_safyte_visible(False)
                    key = Fernet.generate_key()
                    fernet = Fernet(key)
                    encEmail = fernet.encrypt(self.email_edit.text().encode())
                    encpaswd = fernet.encrypt(self.password_edit.text().encode())
                    with open('config/email.bin', 'wb') as file:
                        file.write(key)
                        file.write(b'\n')
                        file.write(encEmail)
                        file.write(b'\n')
                        file.write(encpaswd)
                else:
                    self.safety_password_edit.setStyleSheet("background-color: #fff;\n"
                                                "border-radius: 10px; \n"
                                                "padding-left: 5px;\n"
                                                "font-size: 15px;\n"
                                                "border:1px solid red;\n"
                                                "color:black;\n"
                                                "")
        else:
            key = Fernet.generate_key()
            fernet = Fernet(key)
            encMessage = fernet.encrypt(self.safety_password_edit.text().encode())
            with open('config/auth.bin', 'wb') as file:
                file.write(key)
                file.write(b'\n')
                file.write(encMessage)
            self.widget_safyte_visible(False)

    def save_email(self):
        if not os.path.exists('config/auth.bin'):
            self.safety_title.setText("Придумайте пароль для безопасности:")
            self.save_button_safety.setText("Сохранить пароль")
            self.safety_password_edit.clear()
            self.widget_safyte_visible(True)

        else:
            if self.show_password.isChecked():
                self.save_button_safety.setText("Подветрдить")
                self.show_password.setChecked(False)
            else:
                self.save_button_safety.setText("Сохранить данные")
            self.safety_title.setText("Введите пароль безопасности:")
            self.safety_password_edit.clear()
            self.widget_safyte_visible(True)


    def is_folder_hidden(self, folder_path):
        attrs = ctypes.windll.kernel32.GetFileAttributesW(folder_path)
        return attrs & 0x02 == 0x02

    def hide_folder(self, folder_path):
        path = folder_path.decode("utf-8")
        ctypes.windll.kernel32.SetFileAttributesW(path, 0x02)

    def read_file_email(self):
        if os.path.exists('config/email.bin'):
            with open('config/email.bin', 'rb') as file:
                lines = file.readlines()
                key = lines[0].strip()
                encEmail = lines[1].strip()
                encpaswd = lines[2].strip()
            fernet = Fernet(key)
            dec_email = fernet.decrypt(encEmail).decode()
            dec_paswd = fernet.decrypt(encpaswd).decode()
            self.email_edit.setText(dec_email)
            self.password_edit.setText(dec_paswd)
        else:
            self.email_edit.setText("")
            self.password_edit.setText("")

    def read_file(self):
        lst = []
        if os.path.exists('config/url.bin'):
            with open('config/url.bin', 'rb') as file:
                key = file.readline().strip()
                enc_message = file.read()
            fernet = Fernet(key)
            dec_message = fernet.decrypt(enc_message).decode()
            self.path_to_dir_edit.setText(dec_message)
            docx_count = 0
            for filename in os.listdir(dec_message):
                if not filename.startswith("~$") and filename.endswith(".docx"):
                    docx_count += 1
            self.count_file.setText(f'{self.count_file.text()} {docx_count}')
            return dec_message + '/'
        else:
            self.path_to_dir_edit.setText('')
    def open_dialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Выбрать папку", self.path_to_dir_edit.text() if self.path_to_dir_edit.text().strip() else "/")
        if folder_path:
            self.path_to_dir_edit.setText(folder_path)
            docx_count = 0
            for filename in os.listdir(folder_path):
                if filename.endswith(".docx"):
                    docx_count += 1
            self.count_file.setText(f'{self.count_file.text()} {docx_count}')
            key = Fernet.generate_key()
            fernet = Fernet(key)
            encMessage = fernet.encrypt(folder_path.encode())
            with open('config/url.bin', 'wb') as file:
                file.write(key)
                file.write(b'\n')
                file.write(encMessage)


    def open_sidebar(self):
        self.content_settings.setGeometry(QtCore.QRect(10, 10, 881, 861))
        self.path_to_dir_edit.setGeometry(QtCore.QRect(28, 80, 741, 41))
        self.count_file.setGeometry(QtCore.QRect(20, 130, 861, 31))
        self.path.setGeometry(QtCore.QRect(20, 40, 851, 31))
        self.path_button.setGeometry(QtCore.QRect(780, 80, 101, 41))
        self.email_label.setGeometry(QtCore.QRect(20, 172, 851, 31))
        self.email_edit.setGeometry(QtCore.QRect(30, 210, 741, 41))
        self.password_label.setGeometry(QtCore.QRect(20, 260, 851, 31))
        self.password_edit.setGeometry(QtCore.QRect(30, 300, 851, 41))
        self.save_button.setGeometry(QtCore.QRect(30, 360, 241, 31))
        self.show_password.setGeometry(QtCore.QRect(300, 360, 171, 31))
        self.hint_button.setGeometry(QtCore.QRect(780, 210, 101, 41))
        self.hint_window.setGeometry(QtCore.QRect(550, 260, 331, 171))
        self.hint_title.setGeometry(QtCore.QRect(560, 270, 311, 20))
        self.hint_text.setGeometry(QtCore.QRect(570, 290, 301, 131))
        self.line_1.setGeometry(QtCore.QRect(10, 167, 881, 5))
        self.line_2.setGeometry(QtCore.QRect(10, 410, 881, 5))

    def close_sidebar(self):
        self.content_settings.setGeometry(QtCore.QRect(10, 10, 1021, 861))
        self.path.setGeometry(QtCore.QRect(20, 40, 991, 31))
        self.path_to_dir_edit.setGeometry(QtCore.QRect(28, 80, 881, 41))
        self.path_button.setGeometry(QtCore.QRect(920, 80, 101, 41))
        self.count_file.setGeometry(QtCore.QRect(20, 130, 991, 31))
        self.email_label.setGeometry(QtCore.QRect(20, 172, 851, 31))
        self.email_edit.setGeometry(QtCore.QRect(30, 210, 881, 41))
        self.password_label.setGeometry(QtCore.QRect(20, 260, 851, 31))
        self.password_edit.setGeometry(QtCore.QRect(30, 300, 991, 41))
        self.save_button.setGeometry(QtCore.QRect(30, 360, 241, 31))
        self.show_password.setGeometry(QtCore.QRect(300, 360, 171, 31))
        self.hint_window.setGeometry(QtCore.QRect(690, 260, 331, 171))
        self.hint_button.setGeometry(QtCore.QRect(920, 210, 101, 41))
        self.hint_title.setGeometry(QtCore.QRect(700, 270, 311, 20))
        self.hint_text.setGeometry(QtCore.QRect(710, 290, 301, 131))
        self.line_1.setGeometry(QtCore.QRect(10, 167, 1021, 5))
        self.line_2.setGeometry(QtCore.QRect(10, 410, 1021, 5))
