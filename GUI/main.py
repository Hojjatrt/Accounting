import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from GUI.UI_Files.add_product import Ui_Dialog_add
from GUI.UI_Files.main_window import Ui_MainWindow
from database.Database import Database


class AddDialog(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()

        # Define the instance to access the the UI elements defined in
        self._add_dialog = Ui_Dialog_add()
        self._add_dialog.setupUi(self)
        self._add_dialog.retranslateUi(self)

        # Initialize some other variables.
        #

        # Connect button with methods.
        self._connect()

    def _connect(self):
        # self._window.menu_exit.clicked.connect(self.exit)
        # self._window.menu_add.clicked.connect(self.Rotate)
        pass
    # method exit
    def exit(self):
        sys.exit()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Define the instance to access the the UI elements defined in
        self._window = Ui_MainWindow()
        self._window.setupUi(self)
        self._window.retranslateUi(self)
        self._add_dialog = AddDialog()

        # Initialize some other variables.
        self.table_rows = self._window.tableWidget.rowCount()
        header = self._window.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

        # Connect button with methods.
        self._connect()

    def _connect(self):
        self._window.txt_main_search_name.textChanged.connect(self.search)
        self._window.menu_exit.triggered.connect(self.exit)
        self._window.menu_add.triggered.connect(self.show_add_dialog)

    def displayTime(self):
        self._window.lbl_datetime.setText(QtCore.QDateTime.currentDateTime().toString('hh:mm:ss'))

    def search(self):
        self._window.tableWidget.setRowCount(0)
        global db
        text = self._window.txt_main_search_name.text()
        print(text)
        if text == '':
            data = db.select()
            print(data)
            for d in data:
                self.table_rows = self._window.tableWidget.rowCount()
                self._window.tableWidget.insertRow(self.table_rows)
                self._window.tableWidget.setItem(self.table_rows, 0, QTableWidgetItem(d[1]))
                self._window.tableWidget.setItem(self.table_rows, 1, QTableWidgetItem(str(d[2])))
                self._window.tableWidget.setItem(self.table_rows, 2, QTableWidgetItem(str(d[3])))

        else:
            data = db.select(text)
            print(data)
            for d in data:
                self.table_rows = self._window.tableWidget.rowCount()
                self._window.tableWidget.insertRow(self.table_rows)
                self._window.tableWidget.setItem(self.table_rows, 0, QTableWidgetItem(d[1]))
                self._window.tableWidget.setItem(self.table_rows, 1, QTableWidgetItem(str(d[2])))
                self._window.tableWidget.setItem(self.table_rows, 2, QTableWidgetItem(str(d[3])))

    def show_add_dialog(self):
        self._add_dialog.show()

    # method exit
    def exit(self):
        sys.exit()


db = Database()
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
