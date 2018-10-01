# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_main.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from final_working import Ui_MainWindow
from signup import Ui_Dialog1

class Ui_Dialog(object):
    
    #def showMsgBox(self, title, message):
        #msgBox = QtWidgets.MessageBox()
        #msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        #msgBox.setText(message)
        #msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        #msgBox.exec_()
    
    def loginCheck(self):
        username = self.userlineedit.text()
        password = self.pwd_line_edit.text()
              
        connection = sqlite3.connect("login.db")
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",(username, password))
        if(len(result.fetchall()) > 0):
            print("User found")
            self.mycodeWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.mycodeWindow)
            self.mycodeWindow.show()
            
        else:
            print("User not found")
            self.showMsgBox("Warning", "Incorrect Username or password")
            #self.showMsgBox('Warning','Invalid Username or passoword')
            
        connection.close()
        
    def showMsgBox(self, title, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
        
    def signupCheck(self):
        print("Sign-up clicked")
        self.signupWindow = QtWidgets.QDialog()
        self.ui = Ui_Dialog1()
        self.ui.setupUi(self.signupWindow)
        self.signupWindow.show()
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(519, 264)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color:rgb(170, 255, 255)")
        self.username_label = QtWidgets.QLabel(Dialog)
        self.username_label.setGeometry(QtCore.QRect(120, 80, 91, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.username_label.setFont(font)
        self.username_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(Dialog)
        self.password_label.setGeometry(QtCore.QRect(120, 120, 81, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.userlineedit = QtWidgets.QLineEdit(Dialog)
        self.userlineedit.setGeometry(QtCore.QRect(210, 70, 171, 33))
        self.userlineedit.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.userlineedit.setObjectName("userlineedit")
        self.pwd_line_edit = QtWidgets.QLineEdit(Dialog)
        self.pwd_line_edit.setGeometry(QtCore.QRect(210, 110, 171, 33))
        self.pwd_line_edit.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pwd_line_edit.setObjectName("pwd_line_edit")
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(130, 170, 101, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(self.loginCheck)
        self.signupButton = QtWidgets.QPushButton(Dialog)
        self.signupButton.setGeometry(QtCore.QRect(260, 170, 101, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.signupButton.setFont(font)
        self.signupButton.setObjectName("signupButton")
        self.signupButton.clicked.connect(self.signupCheck)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 21, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login Window"))
        self.username_label.setText(_translate("Dialog", "User-name:"))
        self.password_label.setText(_translate("Dialog", "Password:"))
        self.loginButton.setText(_translate("Dialog", "Login"))
        self.signupButton.setText(_translate("Dialog", "Sign Up"))
        self.label.setText(_translate("Dialog", "LOGIN WINDOW"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

