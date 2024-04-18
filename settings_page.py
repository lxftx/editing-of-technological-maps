import os
import ctypes
from cryptography.fernet import Fernet

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QFileDialog


class SettingsPage(QWidget):
    def __init__(self, main):
        super().__init__()
        self.settings_page = self
        self.main = main
        self.paswd = None

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
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.hint_button.setFont(font)
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

        if not os.path.exists('config'):
            os.makedirs('config')

        if not self.is_folder_hidden('config'):
            self.hide_folder(b'config')
        self.read_file()
        self.read_file_email()
        if self.main.burger_button.isChecked():
            self.open_sidebar()

        self.hint_button.installEventFilter(self)

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
        return super().eventFilter(watched, event)

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
            print(self.show_password.isChecked())
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
        self.hint_button.setGeometry(QtCore.QRect(920, 210, 101, 41))
        self.hint_title.setGeometry(QtCore.QRect(700, 270, 311, 20))
        self.hint_text.setGeometry(QtCore.QRect(710, 290, 301, 131))
