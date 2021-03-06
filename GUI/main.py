from PyQt5 import sip  #  import just for build exe file

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from GUI.UI_Files.login import Ui_login_dialog
from GUI.UI_Files.password_update import Ui_password_dialog
from GUI.UI_Files.add_product import Ui_Dialog_add
from GUI.UI_Files.update_product import Ui_update_dialog
from GUI.UI_Files.main_window import Ui_MainWindow
from database.Database import Database
from Models.Models import Product


class LoginDialog(QDialog):
    def __init__(self, mainwindow):
        super(QDialog, self).__init__()

        # Define the instance to access the the UI elements defined in
        self._login_dialog = Ui_login_dialog()
        self._login_dialog.setupUi(self)
        self._login_dialog.retranslateUi(self)
        self.mainwindow = mainwindow
        self._login_dialog.txt_password.setEchoMode(QLineEdit.Password)  # mask password in the lineEdit
        self.counter = 0

        # Initialize some other variables.
        self.setWindowIcon(QtGui.QIcon('icons/icons.png'))

        # Connect button with methods.
        self._connect()

    def _connect(self):
        self._login_dialog.btn_exit.clicked.connect(self.exit)
        self._login_dialog.btn_login.clicked.connect(self.login)

    def login(self):
        global db
        password = self._login_dialog.txt_password.text()
        if password == '':
            QMessageBox.information(self, 'خطا', "لطفا رمز عبور را وارد نمایید!",
                                    QMessageBox.Ok, QMessageBox.Ok)
            return

        user = ('admin', password)
        check = db.login(user)
        if check:
            self.mainwindow.show()
            self.exit()
        else:
            self.counter += 1
            if self.counter == 3:
                QMessageBox.information(self, 'خطا', "تعداد تکرار اشتباه شما بیش از حد بود!",
                                        QMessageBox.Ok, QMessageBox.Ok)
                sys.exit()
            QMessageBox.information(self, 'خطا', "رمز عبور معتبر نیست!",
                                    QMessageBox.Ok, QMessageBox.Ok)
            return

    # method exit
    def exit(self):
        self.close()


class PasswordDialog(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()

        # Define the instance to access the the UI elements defined in
        self._pass_dialog = Ui_password_dialog()
        self._pass_dialog.setupUi(self)
        self._pass_dialog.retranslateUi(self)

        # Initialize some other variables.
        self.setWindowIcon(QtGui.QIcon('icons/icons.png'))

        # Connect button with methods.
        self._connect()

    def _connect(self):
        self._pass_dialog.btn_exit.clicked.connect(self.exit)
        self._pass_dialog.btn_save.clicked.connect(self.save)

    def save(self):
        global db
        old_password = self._pass_dialog.txt_old_pass.text()
        if old_password == '':
            QMessageBox.information(self, 'خطا', "لطفا رمز عبور فعلی را وارد نمایید!",
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        new_password = self._pass_dialog.txt_new_pass.text()
        if new_password == '':
            QMessageBox.information(self, 'خطا', "لطفا رمز عبور جدید را وارد نمایید!",
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        user = ('admin', old_password)
        check = db.login(user)
        if check:
            if len(new_password) < 6:
                QMessageBox.information(self, 'خطا', "رمز عبور جدید باید بیشتر از 6 کاراکتر باشد!",
                                        QMessageBox.Ok, QMessageBox.Ok)
                return
            db.update_password(new_password)
            QMessageBox.information(self, 'رمز عبور', "رمز عبور با موفقیت تغییر پیدا کرد!",
                                    QMessageBox.Ok, QMessageBox.Ok)
            self.exit()

    # method exit
    def exit(self):
        self.close()


class AddDialog(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()

        # Define the instance to access the the UI elements defined in
        self._add_dialog = Ui_Dialog_add()
        self._add_dialog.setupUi(self)
        self._add_dialog.retranslateUi(self)

        # Initialize some other variables.
        self.setWindowIcon(QtGui.QIcon('icons/icons.png'))

        # Connect button with methods.
        self._connect()

    def _connect(self):
        self._add_dialog.btn_add_cancel.clicked.connect(self.exit)
        self._add_dialog.btn_add_save.clicked.connect(self.add_product)
        self._add_dialog.txt_purchase_price.textChanged.connect(self.txt_pprice_change)
        self._add_dialog.txt_sales_percent.textChanged.connect(self.txt_percent_change)
        self._add_dialog.txt_sales_price.textChanged.connect(self.txt_sprice_change)
        self._add_dialog.checkBox_accessories.toggled.connect(self.checked_change)

    def txt_pprice_change(self):
        p_price = self._add_dialog.txt_purchase_price.text()
        if not p_price.isnumeric():
            self._add_dialog.txt_purchase_price.setText(p_price[:len(p_price)-1])

    def txt_percent_change(self):
        percent = self._add_dialog.txt_sales_percent.text()
        if not percent.isnumeric():
            self._add_dialog.txt_sales_percent.setText(percent[:len(percent)-1])

    def txt_sprice_change(self):
        s_price = self._add_dialog.txt_sales_price.text()
        if not s_price.isnumeric():
            self._add_dialog.txt_purchase_price.setText(s_price[:len(s_price)-1])

    def checked_change(self):
        check = self._add_dialog.checkBox_accessories.isChecked()
        if check:
            self._add_dialog.txt_sales_price.setEnabled(True)
            self._add_dialog.txt_sales_percent.setEnabled(False)
        else:
            self._add_dialog.txt_sales_price.setEnabled(False)
            self._add_dialog.txt_sales_percent.setEnabled(True)

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

        check = self._add_dialog.checkBox_accessories.isChecked()
        print(check)
        s_price = 0
        percent = 0
        if check:
            s_price = self._add_dialog.txt_sales_price.text()
            if s_price == '':
                QMessageBox.information(self, 'خطا', " قیمت فروش محصول باید وارد شود!",
                                        QMessageBox.Ok, QMessageBox.Ok)
                return
        else:
            percent = self._add_dialog.txt_sales_percent.text()
            if percent == '':
                QMessageBox.information(self, 'خطا', "درصد فروش محصول باید وارد شود!",
                                        QMessageBox.Ok, QMessageBox.Ok)
                return
        try:
            p_price = int(p_price)
            if check:
                s_price = int(s_price)
                acc = Product(name, p_price, accessories=check, sales_price=s_price)
            else:
                percent = int(percent)
                acc = Product(name, p_price, percent=percent, accessories=check)

            acc.insert(db)
            QMessageBox.information(self, 'افزودن', "محصول با موفقیت افزوده شد!",
                                    QMessageBox.Ok, QMessageBox.Ok)

            self._add_dialog.txt_product_name.setText('')
            self._add_dialog.txt_sales_percent.setText('')
            self._add_dialog.txt_purchase_price.setText('')
            self._add_dialog.txt_sales_price.setText('')
            self._add_dialog.checkBox_accessories.setChecked(False)
            self.checked_change()
            self._add_dialog.txt_product_name.setFocus()
        except:
            QMessageBox.information(self, 'خطا', "خطا!",
                                    QMessageBox.Ok, QMessageBox.Ok)
            return

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
        self.setWindowIcon(QtGui.QIcon('icons/icons.png'))
        self._update_dialog.txt_product_id.setText(str(product.id))
        self._update_dialog.txt_product_name.setText(str(product.name))
        self._update_dialog.txt_purchase_price.setText(str(product.purchase_price))
        self._update_dialog.txt_sales_percent.setText(str(product.percent))
        self._update_dialog.txt_sales_price.setText(str(product.sales_price))
        self._update_dialog.checkBox_accessories.setChecked(product.accessories)

        self.checked_change()

        # Connect button with methods.
        self._connect()

    def _connect(self):
        self._update_dialog.btn_update_cancel.clicked.connect(self.exit)
        self._update_dialog.btn_update.clicked.connect(self.update_product)
        self._update_dialog.txt_purchase_price.textChanged.connect(self.txt_pprice_change)
        self._update_dialog.txt_sales_percent.textChanged.connect(self.txt_percent_change)
        self._update_dialog.txt_sales_price.textChanged.connect(self.txt_sprice_change)
        self._update_dialog.checkBox_accessories.toggled.connect(self.checked_change)

    def txt_pprice_change(self):
        p_price = self._update_dialog.txt_purchase_price.text()
        if not p_price.isnumeric():
            self._update_dialog.txt_purchase_price.setText(p_price[:len(p_price)-1])

    def txt_percent_change(self):
        percent = self._update_dialog.txt_sales_percent.text()
        if not percent.isnumeric():
            self._update_dialog.txt_sales_percent.setText(percent[:len(percent)-1])

    def txt_sprice_change(self):
        s_price = self._update_dialog.txt_sales_price.text()
        if not s_price.isnumeric():
            self._update_dialog.txt_purchase_price.setText(s_price[:len(s_price)-1])

    def checked_change(self):
        check = self._update_dialog.checkBox_accessories.isChecked()
        if check:
            self._update_dialog.txt_sales_price.setEnabled(True)
            self._update_dialog.txt_sales_percent.setEnabled(False)
        else:
            self._update_dialog.txt_sales_price.setEnabled(False)
            self._update_dialog.txt_sales_percent.setEnabled(True)

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
        check = self._update_dialog.checkBox_accessories.isChecked()
        if check:
            s_price = self._update_dialog.txt_sales_price.text()
            if s_price == '':
                QMessageBox.information(self, 'خطا', " قیمت فروش محصول باید وارد شود!",
                                        QMessageBox.Ok, QMessageBox.Ok)
                return
        else:
            percent = self._update_dialog.txt_sales_percent.text()
            if percent == '':
                QMessageBox.information(self, 'خطا', "درصد فروش محصول باید وارد شود!",
                                        QMessageBox.Ok, QMessageBox.Ok)
                return
        try:
            p_price = int(p_price)
            if check:
                s_price = int(s_price)
                acc = Product(name, p_price, accessories=check, sales_price=s_price)
            else:
                percent = int(percent)
                acc = Product(name, p_price, percent=percent, accessories=check)

            response = QMessageBox.question(self, 'ویرایش', "از ویرایش محصول مطمئن هستید؟",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if response == QMessageBox.Yes:
                acc.id = int(self._update_dialog.txt_product_id.text())
                acc.update(db)

                QMessageBox.question(self, 'ویرایش', "محصول با موفقیت ویرایش شد!",
                                     QMessageBox.Ok, QMessageBox.Ok)
                self.exit()
        except:
            QMessageBox.information(self, 'خطا', "خطا!",
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
        self._login_dialog = LoginDialog(self)
        self._password_dialog = PasswordDialog()
        self._add_dialog = AddDialog()
        self._update_dialog = None

        # Initialize some other variables.
        self.setWindowIcon(QtGui.QIcon('icons/icons.png'))
        self.table_rows = self._window.tableWidget.rowCount()
        header = self._window.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

        # Connect button with methods.
        self._connect()
        self.search_show()

    def _connect(self):
        self._window.txt_main_search_name.textChanged.connect(self.search_show)
        self._window.btn_main_refresh.clicked.connect(self.search_show)
        self._window.menu_pass_edit.triggered.connect(self.show_update_password)
        self._window.btn_main_exit.clicked.connect(self.exit)
        self._window.btn_main_add.clicked.connect(self.show_add_dialog)
        self._window.menu_add.triggered.connect(self.show_add_dialog)
        self._window.btn_main_update.clicked.connect(self.update_product)

    def displayTime(self):
        self._window.lbl_datetime.setText(QtCore.QDateTime.currentDateTime().toString('hh:mm:ss'))

    @property
    def login_dialog(self):
        return self._login_dialog

    def search_show(self):
        self._window.tableWidget.setRowCount(0)
        global db
        text = self._window.txt_main_search_name.text()
        if text == '':
            data = db.select()
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
            if d[5]:
                self._window.tableWidget.setItem(self.table_rows, 5, QTableWidgetItem('***'))
            else:
                self._window.tableWidget.setItem(self.table_rows, 5, QTableWidgetItem(''))

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

    def show_update_password(self):
        self._password_dialog.show()

    # method exit
    def exit(self):
        sys.exit()


db = Database()
app = QApplication(sys.argv)
window = MainWindow()
window.login_dialog.show()
app.exec_()
