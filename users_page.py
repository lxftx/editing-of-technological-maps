import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QAbstractItemView

from alert import AlertMessage


class UsersPage(QWidget, AlertMessage):
    def __init__(self, db, search_widget, main):
        super().__init__()

        self.users_page = self
        self.db = db
        self.main = main

        self.setWindowIcon(QtGui.QIcon(self.get_path('images/icon', 'logo.png')))
        self.search_widget = search_widget
        self.search_widget.clear()
        self.search_widget.textChanged.connect(self.search_users)

        self.content_users = QtWidgets.QLabel(self.users_page)
        self.content_users.setGeometry(QtCore.QRect(10, 10, 1021, 861))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.content_users.setFont(font)
        self.content_users.setStyleSheet("background-color:rgb(240, 240, 240);\n"
                                             "border-radius: 30px;\n"
                                             "color: rgb(255, 255, 17);")
        self.content_users.setText("")
        self.content_users.setObjectName("content_users")

        self.table_users = QtWidgets.QTableWidget(self.users_page)
        self.table_users.setEnabled(True)
        self.table_users.setGeometry(QtCore.QRect(20, 50, 1001, 751))
        self.table_users.setTabletTracking(False)
        self.table_users.setObjectName("table_users")
        self.table_users.setColumnCount(6)  # Увеличиваем количество столбцов на 1
        self.table_users.setRowCount(0)
        self.table_users.setHorizontalHeaderLabels(["Имя", "Фамилия", "Отчество", "Должность", "Почта", "Действие"])
        self.table_users.setEditTriggers(QAbstractItemView.NoEditTriggers)

        header = self.table_users.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.delete_user = QtWidgets.QPushButton(self.users_page)
        self.delete_user.setGeometry(QtCore.QRect(304, 822, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.delete_user.setFont(font)
        self.delete_user.setText('Удалить')
        self.delete_user.setStyleSheet("border-radius: 10px;")
        self.delete_user.setObjectName("delete_user")
        self.delete_user.clicked.connect(self.push_delete_button)
        self.populate_table()


        if self.main.burger_button.isChecked():
            self.open_sidebar()

    def closeEvent(self, event):
        event.accept()

    def get_path(self, dir, name):
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), dir, name)

    def search_users(self):
        if self.search_widget.text():
            ifo = ['' for _ in range(3)]
            list_ifo = self.search_widget.text().split()
            for i, value in enumerate(list_ifo):
                ifo[i] = value
            if os.path.exists(self.get_path(r'config', "db_config.bin")):
                self.db.connect_database('postgres', user=self.main.path[0], password=self.main.path[1],
                                         host=self.main.path[2], port=self.main.path[3],
                                         database=self.main.path[4])
                table_name = self.main.path[5]
            else:
                self.db.connect_database('sqlite', self.main.path[0])
                table_name = self.main.path[1]

            request = """SELECT first_name, last_name, patronymic, post, email FROM {} WHERE email<>'{}' AND last_name LIKE '{}%' AND first_name LIKE '{}%' AND patronymic LIKE '{}%'""".format(
                table_name, self.main.user.email, *ifo)
            self.db.cursor.execute(request)
            data = self.db.cursor.fetchall()
            self.table_users.setRowCount(len(data))

            for i, row_data in enumerate(data):
                for j, value in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    self.table_users.setItem(i, j, item)
                    if item:
                        item.setFlags(item.flags() & ~Qt.ItemIsEditable)

                checkbox = QtWidgets.QCheckBox(self.table_users)
                checkbox.setChecked(False)
                checkbox.setStyleSheet("QCheckBox { margin-left: 35%; }")  # Пользовательский стиль для чекбокса
                self.table_users.setCellWidget(i, 5, checkbox)
            self.db.disconnection_database()
        else:
            self.populate_table()

    def populate_table(self):
        if os.path.exists(self.get_path(r'config', "db_config.bin")):
            self.db.connect_database('postgres', user=self.main.path[0], password=self.main.path[1], host=self.main.path[2], port=self.main.path[3],
                                     database=self.main.path[4])
            self.db.cursor.execute(
                f"""SELECT first_name, last_name, patronymic, post, email FROM {self.main.path[5]} WHERE email <> %s""", (self.main.user.email,))
        else:
            self.db.connect_database('sqlite', self.main.path[0])
            self.db.cursor.execute(
                f"""SELECT first_name, last_name, patronymic, post, email FROM {self.main.path[1]} WHERE email <> ?""",
                (self.main.user.email,))
        data = self.db.cursor.fetchall()
        self.table_users.setRowCount(len(data))
        self.db.disconnection_database()

        for i, row_data in enumerate(data):
            for j, value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.table_users.setItem(i, j, item)

            # Добавляем чекбокс в последний столбец для каждой строки
            checkbox = QtWidgets.QCheckBox(self.table_users)
            checkbox.setChecked(False)
            checkbox.setStyleSheet("QCheckBox { margin-left: 35%; }")  # Пользовательский стиль для чекбокса
            self.table_users.setCellWidget(i, 5, checkbox)  # Устанавливаем чекбокс в ячейку

    def push_delete_button(self):
        rows_to_delete = []
        for row in range(self.table_users.rowCount()):
            checkbox = self.table_users.cellWidget(row, 5)  # Получаем чекбокс в текущей строке
            if checkbox.isChecked():  # Проверяем, выбран ли чекбокс
                rows_to_delete.append((row, self.table_users.item(row, 4).text()))  # Добавляем индекс строки в список для удаления
        for row in reversed(rows_to_delete):
            self.table_users.removeRow(row[0])
            if os.path.exists(self.get_path(r'config', "db_config.bin")):
                self.db.connect_database('postgres', user=self.main.path[0], password=self.main.path[1],
                                         host=self.main.path[2], port=self.main.path[3],
                                         database=self.main.path[4])
                self.db.cursor.execute(f"""DELETE FROM {self.main.path[5]} WHERE email = %s""",
                                   (row[1],))
            else:
                self.db.connect_database('sqlite', self.main.path[0])
                self.db.cursor.execute(f"""DELETE FROM {self.main.path[1]} WHERE email = ?""",
                                   (row[1],))
            self.db.connection.commit()
            self.db.disconnection_database()


    def open_sidebar(self):
        self.content_users.setGeometry(QtCore.QRect(10, 10, 881, 861))
        self.table_users.setGeometry(QtCore.QRect(20, 50, 861, 751))
        self.delete_user.setGeometry(QtCore.QRect(220, 822, 431, 31))

    def close_sidebar(self):
        self.content_users.setGeometry(QtCore.QRect(10, 10, 1021, 861))
        self.table_users.setGeometry(QtCore.QRect(20, 50, 1001, 751))
        self.delete_user.setGeometry(QtCore.QRect(304, 822, 431, 31))