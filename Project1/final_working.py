# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mydesign2.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
# This is py file for the main window
# File: final_working.py
# Author: Nikhil Divekar

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime
import Adafruit_DHT
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Ui_MainWindow(object):
    
    # Global variables
    readings = 0
    temp_avg = 0
    temp_avg1 = 0
    hum_avg = 0;
    correct_readings = 0
    tempList = np.array([0,0,0,0,0,0,0,0,0,0])
    humList =[0,0,0,0,0,0,0,0,0,0]
    readingNum = np.array([0,1,2,3,4,5,6,7,8,9])
    tempCount = 0
    humCount = 0
    temp_min_val = 20
    temp_max_val = 40
    hum_min_val = 15
    hum_max_val = 50
    
    # User can set the manual limit on the UI for temp and humidity
    def setLimit(self):
        if(len(self.temp_min.text()) > 0):
            self.temp_min_val = int(self.temp_min.text());
        if(len(self.temp_max.text()) > 0):
            self.temp_max_val = int(self.temp_max.text());
        if(len(self.hum_min.text()) > 0):
            self.hum_min_val = int(self.hum_min.text());
        if(len(self.hum_max.text()) > 0):
            self.hum_max_val = int(self.hum_max.text()); 
    
    # Plots the temperature graph
    def plotGraph(self):
        fig = plt.figure()
        ax1 = fig.add_subplot(1,1,1)
        ax1.plot(self.readingNum, self.tempList)
        ax1.set_title("Temperature Graph")
        ax1.set_xlabel("Reading number")
        ax1.set_ylabel("Temp value")
        plt.show()
        print("Plot Graph")
        
    # Plots the humidity graph    
    def hum_plotGraph(self):
        fig2 = plt.figure()
        ax2 = fig2.add_subplot(1,1,1)
        ax2.plot(self.readingNum, self.humList)
        ax2.set_title("Humidity Graph")
        ax2.set_xlabel("Reading number")
        ax2.set_ylabel("Humidity value")
        plt.show()
        print("Plot Graph")
        
    # Function for the timer    
    def get_readings(self):
        self.readings = self.readings + 1
        print("Reached")
        print("Readings :" ,self.readings)
        print("Min temp",self.temp_min_val)
        if(self.ref_enable.isChecked()):
            self.get_temp()
    
    def timerEvent(self):
        global time
        timer = QTimer()
        time = QTime(0,0,0)
        prev_time = QTime(0,0,0)
        prev_time = time
        time = time.addSecs(1)
        print(time.toString("hh:mm:ss"))
        print("Entered")
        timer.start(100)
        timer.setInterval(2000)
        timer.timeout.connect(self.timerEvent)
    
    # This function is responsible for setup of the user layout
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(475, 406)
        MainWindow.setStyleSheet("background-color:rgb(170, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.temp_label = QtWidgets.QLabel(self.centralwidget)
        self.temp_label.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.temp_label.setObjectName("temp_label")
        self.hum_label = QtWidgets.QLabel(self.centralwidget)
        self.hum_label.setGeometry(QtCore.QRect(250, 10, 71, 21))
        self.hum_label.setObjectName("hum_label")
        self.hum_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.hum_edit.setGeometry(QtCore.QRect(320, 10, 104, 31))
        self.hum_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hum_edit.setObjectName("hum_edit")
        self.temp_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.temp_edit.setGeometry(QtCore.QRect(110, 10, 121, 31))
        self.temp_edit.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.temp_edit.setObjectName("temp_edit")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(320, 60, 211, 21))
        self.time_label.setText("")
        self.time_label.setObjectName("time_label")
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setGeometry(QtCore.QRect(10, 60, 101, 31))
        self.refreshButton.setObjectName("refreshButton")
        self.refreshButton.clicked.connect(self.get_temp)
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(140, 60, 181, 21))
        self.label4.setObjectName("label4")
        self.avg_temp_label = QtWidgets.QLabel(self.centralwidget)
        self.avg_temp_label.setGeometry(QtCore.QRect(10, 110, 111, 21))
        self.avg_temp_label.setObjectName("avg_temp_label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 110, 131, 21))
        self.label_6.setObjectName("label_6")
        self.ref_enable = QtWidgets.QCheckBox(self.centralwidget)
        self.ref_enable.setGeometry(QtCore.QRect(10, 160, 161, 26))
        self.ref_enable.setObjectName("ref_enable")
        self.graph_but = QtWidgets.QPushButton(self.centralwidget)
        self.graph_but.setGeometry(QtCore.QRect(10, 200, 181, 31))
        self.graph_but.setObjectName("graph_but")
        self.graph_but.clicked.connect(self.plotGraph)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(210, 160, 67, 21))
        self.label_7.setObjectName("label_7")
        self.alert_label = QtWidgets.QLabel(self.centralwidget)
        self.alert_label.setGeometry(QtCore.QRect(250, 160, 191, 21))
        self.alert_label.setText("")
        self.alert_label.setObjectName("alert_label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(120, 100, 104, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(380, 104, 81, 31))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 200, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.hum_plotGraph)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 240, 99, 26))
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 280, 181, 21))
        self.label.setObjectName("label")
        self.temp_min = QtWidgets.QLineEdit(self.centralwidget)
        self.temp_min.setGeometry(QtCore.QRect(190, 274, 61, 31))
        self.temp_min.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.temp_min.setObjectName("temp_min")
        self.temp_max = QtWidgets.QLineEdit(self.centralwidget)
        self.temp_max.setGeometry(QtCore.QRect(320, 270, 61, 31))
        self.temp_max.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.temp_max.setObjectName("temp_max")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(276, 280, 21, 21))
        self.label_2.setObjectName("label_2")
        self.hum_max = QtWidgets.QLineEdit(self.centralwidget)
        self.hum_max.setGeometry(QtCore.QRect(320, 310, 61, 31))
        self.hum_max.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hum_max.setObjectName("hum_max")
        self.hum_min = QtWidgets.QLineEdit(self.centralwidget)
        self.hum_min.setGeometry(QtCore.QRect(190, 314, 61, 31))
        self.hum_min.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hum_min.setObjectName("hum_min")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(276, 320, 21, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 320, 161, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 280, 61, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.setLimit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 475, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.get_readings)
        self.timer1.start(3000)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # This function is responsible for the changes made by user on designer
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Temperature and Humidity Measurement"))
        self.temp_label.setText(_translate("MainWindow", "Temperature: "))
        self.hum_label.setText(_translate("MainWindow", "Humidity:"))
        self.refreshButton.setText(_translate("MainWindow", "Refresh"))
        self.label4.setText(_translate("MainWindow", "Time of the last change:"))
        self.avg_temp_label.setText(_translate("MainWindow", "Average temp:"))
        self.label_6.setText(_translate("MainWindow", "Average humidity:"))
        self.ref_enable.setText(_translate("MainWindow", "Automatic Refresh"))
        self.graph_but.setText(_translate("MainWindow", "Plot Temperature Graph"))
        self.label_7.setText(_translate("MainWindow", "Alert:"))
        self.pushButton.setText(_translate("MainWindow", "Plot Humidity Graph"))
        self.checkBox.setText(_translate("MainWindow", "Fahrenheit"))
        self.label.setText(_translate("MainWindow", "Set Temperature Range:"))
        self.label_2.setText(_translate("MainWindow", "to"))
        self.label_3.setText(_translate("MainWindow", "to"))
        self.label_4.setText(_translate("MainWindow", "Set Humidity Range:"))
        self.pushButton_2.setText(_translate("MainWindow", "SET"))
     
    # The following temperature reads the temperature and humidity and also calculate their average
    def get_temp(self):
        _translate = QtCore.QCoreApplication.translate
        humidity, temperature = Adafruit_DHT.read(Adafruit_DHT.DHT22, 4)
        
        if(self.checkBox.isChecked()):
            temperature = temperature * 9/5.0 + 32

        if(humidity != None or temperature != None):
            temp_display = '{0:0.1f}'.format(temperature)
            humidity_display = '{0:0.1f}'.format(humidity)
            self.temp_edit.setText(_translate("MainWindow", temp_display))
            self.hum_edit.setText(_translate("MainWindow", humidity_display))
            self.time_label.setText(_translate("MainWindow", QtCore.QDateTime.currentDateTime().toString()))
            self.alert_label.setText(_translate("MainWindow", ""))
            self.correct_readings = self.correct_readings + 1
            
            if(temperature < self.temp_min_val):
                self.alert_label.setText(_translate("MainWindow", "Temperature below rang"))
            
            elif(temperature > self.temp_max_val):
                self.alert_label.setText(_translate("MainWindow", "Temperature exceeding range"))
                
            elif(humidity > self.hum_max_val):
                self.alert_label.setText(_translate("MainWindow", "Humidity exceeding range"))
                
            elif(humidity < self.hum_min_val):
                self.alert_label.setText(_translate("MainWindow", "Humidity below range"))
            
            if(self.tempCount > 9):
                self.tempCount = 0
                            
            self.tempList[self.tempCount] = temperature
            self.tempCount += 1
            print(self.tempList)
            
            if(self.humCount > 9):
                self.humCount = 0
                            
            self.humList[self.humCount] = humidity
            self.humCount += 1
            print(self.humList)
            
            #print("Correct readings:",correct readings)
            print(temperature)
            print(self.correct_readings)
            
            self.temp_avg = ((self.temp_avg *(self.correct_readings - 1)) + temperature)/self.correct_readings
            self.hum_avg = ((self.hum_avg *(self.correct_readings - 1)) + humidity)/self.correct_readings
            
            avg_temp_display = '{0:0.1f}'.format(self.temp_avg)
            avg_humidity_display = '{0:0.1f}'.format(self.hum_avg)
            self.textEdit.setText(_translate("MainWindow", avg_temp_display))
            self.textEdit_2.setText(_translate("MainWindow", avg_humidity_display))
        elif(humidity is None and temperature is None):
            self.alert_label.setText(_translate("MainWindow", "Sensor disconnected"))
            print("Sensor disconnected")
            
        
        #self.label.hide()
        #self.readings = self.readings + 1
        #print("Readings: ", self.readings)

# main function
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

