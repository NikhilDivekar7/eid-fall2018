# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Dialog1(object):
    def insert_data(self):
        username = self.uname_le.text()
        email = self.email_le.text()
        password = self.pwd_le.text()
        
        connection = sqlite3.connect("login.db")
        connection.execute("INSERT INTO USERS VALUES(?,?,?)",(username, email, password))
        connection.commit()
        connection.close()
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(404, 225)
        
        self.uname_label = QtWidgets.QLabel(Dialog)
        self.uname_label.setGeometry(QtCore.QRect(80, 60, 91, 21))
        self.uname_label.setObjectName("uname_label")
        self.email_label = QtWidgets.QLabel(Dialog)
        self.email_label.setGeometry(QtCore.QRect(80, 100, 81, 21))
        self.email_label.setObjectName("email_label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 140, 81, 21))
        self.label_3.setObjectName("label_3")
        self.pwd_label = QtWidgets.QLabel(Dialog)
        self.pwd_label.setGeometry(QtCore.QRect(80, 140, 67, 21))
        self.pwd_label.setText("")
        self.pwd_label.setObjectName("pwd_label")
        self.uname_le = QtWidgets.QLineEdit(Dialog)
        self.uname_le.setGeometry(QtCore.QRect(180, 50, 161, 33))
        self.uname_le.setObjectName("uname_le")
        self.email_le = QtWidgets.QLineEdit(Dialog)
        self.email_le.setGeometry(QtCore.QRect(180, 90, 161, 33))
        self.email_le.setObjectName("email_le")
        self.pwd_le = QtWidgets.QLineEdit(Dialog)
        self.pwd_le.setGeometry(QtCore.QRect(180, 130, 161, 33))
        self.pwd_le.setObjectName("pwd_le")
        self.signup_button = QtWidgets.QPushButton(Dialog)
        self.signup_button.setGeometry(QtCore.QRect(150, 180, 101, 31))
        self.signup_button.setObjectName("signup_button")
        self.signup_button.clicked.connect(self.insert_data)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sign-up Window"))
        self.uname_label.setText(_translate("Dialog", "User-name:"))
        self.email_label.setText(_translate("Dialog", "Email-Id:"))
        self.label_3.setText(_translate("Dialog", "Password:"))
        self.signup_button.setText(_translate("Dialog", "SignUp"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog1()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

