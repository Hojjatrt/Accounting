import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from GUI.UI_Files.add_product import Ui_Dialog_add
from GUI.UI_Files.main_window import Ui_MainWindow
from database.Database import Database
from Models.Accounting import Accounting


class AddDialog(QDialog):
    def __init__(self, mainWindow):
        super(QDialog, self).__init__()

        # Define the instance to access the the UI elements defined in
        self.mainWindow = mainWindow
        self._add_dialog = Ui_Dialog_add()
        self._add_dialog.setupUi(self)
        self._add_dialog.retranslateUi(self)
        self.dialog = QMainWindow()
        # Initialize some other variables.
        #

        # Connect button with methods.
        self._connect()

    def _connect(self):
        self._add_dialog.btn_add_cancel.clicked.connect(self.exit)
        self._add_dialog.btn_add_save.clicked.connect(self.add_product)
        self._add_dialog.txt_purchase_price.textChanged.connect(self.txt_pprice_change)
        self._add_dialog.txt_sales_price.textChanged.connect(self.txt_sprice_change)

    def txt_pprice_change(self):
        p_price = self._add_dialog.txt_purchase_price.text()
        if not p_price.isnumeric():
            self._add_dialog.txt_purchase_price.setText(p_price[:len(p_price)-1])

    def txt_sprice_change(self):
        s_price = self._add_dialog.txt_sales_price.text()
        if not s_price.isnumeric():
            self._add_dialog.txt_sales_price.setText(s_price[:len(s_price)-1])

    def add_product(self):
        global db
        name = self._add_dialog.txt_product_name.text()
        if name == '':
            QMessageBox.information(self, 'خطا', "نام محصول باید وارد شود!",
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        p_price = self._add_dialog.txt_purchase_price.text()
        if p_price == '':
            QMessageBox.question(self.dialog, 'خطا', " قیمت خرید محصول باید وارد شود!",
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        s_price = self._add_dialog.txt_sales_price.text()
        if s_price == '':
            QMessageBox.question(self.dialog, 'خطا', "قیمت فروش محصول باید وارد شود!",
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        p_price = int(p_price)
        s_price = int(s_price)
        if p_price > s_price:
            QMessageBox.question(self.dialog, 'خطا', "قیمت خرید نباید بیشتر از قیمت فروش باشد!",
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        print('here is')
        acc = Accounting(name, p_price, s_price)
        print('here is 2')
        acc.insert(db)
        print('here is 3')
        QMessageBox.information(self.dialog, 'افزودن', "محصول با موفقیت افزوده شد!",
                             QMessageBox.Ok, QMessageBox.Ok)

        self._add_dialog.txt_product_name.text('')
        self._add_dialog.txt_sales_price.text('')
        self._add_dialog.txt_purchase_price.text('')
        self._add_dialog.txt_product_name.setFocus()

    # method exit
    def exit(self):
        self.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Define the instance to access the the UI elements defined in
        self._window = Ui_MainWindow()
        self._window.setupUi(self)
        self._window.retranslateUi(self)
        self._add_dialog = AddDialog(self._window)

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

        self.search()

    def _connect(self):
        self._window.txt_main_search_name.textChanged.connect(self.search)
        self._window.menu_exit.triggered.connect(self.exit)
        self._window.btn_main_exit.clicked.connect(self.exit)
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
