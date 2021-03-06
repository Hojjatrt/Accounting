# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 450)
        MainWindow.setMinimumSize(QtCore.QSize(600, 450))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_datetime = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_datetime.setFont(font)
        self.lbl_datetime.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_datetime.setWordWrap(True)
        self.lbl_datetime.setObjectName("lbl_datetime")
        self.verticalLayout.addWidget(self.lbl_datetime)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txt_main_search_name = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_main_search_name.setObjectName("txt_main_search_name")
        self.horizontalLayout.addWidget(self.txt_main_search_name)
        self.btn_main_refresh = QtWidgets.QToolButton(self.centralwidget)
        self.btn_main_refresh.setMinimumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_main_refresh.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("refresh24x24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_main_refresh.setIcon(icon)
        self.btn_main_refresh.setIconSize(QtCore.QSize(25, 25))
        self.btn_main_refresh.setObjectName("btn_main_refresh")
        self.horizontalLayout.addWidget(self.btn_main_refresh)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_main_add = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_main_add.setFont(font)
        self.btn_main_add.setObjectName("btn_main_add")
        self.horizontalLayout_2.addWidget(self.btn_main_add)
        self.btn_main_update = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_main_update.setFont(font)
        self.btn_main_update.setObjectName("btn_main_update")
        self.horizontalLayout_2.addWidget(self.btn_main_update)
        self.btn_main_exit = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_main_exit.setFont(font)
        self.btn_main_exit.setObjectName("btn_main_exit")
        self.horizontalLayout_2.addWidget(self.btn_main_exit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lbl_datetime_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_datetime_2.setFont(font)
        self.lbl_datetime_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_datetime_2.setWordWrap(True)
        self.lbl_datetime_2.setObjectName("lbl_datetime_2")
        self.verticalLayout.addWidget(self.lbl_datetime_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.menu.setObjectName("menu")
        self.menu_exit = QtWidgets.QMenu(self.menubar)
        self.menu_exit.setObjectName("menu_exit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu_add = QtWidgets.QAction(MainWindow)
        self.menu_add.setObjectName("menu_add")
        self.menu_update = QtWidgets.QAction(MainWindow)
        self.menu_update.setObjectName("menu_update")
        self.menu_pass_edit = QtWidgets.QAction(MainWindow)
        self.menu_pass_edit.setObjectName("menu_pass_edit")
        self.menu.addAction(self.menu_add)
        self.menu_exit.addAction(self.menu_pass_edit)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_exit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "حسابداری"))
        self.lbl_datetime.setText(_translate("MainWindow", "....."))
        self.label.setText(_translate("MainWindow", "نام محصول : "))
        self.btn_main_refresh.setText(_translate("MainWindow", "بازخوانی"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "نام محصول"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "شناسه"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "قیمت خرید"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "درصد"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "قیمت فروش"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "ادوات"))
        self.btn_main_add.setText(_translate("MainWindow", "افزودن"))
        self.btn_main_update.setText(_translate("MainWindow", "ویرایش"))
        self.btn_main_exit.setText(_translate("MainWindow", "خروج"))
        self.lbl_datetime_2.setText(_translate("MainWindow", "پشتیبانی : رأفت 09150352682"))
        self.menu.setTitle(_translate("MainWindow", "محصول"))
        self.menu_exit.setTitle(_translate("MainWindow", "تنظیمات"))
        self.action_3.setText(_translate("MainWindow", "یسب"))
        self.menu_add.setText(_translate("MainWindow", "افزودن"))
        self.menu_update.setText(_translate("MainWindow", "بروزرسانی"))
        self.menu_pass_edit.setText(_translate("MainWindow", "تغییر رمز عبور"))

