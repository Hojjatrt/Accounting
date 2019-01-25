import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from GUI.UI_Files.add_product import Ui_Dialog_add
from GUI.UI_Files.update_product import Ui_update_dialog
from GUI.UI_Files.main_window import Ui_MainWindow
from database.Database import Database
from Models.Models import Product


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
        self._add_dialog.btn_add_cancel.clicked.connect(self.exit)
        self._add_dialog.btn_add_save.clicked.connect(self.add_product)
        self._add_dialog.txt_purchase_price.textChanged.connect(self.txt_pprice_change)
        self._add_dialog.txt_sales_percent.textChanged.connect(self.txt_percent_change)

    def txt_pprice_change(self):
        p_price = self._add_dialog.txt_purchase_price.text()
        if not p_price.isnumeric():
            self._add_dialog.txt_purchase_price.setText(p_price[:len(p_price)-1])

    def txt_percent_change(self):
        percent = self._add_dialog.txt_sales_percent.text()
        if not percent.isnumeric():
            self._add_dialog.txt_sales_percent.setText(percent[:len(percent)-1])

    def add_product(self):
        global db
        name = self._add_dialog.txt_product_name.text()
        if name == '':
            QMessageBox.information(self, 'خطا', "نام محصول باید وارد شود!",
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        p_price = self._add_dialog.txt_purchase_price.text()
        if p_price == '':
            QMessageBox.information(self, 'خطا', " قیمت خرید محصول باید وارد شود!",
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        percent = self._add_dialog.txt_sales_percent.text()
        if percent == '':
            QMessageBox.information(self, 'خطا', "درصد فروش محصول باید وارد شود!",
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        p_price = int(p_price)
        percent = int(percent)

        acc = Product(name, p_price, percent=percent)
        acc.insert(db)
        QMessageBox.information(self, 'افزودن', "محصول با موفقیت افزوده شد!",
                                QMessageBox.Ok, QMessageBox.Ok)

        self._add_dialog.txt_product_name.setText('')
        self._add_dialog.txt_sales_percent.setText('')
        self._add_dialog.txt_purchase_price.setText('')
        self._add_dialog.txt_product_name.setFocus()

    # method exit
    def exit(self):
        self.close()


class UpdateDialog(QDialog):
    def __init__(self, product):
        super(QDialog, self).__init__()

        # Define the instance to access the the UI elements defined in
        self._update_dialog = Ui_update_dialog()
        self._update_dialog.setupUi(self)
        self._update_dialog.retranslateUi(self)

        # Initialize textbox's text
        self._update_dialog.txt_product_id.setText(str(product.id))
        self._update_dialog.txt_product_name.setText(str(product.name))
        self._update_dialog.txt_purchase_price.setText(str(product.purchase_price))
        self._update_dialog.txt_sales_percent.setText(str(product.percent))
        self._update_dialog.txt_sales_price.setText(str(product.sales_price))

        # Connect button with methods.
        self._connect()

    def _connect(self):
        self._update_dialog.btn_update_cancel.clicked.connect(self.exit)
        self._update_dialog.btn_update.clicked.connect(self.update_product)
        self._update_dialog.txt_purchase_price.textChanged.connect(self.txt_pprice_change)
        self._update_dialog.txt_sales_percent.textChanged.connect(self.txt_percent_change)

    def txt_pprice_change(self):
        p_price = self._update_dialog.txt_purchase_price.text()
        if not p_price.isnumeric():
            self._update_dialog.txt_purchase_price.setText(p_price[:len(p_price)-1])

    def txt_percent_change(self):
        percent = self._update_dialog.txt_sales_percent.text()
        if not percent.isnumeric():
            self._update_dialog.txt_sales_percent.setText(percent[:len(percent)-1])

    def update_product(self):
        global db
        name = self._update_dialog.txt_product_name.text()
        if name == '':
            QMessageBox.information(self, 'خطا', "نام محصول باید وارد شود!",
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        p_price = self._update_dialog.txt_purchase_price.text()
        if p_price == '':
            QMessageBox.information(self, 'خطا', " قیمت خرید محصول باید وارد شود!",
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        percent = self._update_dialog.txt_sales_percent.text()
        if percent == '':
            QMessageBox.information(self, 'خطا', "درصد فروش محصول باید وارد شود!",
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        p_price = int(p_price)
        percent = int(percent)

        response = QMessageBox.question(self, 'ویرایش', "از ویرایش محصول مطمئن هستید؟",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if response == QMessageBox.Yes:
            acc = Product(name=name, purchase_price=p_price, percent=percent)
            acc.id = int(self._update_dialog.txt_product_id.text())
            acc.update(db)

            QMessageBox.question(self, 'ویرایش', "محصول با موفقیت ویرایش شد!",
                                 QMessageBox.Ok, QMessageBox.Ok)
            self.exit()

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
        self._add_dialog = AddDialog()
        self._update_dialog = None

        # Initialize some other variables.
        self.table_rows = self._window.tableWidget.rowCount()
        header = self._window.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

        # Connect button with methods.
        self._connect()

        self.search()

    def _connect(self):
        self._window.txt_main_search_name.textChanged.connect(self.search)
        self._window.btn_main_refresh.clicked.connect(self.search)
        self._window.menu_exit.triggered.connect(self.exit)
        self._window.btn_main_exit.clicked.connect(self.exit)
        self._window.btn_main_add.clicked.connect(self.show_add_dialog)
        self._window.menu_add.triggered.connect(self.show_add_dialog)
        self._window.btn_main_update.clicked.connect(self.update_product)

    def displayTime(self):
        self._window.lbl_datetime.setText(QtCore.QDateTime.currentDateTime().toString('hh:mm:ss'))

    def search(self):
        self._window.tableWidget.setRowCount(0)
        global db
        text = self._window.txt_main_search_name.text()
        if text == '':
            data = db.select()
            for d in data:
                self.table_rows = self._window.tableWidget.rowCount()
                self._window.tableWidget.insertRow(self.table_rows)
                self._window.tableWidget.setItem(self.table_rows, 0, QTableWidgetItem(d[1]))
                self._window.tableWidget.setItem(self.table_rows, 1, QTableWidgetItem(str(d[0])))
                self._window.tableWidget.setItem(self.table_rows, 2, QTableWidgetItem(str(d[2])))
                self._window.tableWidget.setItem(self.table_rows, 3, QTableWidgetItem(str(d[4])))
                self._window.tableWidget.setItem(self.table_rows, 4, QTableWidgetItem(str(d[3])))

        else:
            data = db.select(text)
            for d in data:
                self.table_rows = self._window.tableWidget.rowCount()
                self._window.tableWidget.insertRow(self.table_rows)
                self._window.tableWidget.setItem(self.table_rows, 0, QTableWidgetItem(d[1]))
                self._window.tableWidget.setItem(self.table_rows, 1, QTableWidgetItem(str(d[0])))
                self._window.tableWidget.setItem(self.table_rows, 2, QTableWidgetItem(str(d[2])))
                self._window.tableWidget.setItem(self.table_rows, 3, QTableWidgetItem(str(d[4])))
                self._window.tableWidget.setItem(self.table_rows, 4, QTableWidgetItem(str(d[3])))

    def update_product(self):
        global db
        item = self._window.tableWidget.selectedItems()
        if len(item) == 0:
            QMessageBox.information(self, 'خطا', "لطفا یک محصول را انتخاب کنید!",
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        id = int(item[1].text())
        product = Product.search(db, id)
        if not product:
            QMessageBox.information(self, 'خطا', "محصولی با این مشخصات یافت نشد! لطفا صفحه را بازخوانی کرده و دوباره تلاش کنید.",
                                    QMessageBox.Ok, QMessageBox.Ok)
        else:
            self._update_dialog = UpdateDialog(product)
            self.show_update_dialog()

    def show_add_dialog(self):
        self._add_dialog.show()

    def show_update_dialog(self):
        self._update_dialog.show()

    # method exit
    def exit(self):
        sys.exit()


db = Database()
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
