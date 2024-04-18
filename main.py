# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QEvent, QObject
from PyQt5.QtWidgets import QMainWindow, QWidget

from calculation_page import CalculationPage
from settings_page import SettingsPage
from user_info_page import UserInfoPage
from registration_user_page import RegistrationUserPage
from users_page import UsersPage
from home_page import HomePage

import hash_passwd


class Main(QMainWindow):
    def __init__(self, db, user, auth):
        super().__init__()
        self.db = db
        self.user = user
        self.auth = auth
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setFixedSize(1125, 942)
        self.setStyleSheet("background-color: #fff;")


        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setFixedSize(1125, 942)
        self.centralwidget.setObjectName("centralwidget")

        self.navigate = QtWidgets.QLabel(self.centralwidget)
        self.navigate.setGeometry(QtCore.QRect(70, 0, 1056, 51))
        self.navigate.setText("")
        self.navigate.setObjectName("navigate")
        self.navigate.setStyleSheet("background-color:rgb(240, 240, 240);")

        self.user_info_button = QtWidgets.QPushButton(self.centralwidget)
        self.user_info_button.setGeometry(QtCore.QRect(1081, 0, 41, 50))
        self.user_info_button.setBaseSize(QtCore.QSize(0, 0))
        self.user_info_button.setStyleSheet("border: 0px;")
        self.user_info_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon/user_out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.user_info_button.setIcon(icon)
        self.user_info_button.setIconSize(QtCore.QSize(46, 25))
        self.user_info_button.setObjectName("user_info_button")
        self.user_info_button.setStyleSheet('border: 0px; background-color:rgb(240, 240, 240);')
        self.user_info_button.clicked.connect(self.open_user_info_page)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(218, 0, 771, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayoutWidget.setStyleSheet('background-color:rgb(240, 240, 240);')

        self.search_edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.search_edit.setMinimumSize(QtCore.QSize(61, 28))
        self.search_edit.setObjectName("search_edit")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.search_edit.setFont(font)
        self.search_edit.setStyleSheet('background-color:rgb(213, 213, 213); border:0px;')
        self.search_edit.setPlaceholderText("Фамилия Имя Отчество")
        self.search_edit.textChanged.connect(self.search_text)
        self.search_edit.setPlaceholderText("")
        self.horizontalLayout.addWidget(self.search_edit)

        self.search_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.search_button.setMinimumSize(QtCore.QSize(50, 30))
        self.search_button.setStyleSheet("border: 0px;")
        self.search_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icon/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon1)
        self.search_button.setCheckable(False)
        self.search_button.setAutoRepeat(False)
        self.search_button.setAutoExclusive(False)
        self.search_button.setObjectName("search_button")
        self.search_button.setIconSize(QtCore.QSize(20, 20))

        self.horizontalLayout.addWidget(self.search_button)

        self.sidebar = QtWidgets.QLabel(self.centralwidget)
        self.sidebar.setGeometry(QtCore.QRect(0, 0, 71, 951))
        self.sidebar.setToolTipDuration(-1)
        self.sidebar.setAutoFillBackground(False)
        self.sidebar.setStyleSheet("background-color:rgb(37, 39, 72);")
        self.sidebar.setText("")
        self.sidebar.setIndent(2)
        self.sidebar.setObjectName("sidebar")

        self.logo = QtWidgets.QPushButton(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(0, 0, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.logo.setFont(font)
        self.logo.setStyleSheet("background-color:rgb(37, 39, 72); border:0px;")
        self.logo.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logo.setIcon(icon2)
        self.logo.setIconSize(QtCore.QSize(75, 75))
        self.logo.setObjectName("logo")

        self.home_button = QtWidgets.QPushButton(self.centralwidget)
        self.home_button.setGeometry(QtCore.QRect(0, 70, 71, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_button.sizePolicy().hasHeightForWidth())
        self.home_button.setSizePolicy(sizePolicy)
        self.home_button.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.home_button.setFont(font)
        self.home_button.setAcceptDrops(False)
        self.home_button.setToolTipDuration(-1)
        self.home_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.home_button.setStyleSheet("background-color:rgb(37, 39, 72); border: 0px;\n"
                                       "")
        self.home_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/icon/home_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_button.setIcon(icon3)
        self.home_button.setIconSize(QtCore.QSize(25, 25))
        self.home_button.setCheckable(True)
        self.home_button.setChecked(False)
        self.home_button.setObjectName("home_button")
        self.home_button.clicked.connect(self.open_home_page)

        self.calculation_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculation_button.setGeometry(QtCore.QRect(0, 120, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.calculation_button.setFont(font)
        self.calculation_button.setStyleSheet("background-color:rgb(37, 39, 72); border: 0px; color: rgb(104, 116, 124);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/icon/pencil_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calculation_button.setIcon(icon4)
        self.calculation_button.setIconSize(QtCore.QSize(25, 25))
        self.calculation_button.setAutoRepeatDelay(300)
        self.calculation_button.setAutoRepeatInterval(100)
        self.calculation_button.setObjectName("calculation_button")
        self.calculation_button.clicked.connect(self.open_calculation_button)

        self.users_button = QtWidgets.QPushButton(self.centralwidget)
        self.users_button.setGeometry(QtCore.QRect(0, 170, 71, 51))
        self.users_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.users_button.setFont(font)
        self.users_button.setStyleSheet("background-color:rgb(37, 39, 72); border: 0px;")
        self.users_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/icon/users_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.users_button.setIcon(icon5)
        self.users_button.setIconSize(QtCore.QSize(25, 25))
        self.users_button.setAutoRepeatDelay(300)
        self.users_button.setAutoRepeatInterval(100)
        self.users_button.setObjectName("users_button")
        self.users_button.clicked.connect(self.open_users_page)

        self.settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.settings_button.setGeometry(QtCore.QRect(0, 270, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.settings_button.setFont(font)
        self.settings_button.setStyleSheet(
            "background-color:rgb(37, 39, 72); border: 0px;  color: rgb(104, 116, 124); padding-left: 0px;")
        self.settings_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/icon/setting_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_button.setIcon(icon6)
        self.settings_button.setIconSize(QtCore.QSize(25, 25))
        self.settings_button.setObjectName("settings_button")
        self.settings_button.clicked.connect(self.open_settings_page)

        self.add_user_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_user_button.setGeometry(QtCore.QRect(0, 220, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.add_user_button.setFont(font)
        self.add_user_button.setStyleSheet("background-color:rgb(37, 39, 72); border: 0px; padding-left: 5px;\n"
                                           "")
        self.add_user_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/icon/add_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_user_button.setIcon(icon7)
        self.add_user_button.setIconSize(QtCore.QSize(25, 25))
        self.add_user_button.setObjectName("add_user_button")
        if self.user.posts != 'Технолог':
            self.add_user_button.setEnabled(False)
            self.users_button.setEnabled(False)
            self.settings_button.setEnabled(False)
        self.add_user_button.clicked.connect(self.open_add_user_page)

        self.burger_button = QtWidgets.QPushButton(self.centralwidget)
        self.burger_button.setGeometry(QtCore.QRect(72, 2, 51, 48))
        self.burger_button.setStyleSheet("border: 0px;")
        self.burger_button.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/icon/burger.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.burger_button.setIcon(icon8)
        self.burger_button.setIconSize(QtCore.QSize(25, 55))
        self.burger_button.setObjectName("burger_button")
        self.burger_button.setCheckable(True)
        self.burger_button.clicked.connect(self.open_sidebar)
        self.burger_button.setStyleSheet('border: 0px; background-color:rgb(240, 240, 240);')

        self.exit_user_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_user_button.setGeometry(QtCore.QRect(0, 860, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.exit_user_button.setFont(font)
        self.exit_user_button.setStyleSheet(
            "background-color:rgb(37, 39, 72); border: 0px;  color: rgb(104, 116, 124); padding-left: 1px")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/icon/exit_out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_user_button.setIcon(icon9)
        self.exit_user_button.setIconSize(QtCore.QSize(25, 25))
        self.exit_user_button.setObjectName("exit_user_button")
        self.exit_user_button.clicked.connect(self.exit_user)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(76, 59, 1051, 881))
        self.stackedWidget.setObjectName("stackedWidget")

        self.settings_page = SettingsPage(self)
        self.settings_page.setObjectName("setObjectName")
        self.stackedWidget.addWidget(self.settings_page)

        self.home_page = HomePage(self, self.search_edit, self.settings_page.read_file())
        self.home_page.setObjectName("home_page")
        self.stackedWidget.addWidget(self.home_page)
        self.search_edit.setPlaceholderText("Название файла")

        self.user_info_page = UserInfoPage(self.db, self.user, self)
        self.user_info_page.setObjectName("user_info_page")
        self.stackedWidget.addWidget(self.user_info_page)

        self.add_user_page = RegistrationUserPage(self.db, self)
        self.add_user_page.setObjectName("add_user_page")
        self.stackedWidget.addWidget(self.add_user_page)

        self.users_page = UsersPage(self.db, self.search_edit, self)
        self.users_page.setObjectName("users_page")
        self.stackedWidget.addWidget(self.users_page)

        self.calculation_page = CalculationPage(self)
        self.calculation_page.setObjectName("calculation_page")
        self.stackedWidget.addWidget(self.calculation_page)

        self.user_info_button.installEventFilter(self)
        self.home_button.installEventFilter(self)
        self.calculation_button.installEventFilter(self)
        self.users_button.installEventFilter(self)
        self.add_user_button.installEventFilter(self)
        self.settings_button.installEventFilter(self)
        self.exit_user_button.installEventFilter(self)

        self.retranslateUi()
        self.stackedWidget.setCurrentWidget(self.home_page)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle("MainWindow")

    def closeEvent(self, event):
        self.db.disconnection_database()
        event.accept()

    def open_home_page(self):
        self.search_edit.clear()
        self.home_page = HomePage(self, self.search_edit, self.settings_page.read_file())
        self.stackedWidget.addWidget(self.home_page)
        self.stackedWidget.setCurrentWidget(self.home_page)
        self.search_edit.setEnabled(True)
        self.search_edit.setPlaceholderText("Название файла")

    def open_calculation_button(self):
        self.calculation_page = CalculationPage(self)
        self.calculation_page.setObjectName("calculation_page")
        self.search_edit.setEnabled(False)
        self.stackedWidget.addWidget(self.calculation_page)
        self.stackedWidget.setCurrentWidget(self.calculation_page)

    def open_users_page(self):
        self.search_edit.clear()
        self.users_page = UsersPage(self.db, self.search_edit, self)
        self.stackedWidget.addWidget(self.users_page)
        self.stackedWidget.setCurrentWidget(self.users_page)
        self.search_edit.setEnabled(True)
        self.search_edit.setPlaceholderText("Фамилия Имя Отчество")

    def open_add_user_page(self):
        self.add_user_page = RegistrationUserPage(self.db, self)
        self.stackedWidget.addWidget(self.add_user_page)
        self.stackedWidget.setCurrentWidget(self.add_user_page)
        self.search_edit.setEnabled(False)
        self.search_edit.setPlaceholderText("")

    def open_user_info_page(self):
        self.user_info_page = UserInfoPage(self.db, self.user, self)
        self.stackedWidget.addWidget(self.user_info_page)
        self.stackedWidget.setCurrentWidget(self.user_info_page)
        self.search_edit.setEnabled(False)
        self.search_edit.setPlaceholderText("")

    def open_settings_page(self):
        self.settings_page = SettingsPage(self)
        self.stackedWidget.addWidget(self.settings_page)
        self.stackedWidget.setCurrentWidget(self.settings_page)
        self.search_edit.setEnabled(False)
        self.search_edit.setPlaceholderText("")

    def search_text(self):
        if not self.search_edit.text():
            self.search_edit.setStyleSheet('background-color:rgb(213, 213, 213); border: 0px;')
        else:
            self.search_edit.setStyleSheet('background-color:rgb(108, 108, 255); border: 0px;')

    def eventFilter(self, watched, event):
        icon = QtGui.QIcon()
        if (event.type() == QtCore.QEvent.Enter) and (watched == self.home_button):
            icon.addPixmap(QtGui.QPixmap("images/icon/home_out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.home_button.setIcon(icon)
            if self.burger_button.isChecked():
                self.home_button.setStyleSheet(
                    "background-color:rgb(75, 80, 147); border: 0px; padding-right: 22px; color:rgb(246, 246, 247);")
            else:
                self.home_button.setStyleSheet(
                    "background-color:rgb(75, 80, 147); border: 0px; color:rgb(246, 246, 247);")
        elif (event.type() == QtCore.QEvent.Leave) and (watched == self.home_button):
            icon.addPixmap(QtGui.QPixmap("images/icon/home_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.home_button.setIcon(icon)
            if self.burger_button.isChecked():
                self.home_button.setStyleSheet(
                    "background-color:rgb(37, 39, 72); border: 0px; padding-right: 22px; color:rgb(104, 116, 124);")
            else:
                self.home_button.setStyleSheet(
                    "background-color:rgb(37, 39, 72); border: 0px; color:rgb(104, 116, 124);")

        elif (event.type() == QtCore.QEvent.Enter) and (watched == self.calculation_button):
            icon.addPixmap(QtGui.QPixmap("images/icon/pencil_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.calculation_button.setIcon(icon)
            if self.burger_button.isChecked():
                self.calculation_button.setStyleSheet(
                    "background-color:rgb(75, 80, 147); border: 0px; padding-right: 10px; color:rgb(246, 246, 247);")
            else:
                self.calculation_button.setStyleSheet(
                    "background-color:rgb(75, 80, 147); border: 0px; color: rgb(104, 116, 124);")
        elif (event.type() == QtCore.QEvent.Leave) and (watched == self.calculation_button):
            icon.addPixmap(QtGui.QPixmap("images/icon/pencil_out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.calculation_button.setIcon(icon)
            if self.burger_button.isChecked():
                self.calculation_button.setStyleSheet(
                    "background-color:rgb(37, 39, 72); border: 0px; padding-right: 10px; color:rgb(104, 116, 124);")
            else:
                self.calculation_button.setStyleSheet(
                    "background-color:rgb(37, 39, 72); border: 0px; color: rgb(104, 116, 124);")

        elif (event.type() == QtCore.QEvent.Enter) and (watched == self.user_info_button):
            icon.addPixmap(QtGui.QPixmap("images/icon/user_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.user_info_button.setIcon(icon)

        elif (event.type() == QtCore.QEvent.Leave) and (watched == self.user_info_button):
            icon.addPixmap(QtGui.QPixmap("images/icon/user_out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.user_info_button.setIcon(icon)

        elif (event.type() == QtCore.QEvent.Enter) and (watched == self.exit_user_button):
            icon.addPixmap(QtGui.QPixmap("images/icon/exit_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.exit_user_button.setIcon(icon)
            if self.burger_button.isChecked():
                self.exit_user_button.setStyleSheet(
                    "background-color:rgb(75, 80, 147); border: 0px; padding-right: 85px; color:rgb(246, 246, 247);")
            else:
                self.exit_user_button.setStyleSheet(
                    "background-color:rgb(75, 80, 147); border: 0px;  color: rgb(104, 116, 124); padding-left: 1px")

        elif (event.type() == QtCore.QEvent.Leave) and (watched == self.exit_user_button):
            icon.addPixmap(QtGui.QPixmap("images/icon/exit_out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.exit_user_button.setIcon(icon)
            if self.burger_button.isChecked():
                self.exit_user_button.setStyleSheet(
                    "background-color:rgb(37, 39, 72); border: 0px; padding-right: 85px; color: rgb(104, 116, 124);")
            else:
                self.exit_user_button.setStyleSheet(
                    "background-color:rgb(37, 39, 72); border: 0px;  color: rgb(104, 116, 124); padding-left: 1px")

        elif self.user.posts == 'Технолог':
            if (event.type() == QtCore.QEvent.Enter) and (watched == self.users_button):
                icon.addPixmap(QtGui.QPixmap("images/icon/users_out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.users_button.setIcon(icon)
                if self.burger_button.isChecked():
                    self.users_button.setStyleSheet(
                        "background-color:rgb(75, 80, 147); border: 0px; padding-right: 43px; color: rgb(246, 246, 247);")
                else:
                    self.users_button.setStyleSheet(
                        "background-color:rgb(75, 80, 147); border: 0px; color: rgb(246, 246, 247);")

            elif (event.type() == QtCore.QEvent.Leave) and (watched == self.users_button):
                icon.addPixmap(QtGui.QPixmap("images/icon/users_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.users_button.setIcon(icon)
                if self.burger_button.isChecked():
                    self.users_button.setStyleSheet(
                        "background-color:rgb(37, 39, 72); border: 0px; padding-right: 43px; color: rgb(104, 116, 124);")
                else:
                    self.users_button.setStyleSheet(
                        "background-color:rgb(37, 39, 72); border: 0px; color: rgb(104, 116, 124);")

            elif (event.type() == QtCore.QEvent.Enter) and (watched == self.add_user_button):
                icon.addPixmap(QtGui.QPixmap("images/icon/add_out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.add_user_button.setIcon(icon)
                if self.burger_button.isChecked():
                    self.add_user_button.setStyleSheet(
                        "background-color:rgb(75, 80, 147); border: 0px; padding-right: -14px; color: rgb(246, 246, 247);")
                else:
                    self.add_user_button.setStyleSheet(
                        "background-color:rgb(75, 80, 147); border: 0px; padding-left: 6px; color:rgb(246, 246, 247)")

            elif (event.type() == QtCore.QEvent.Leave) and (watched == self.add_user_button):
                icon.addPixmap(QtGui.QPixmap("images/icon/add_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.add_user_button.setIcon(icon)
                if self.burger_button.isChecked():
                    self.add_user_button.setStyleSheet(
                        "background-color:rgb(37, 39, 72); border: 0px; padding-right: -14px; color: rgb(104, 116, 124);")
                else:
                    self.add_user_button.setStyleSheet(
                        "background-color:rgb(37, 39, 72); border: 0px; padding-left: 6px;\n")

            elif (event.type() == QtCore.QEvent.Enter) and (watched == self.settings_button):
                icon.addPixmap(QtGui.QPixmap("images/icon/setting_out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.settings_button.setIcon(icon)
                if self.burger_button.isChecked():
                    self.settings_button.setStyleSheet(
                        "background-color:rgb(75, 80, 147); border: 0px; padding-right: 60px; color:rgb(246, 246, 247);")
                else:
                    self.settings_button.setStyleSheet(
                        "background-color:rgb(75, 80, 147); border: 0px;  color: rgb(104, 116, 124); padding-left: 0px;")

            elif (event.type() == QtCore.QEvent.Leave) and (watched == self.settings_button):
                icon.addPixmap(QtGui.QPixmap("images/icon/setting_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.settings_button.setIcon(icon)
                if self.burger_button.isChecked():
                    self.settings_button.setStyleSheet(
                        "background-color:rgb(37, 39, 72); border: 0px; padding-right: 60px; color: rgb(104, 116, 124);")
                else:
                    self.settings_button.setStyleSheet(
                        "background-color:rgb(37, 39, 72); border: 0px; padding-left: 0px;\n")

        return super().eventFilter(watched, event)

    def exit_user(self):
        self.auth.show()
        self.close()

    def open_sidebar(self):

        if self.burger_button.isChecked():
            icon = QtGui.QIcon()

            self.navigate.setGeometry(QtCore.QRect(220, 0, 906, 51))

            self.burger_button.setGeometry(QtCore.QRect(221, 2, 51, 48))
            icon.addPixmap(QtGui.QPixmap("images/icon/burger.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.burger_button.setIcon(icon)
            self.burger_button.setIconSize(QtCore.QSize(25, 55))

            self.horizontalLayoutWidget.setGeometry(QtCore.QRect(358, 0, 631, 51))

            self.sidebar.setGeometry(QtCore.QRect(0, 0, 221, 951))
            self.sidebar.setStyleSheet("background-color:rgb(37, 39, 72);")

            self.logo.setGeometry(QtCore.QRect(0, 0, 221, 61))
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.logo.setFont(font)
            self.logo.setStyleSheet("background-color:rgb(37, 39, 72); border:0px; padding-right: 50px; color: #fff;")
            self.logo.setText("TechMap")
            icon.addPixmap(QtGui.QPixmap("images/icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.logo.setIcon(icon)
            self.logo.setIconSize(QtCore.QSize(75, 75))

            icon = QtGui.QIcon()
            self.home_button.setGeometry(QtCore.QRect(0, 70, 221, 51))
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(10)
            font.setBold(True)
            font.setItalic(False)
            font.setWeight(75)
            self.home_button.setText('   Главная страница')
            self.home_button.setFont(font)
            self.home_button.setAcceptDrops(False)
            self.home_button.setToolTipDuration(-1)
            self.home_button.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.home_button.setStyleSheet(
                "background-color:rgb(37, 39, 72); border: 0px; padding-right: 22px; color:rgb(104, 116, 124);\n"
                "")
            icon.addPixmap(QtGui.QPixmap("images/icon/home_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.home_button.setIcon(icon)
            self.home_button.setIconSize(QtCore.QSize(25, 25))

            self.calculation_button.setGeometry(QtCore.QRect(0, 120, 221, 51))
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            font.setStyleStrategy(QtGui.QFont.PreferDefault)
            self.calculation_button.setFont(font)
            self.calculation_button.setStyleSheet(
                "background-color:rgb(37, 39, 72); border: 0px; padding-right: 10px; color: rgb(104, 116, 124);")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/icon/pencil_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.calculation_button.setIcon(icon)
            self.calculation_button.setIconSize(QtCore.QSize(25, 25))
            self.calculation_button.setAutoRepeatDelay(300)
            self.calculation_button.setAutoRepeatInterval(100)
            self.calculation_button.setText("  Маршрут волочения")
            self.calculation_button.setObjectName("calculation_button")

            self.users_button.setGeometry(QtCore.QRect(0, 170, 221, 51))
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.users_button.setText('   Пользователи')
            self.users_button.setFont(font)
            self.users_button.setStyleSheet(
                "background-color:rgb(37, 39, 72); border: 0px; padding-right: 44px; color: rgb(104, 116, 124);")
            icon.addPixmap(QtGui.QPixmap("images/icon/users_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.users_button.setIcon(icon)
            self.users_button.setIconSize(QtCore.QSize(25, 25))

            self.add_user_button.setGeometry(QtCore.QRect(0, 220, 221, 51))
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.add_user_button.setText('  Добавить пользователя')
            self.add_user_button.setFont(font)
            self.add_user_button.setStyleSheet(
                "background-color:rgb(37, 39, 72); border: 0px; padding-right: -14px; color: rgb(104, 116, 124);")
            icon.addPixmap(QtGui.QPixmap("images/icon/add_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.add_user_button.setIcon(icon)
            self.add_user_button.setIconSize(QtCore.QSize(25, 25))

            self.exit_user_button.setGeometry(QtCore.QRect(0, 860, 221, 51))
            self.exit_user_button.setText("   Выйти")
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.exit_user_button.setFont(font)
            self.exit_user_button.setStyleSheet(
                "background-color:rgb(37, 39, 72); border: 0px; padding-right: 85px; color: rgb(104, 116, 124);")
            icon7 = QtGui.QIcon()
            icon7.addPixmap(QtGui.QPixmap("images/icon/exit_out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.exit_user_button.setIcon(icon7)
            self.exit_user_button.setIconSize(QtCore.QSize(25, 25))
            self.exit_user_button.setObjectName("exit_user_button")

            self.settings_button.setGeometry(QtCore.QRect(0, 270, 221, 51))
            self.settings_button.setStyleSheet(
                "background-color:rgb(37, 39, 72); border: 0px; padding-right: 60px; color: rgb(104, 116, 124);")
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.settings_button.setFont(font)
            self.settings_button.setText("   Настройки")

            self.stackedWidget.setGeometry(QtCore.QRect(221, 59, 906, 881))
            self.user_info_page.open_sidebar()
            self.add_user_page.open_sidebar()
            self.users_page.open_sidebar()
            self.home_page.open_sidebar()
            self.settings_page.open_sidebar()
            self.calculation_page.open_sidebar()

        else:
            self.logo.setText("")
            self.home_button.setText("")
            self.calculation_button.setText("")
            self.users_button.setText("")
            self.add_user_button.setText("")
            self.exit_user_button.setText("")
            self.settings_button.setText("")

            self.navigate.setGeometry(QtCore.QRect(70, 0, 1056, 51))
            self.user_info_button.setGeometry(QtCore.QRect(1081, 0, 41, 50))
            self.horizontalLayoutWidget.setGeometry(QtCore.QRect(218, 0, 771, 51))
            self.sidebar.setGeometry(QtCore.QRect(0, 0, 71, 951))
            self.logo.setGeometry(QtCore.QRect(0, 0, 71, 61))
            self.home_button.setGeometry(QtCore.QRect(0, 70, 71, 51))
            self.calculation_button.setGeometry(QtCore.QRect(0, 120, 71, 51))
            self.calculation_button.setStyleSheet("background-color:rgb(37, 39, 72); border: 0px; color: rgb(104, 116, 124);")
            self.users_button.setGeometry(QtCore.QRect(0, 170, 71, 51))
            self.add_user_button.setGeometry(QtCore.QRect(0, 220, 71, 51))
            self.burger_button.setGeometry(QtCore.QRect(72, 2, 51, 48))
            self.exit_user_button.setGeometry(QtCore.QRect(0, 860, 71, 51))
            self.exit_user_button.setStyleSheet(
                "background-color:rgb(37, 39, 72); border: 0px;  color: rgb(104, 116, 124); padding-left: 1px")
            self.settings_button.setGeometry(QtCore.QRect(0, 270, 71, 51))
            self.settings_button.setStyleSheet(
                "background-color:rgb(37, 39, 72); border: 0px;  color: rgb(104, 116, 124); padding-left: 0px;")
            self.stackedWidget.setGeometry(QtCore.QRect(76, 59, 1051, 881))
            self.user_info_page.close_sidebar()
            self.add_user_page.close_sidebar()
            self.users_page.close_sidebar()
            self.home_page.close_sidebar()
            self.settings_page.close_sidebar()
            self.calculation_page.close_sidebar()


            self.logo.setStyleSheet("background-color:rgb(37, 39, 72); border:0px;")
            self.home_button.setStyleSheet("background-color:rgb(37, 39, 72); border: 0px;")
            self.users_button.setStyleSheet("background-color:rgb(37, 39, 72); border: 0px;")
            self.add_user_button.setStyleSheet("background-color:rgb(37, 39, 72); border: 0px; padding-left: 5px;\n")
