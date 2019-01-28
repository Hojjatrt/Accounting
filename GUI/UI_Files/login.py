# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login_dialog(object):
    def setupUi(self, login_dialog):
        login_dialog.setObjectName("login_dialog")
        login_dialog.resize(400, 293)
        login_dialog.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.verticalLayout = QtWidgets.QVBoxLayout(login_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(login_dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(login_dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.txt_password = QtWidgets.QLineEdit(login_dialog)
        self.txt_password.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txt_password.setInputMask("")
        self.txt_password.setText("")
        self.txt_password.setMaxLength(10)
        self.txt_password.setClearButtonEnabled(False)
        self.txt_password.setObjectName("txt_password")
        self.horizontalLayout_4.addWidget(self.txt_password)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_login = QtWidgets.QPushButton(login_dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout_3.addWidget(self.btn_login)
        self.btn_exit = QtWidgets.QPushButton(login_dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setObjectName("btn_exit")
        self.horizontalLayout_3.addWidget(self.btn_exit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(login_dialog)
        QtCore.QMetaObject.connectSlotsByName(login_dialog)

    def retranslateUi(self, login_dialog):
        _translate = QtCore.QCoreApplication.translate
        login_dialog.setWindowTitle(_translate("login_dialog", "ورود"))
        self.label_2.setText(_translate("login_dialog", "ورود به سیستم حسابداری"))
        self.label_5.setText(_translate("login_dialog", "رمز عبور :"))
        self.txt_password.setPlaceholderText(_translate("login_dialog", "رمز عبور"))
        self.btn_login.setText(_translate("login_dialog", "ورود"))
        self.btn_exit.setText(_translate("login_dialog", "خروج"))

