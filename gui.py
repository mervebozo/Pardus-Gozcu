#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GUI file for Pardus Gözcü

from PyQt4 import QtCore, QtGui
from findUsers import *
from host import getUserData
from activeInterface import interface
from times import *
from kill_logout import *
from time import sleep
from threading import Thread
from applications import *
from restrictAccess import *
from tasks import *
from Tkinter import *
from notify import *
from menus import *
import tkFont
import os 
import re
import subprocess
import tarfile
import sqlite3
import datetime
import time


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

def showMsgBox(title, text):
    msgBox = QtGui.QMessageBox()
    msgBox.setWindowTitle(title)
    msgBox.setText(text)
    msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
    msgBox.exec_()

class Ui_MainWindow(object):

    def showPopup(self):
	dlg = QtGui.QInputDialog()                 
        dlg.setInputMode(QtGui.QInputDialog.TextInput) 
        dlg.setWindowTitle("Yasaklanacak Alan Adi")
        dlg.setLabelText("IP veya Host Adi:")                        
        dlg.resize(500,100)                             
        ok = dlg.exec_()                                
        url = dlg.textValue()
        if ok:
            available = False
            for i in range(self.listWidget.count()):
                if url == str(self.listWidget.item(i).text()):
                    available = True
                    showMsgBox("Pardus Gozcu", "Site zaten karalistede!")
                    break
            if not available:
                self.listWidget.addItem(url)

    def setupUi(self, MainWindow):
        setOut = self.readSettings()
	rp = os.path.dirname(os.path.realpath(sys.argv[0]))
	USR = setOut[14][:-1]
	cmd = "sudo find " + rp + "/ -exec chown " + USR + " {} \;"
	os.system(cmd)
	cmd = "sudo find " + rp + "/ -exec chmod 700 {} \;"
	os.system(cmd)
	QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(setOut[11][:-1]))
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1059, 676)
	MainWindow.setFixedSize(1059, 676)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(40, 10, 981, 591))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 30, 141, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.frame = QtGui.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(30, 60, 211, 51))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.comboBox = QtGui.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 191, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))

        userNames = user()
        self.comboBox.clear()
        self.comboBox.addItems(userNames)
        self.comboBox.currentIndexChanged.connect(self.itemSelect)

        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 191, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.scrollArea = QtGui.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(30, 150, 211, 381))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 209, 379))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.listWidget = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 211, 381))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget.addItems(getUserData("appSettings/karaliste.txt", str(self.comboBox.currentText())))

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.ekleButon = QtGui.QPushButton(self.tab)
        self.ekleButon.setGeometry(QtCore.QRect(250, 310, 71, 27))
        self.ekleButon.setObjectName(_fromUtf8("ekleButon"))
        self.ekleButon.clicked.connect(self.showPopup) #
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 350, 71, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.cikar) #

        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(830, 20, 81, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.frame_2 = QtGui.QFrame(self.tab)
        self.frame_2.setGeometry(QtCore.QRect(780, 50, 181, 341))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.textEdit = QtGui.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 181, 341))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(380, 20, 141, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.scrollArea_2 = QtGui.QScrollArea(self.tab)
        self.scrollArea_2.setGeometry(QtCore.QRect(370, 50, 241, 231))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 239, 229))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.listWidget_5 = QtGui.QListWidget(self.scrollAreaWidgetContents_2)
        self.listWidget_5.setGeometry(QtCore.QRect(0, 0, 241, 231))
        self.listWidget_5.setObjectName(_fromUtf8("listWidget_5"))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.pushButton_3 = QtGui.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 120, 71, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
	self.pushButton_3.clicked.connect(self.addBadWord)

        self.pushButton_4 = QtGui.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(620, 160, 71, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
	self.pushButton_4.clicked.connect(self.removeBadWord)

        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(390, 330, 141, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.frame_3 = QtGui.QFrame(self.tab)
        self.frame_3.setGeometry(QtCore.QRect(370, 370, 241, 161))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.label_7 = QtGui.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(10, 40, 141, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit = QtGui.QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QtCore.QRect(170, 40, 61, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_8 = QtGui.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(10, 100, 141, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit_2 = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 100, 61, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton_5 = QtGui.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(620, 420, 81, 27))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.listeUygButton = QtGui.QPushButton(self.tab)
        self.listeUygButton.setGeometry(QtCore.QRect(250, 400, 71, 27))
        self.listeUygButton.clicked.connect(self.applyRestriction)

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.listeUygButton.setFont(font)
        self.listeUygButton.setObjectName(_fromUtf8("listeUygButton"))
        self.pushButton_8 = QtGui.QPushButton(self.tab)
        self.pushButton_8.setGeometry(QtCore.QRect(620, 210, 71, 27))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
	self.pushButton_8.clicked.connect(self.applyBadWord)

        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(430, 50, 141, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.comboBox_3 = QtGui.QComboBox(self.tab_2)
        self.comboBox_3.setGeometry(QtCore.QRect(380, 80, 191, 27))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))

        self.comboBox_3.clear()
        self.comboBox_3.addItems(userNames)
        self.comboBox_3.currentIndexChanged.connect(self.userChange)

        self.label_10 = QtGui.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(420, 150, 141, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.tableWidget = QtGui.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(50, 180, 901, 271))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))

        self.tableWidget.setColumnCount(24)
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnWidth(0,45)
        self.tableWidget.setColumnWidth(1,45)
        self.tableWidget.setColumnWidth(2,45)
        self.tableWidget.setColumnWidth(3,45)
        self.tableWidget.setColumnWidth(4,45)
        self.tableWidget.setColumnWidth(5,45)
        self.tableWidget.setColumnWidth(6,45)
        self.tableWidget.setColumnWidth(7,45)
        self.tableWidget.setColumnWidth(8,45)
        self.tableWidget.setColumnWidth(9,45)
        self.tableWidget.setColumnWidth(10,45)
        self.tableWidget.setColumnWidth(11,45)
        self.tableWidget.setColumnWidth(12,45)
        self.tableWidget.setColumnWidth(13,45)
        self.tableWidget.setColumnWidth(14,45)
        self.tableWidget.setColumnWidth(15,45)
        self.tableWidget.setColumnWidth(16,45)
        self.tableWidget.setColumnWidth(17,45)
        self.tableWidget.setColumnWidth(18,45)
        self.tableWidget.setColumnWidth(19,45)
        self.tableWidget.setColumnWidth(20,45)
        self.tableWidget.setColumnWidth(21,45)
        self.tableWidget.setColumnWidth(22,45)
        self.tableWidget.setColumnWidth(23,45)

        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(20, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(21, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(22, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(23, item)

        for i in range(7):
            for j in range(24):
                item = QtGui.QTableWidgetItem()
                item.setCheckState(QtCore.Qt.Unchecked)
                self.tableWidget.setItem(i, j, item)
        times = getTimes(str(self.comboBox_3.currentText()), "appSettings/zamankisit.txt")
        for x in times:
            item = QtGui.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Checked)
            self.tableWidget.setItem(int(x[0]), int(x[1]), item)

        self.pushButton = QtGui.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(440, 480, 98, 27))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton.clicked.connect(self.restrictTime)

        self.radioButton = QtGui.QRadioButton(self.tab_2)
        self.radioButton.setGeometry(QtCore.QRect(80, 110, 191, 22))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.tab_2)
        self.radioButton_2.setGeometry(QtCore.QRect(80, 80, 141, 22))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
	self.radioButton_2.setChecked(True)
        self.radioButton_2.toggled.connect(self.userChange)
        self.tipButton = QtGui.QPushButton(self.tab_2)
        self.tipButton.setGeometry(QtCore.QRect(900, 480, 51, 21))
        self.tipButton.setObjectName(_fromUtf8("tipButton"))
        self.tipButton.clicked.connect(self.showTip)

        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.frame_4 = QtGui.QFrame(self.tab_3)
        self.frame_4.setGeometry(QtCore.QRect(30, 60, 211, 51))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.comboBox_4 = QtGui.QComboBox(self.frame_4)
        self.comboBox_4.setGeometry(QtCore.QRect(10, 10, 191, 27))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
		
        self.comboBox_4.clear()
        self.comboBox_4.addItems(userNames)
        self.comboBox_4.currentIndexChanged.connect(self.itemSelect2)

        self.label_11 = QtGui.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(40, 30, 141, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(410, 30, 171, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.listWidget_2 = QtGui.QListWidget(self.tab_3)
        self.listWidget_2.setGeometry(QtCore.QRect(30, 170, 211, 301))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.listWidget_2.addItems(getApps())

        self.pushButton_6 = QtGui.QPushButton(self.tab_3)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 300, 71, 31))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
	self.pushButton_6.clicked.connect(self.addToList)
	
        self.pushButton_7 = QtGui.QPushButton(self.tab_3)
        self.pushButton_7.setGeometry(QtCore.QRect(630, 250, 71, 31))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
	self.pushButton_7.clicked.connect(self.removeApp)
	
        self.label_13 = QtGui.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(830, 30, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.textEdit_2 = QtGui.QTextEdit(self.tab_3)
        self.textEdit_2.setGeometry(QtCore.QRect(770, 60, 191, 341))
	self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.pushButton_9 = QtGui.QPushButton(self.tab_3)
        self.pushButton_9.setGeometry(QtCore.QRect(420, 500, 181, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_9.clicked.connect(self.confirmAppRestrict)

        self.label_14 = QtGui.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(40, 140, 171, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.listWidget_3 = QtGui.QListWidget(self.tab_3)
        self.listWidget_3.setGeometry(QtCore.QRect(400, 60, 221, 411))
        self.listWidget_3.setObjectName(_fromUtf8("listWidget_3"))
	self.listWidget_3.addItems(getUserData("appSettings/uygulamalar.txt", str(self.comboBox_4.currentText())))

        self.pushButton_13 = QtGui.QPushButton(self.tab_3)
        self.pushButton_13.setGeometry(QtCore.QRect(630, 206, 71, 31))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
	self.pushButton_13.clicked.connect(self.itemSelect2)

        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.frame_5 = QtGui.QFrame(self.tab_4)
	self.frame_5.setGeometry(QtCore.QRect(30, 170, 211, 161))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.logsButton = QtGui.QPushButton(self.frame_5)
	self.logsButton.setGeometry(QtCore.QRect(30, 26, 151, 31))
        self.logsButton.setObjectName(_fromUtf8("logsButton"))
        self.logsButton.clicked.connect(self.showLog)

        self.resetLogsButton = QtGui.QPushButton(self.frame_5)
	self.resetLogsButton.setGeometry(QtCore.QRect(30, 66, 151, 31))
        self.resetLogsButton.setObjectName(_fromUtf8("resetLogsButton"))
	self.resetLogsButton.clicked.connect(self.deleteLog)

        self.archieveButton = QtGui.QPushButton(self.frame_5)
	self.archieveButton.setGeometry(QtCore.QRect(30, 106, 151, 31))
        self.archieveButton.setObjectName(_fromUtf8("archieveButton"))
	self.archieveButton.clicked.connect(self.createArchieve)

        self.label_16 = QtGui.QLabel(self.tab_4)
        self.label_16.setGeometry(QtCore.QRect(40, 30, 161, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.frame_6 = QtGui.QFrame(self.tab_4)
        self.frame_6.setGeometry(QtCore.QRect(30, 60, 211, 51))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.comboBox_5 = QtGui.QComboBox(self.frame_6)
        self.comboBox_5.setGeometry(QtCore.QRect(10, 10, 191, 27))
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
	self.comboBox_5.addItems(userNames)
        self.label_15 = QtGui.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(40, 140, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_17 = QtGui.QLabel(self.tab_4)
        self.label_17.setGeometry(QtCore.QRect(410, 30, 151, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.frame_7 = QtGui.QFrame(self.tab_4)
        self.frame_7.setGeometry(QtCore.QRect(350, 60, 221, 471))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.listWidget_4 = QtGui.QListWidget(self.frame_7)
        self.listWidget_4.setGeometry(QtCore.QRect(0, 0, 221, 471))
        self.listWidget_4.setObjectName(_fromUtf8("listWidget_4"))
        self.listWidget_4.addItems(getUserTasksPS(str(self.comboBox_5.currentText())))
	self.comboBox_5.currentIndexChanged.connect(self.userChange2)
        self.killButton = QtGui.QPushButton(self.tab_4)
        self.killButton.setGeometry(QtCore.QRect(580, 260, 121, 27))
        self.killButton.setObjectName(_fromUtf8("killButton"))
	self.killButton.clicked.connect(self.Kill)

        self.pushButton_10 = QtGui.QPushButton(self.tab_4)
        self.pushButton_10.setGeometry(QtCore.QRect(580, 300, 121, 27))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
	self.pushButton_10.clicked.connect(self.KillForbid)	

        self.label_18 = QtGui.QLabel(self.tab_4)
        self.label_18.setGeometry(QtCore.QRect(830, 30, 151, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.textEdit_3 = QtGui.QTextEdit(self.tab_4)
        self.textEdit_3.setGeometry(QtCore.QRect(770, 60, 191, 201))
	self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.label_19 = QtGui.QLabel(self.tab_4)
        self.label_19.setGeometry(QtCore.QRect(820, 300, 141, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.frame_8 = QtGui.QFrame(self.tab_4)
        self.frame_8.setGeometry(QtCore.QRect(769, 330, 191, 201))
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName(_fromUtf8("frame_8"))
        self.pushButton_11 = QtGui.QPushButton(self.frame_8)
        self.pushButton_11.setGeometry(QtCore.QRect(50, 160, 98, 27))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_11.clicked.connect(self.notification)

        self.textEdit_4 = QtGui.QTextEdit(self.frame_8)
        self.textEdit_4.setGeometry(QtCore.QRect(23, 20, 151, 131))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
	self.pushButton_12 = QtGui.QPushButton(self.tab_4)
        self.pushButton_12.setGeometry(QtCore.QRect(580, 220, 121, 27))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
	self.pushButton_12.clicked.connect(self.userChange2)

        self.label_20 = QtGui.QLabel(self.tab_4)
        self.label_20.setGeometry(QtCore.QRect(40, 350, 151, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.frame_9 = QtGui.QFrame(self.tab_4)
        self.frame_9.setGeometry(QtCore.QRect(30, 380, 211, 151))
        self.frame_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setObjectName(_fromUtf8("frame_9"))
        self.listWidget_6 = QtGui.QListWidget(self.frame_9)
        self.listWidget_6.setGeometry(QtCore.QRect(0, 0, 211, 151))
        self.listWidget_6.setObjectName(_fromUtf8("listWidget_6"))
	self.listWidget_6.addItems(activeUser())

        self.pushButton_14 = QtGui.QPushButton(self.tab_4)
        self.pushButton_14.setGeometry(QtCore.QRect(250, 440, 81, 27))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.pushButton_14.clicked.connect(self.currentUsers)

        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))

	self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.label_6 = QtGui.QLabel(self.tab_5)
        self.label_6.setGeometry(QtCore.QRect(120, 6, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.frame_10 = QtGui.QFrame(self.tab_5)
        self.frame_10.setGeometry(QtCore.QRect(80, 40, 811, 381))
        self.frame_10.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_10.setObjectName(_fromUtf8("frame_10"))
        self.pushButton_15 = QtGui.QPushButton(self.frame_10)
        self.pushButton_15.setGeometry(QtCore.QRect(520, 320, 181, 41))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
	self.pushButton_15.clicked.connect(self.updateMessage)

        self.label_21 = QtGui.QLabel(self.frame_10)
        self.label_21.setGeometry(QtCore.QRect(20, 10, 401, 17))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.textEdit_5 = QtGui.QTextEdit(self.frame_10)
        self.textEdit_5.setGeometry(QtCore.QRect(20, 30, 371, 31))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.textEdit_5.setText(setOut[0][:-1])
        self.label_22 = QtGui.QLabel(self.frame_10)
        self.label_22.setGeometry(QtCore.QRect(20, 70, 361, 17))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.textEdit_6 = QtGui.QTextEdit(self.frame_10)
        self.textEdit_6.setGeometry(QtCore.QRect(20, 90, 371, 31))
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.textEdit_6.setText(setOut[1][:-1])
        self.label_23 = QtGui.QLabel(self.frame_10)
        self.label_23.setGeometry(QtCore.QRect(20, 130, 381, 17))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.textEdit_7 = QtGui.QTextEdit(self.frame_10)
        self.textEdit_7.setGeometry(QtCore.QRect(20, 150, 371, 31))
        self.textEdit_7.setObjectName(_fromUtf8("textEdit_7"))
	self.textEdit_7.setText(setOut[2][:-1])
        self.label_24 = QtGui.QLabel(self.frame_10)
        self.label_24.setGeometry(QtCore.QRect(420, 0, 371, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.textEdit_8 = QtGui.QTextEdit(self.frame_10)
        self.textEdit_8.setGeometry(QtCore.QRect(420, 30, 371, 31))
        self.textEdit_8.setObjectName(_fromUtf8("textEdit_8"))
	self.textEdit_8.setText(setOut[6][:-1])
        self.label_25 = QtGui.QLabel(self.frame_10)
        self.label_25.setGeometry(QtCore.QRect(20, 250, 371, 17))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.textEdit_9 = QtGui.QTextEdit(self.frame_10)
        self.textEdit_9.setGeometry(QtCore.QRect(20, 270, 371, 31))
        self.textEdit_9.setObjectName(_fromUtf8("textEdit_9"))
   	self.textEdit_9.setText(setOut[4][:-1])
        self.label_26 = QtGui.QLabel(self.frame_10)
        self.label_26.setGeometry(QtCore.QRect(20, 306, 381, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.textEdit_10 = QtGui.QTextEdit(self.frame_10)
        self.textEdit_10.setGeometry(QtCore.QRect(20, 330, 371, 31))
        self.textEdit_10.setObjectName(_fromUtf8("textEdit_10"))
   	self.textEdit_10.setText(setOut[5][:-1])
        self.label_27 = QtGui.QLabel(self.frame_10)
        self.label_27.setGeometry(QtCore.QRect(420, 70, 341, 17))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.textEdit_11 = QtGui.QTextEdit(self.frame_10)
        self.textEdit_11.setGeometry(QtCore.QRect(420, 90, 371, 31))
        self.textEdit_11.setObjectName(_fromUtf8("textEdit_11"))
	self.textEdit_11.setText(setOut[7][:-1])
        self.label_28 = QtGui.QLabel(self.frame_10)
        self.label_28.setGeometry(QtCore.QRect(420, 130, 371, 17))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_28.setFont(font)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.textEdit_12 = QtGui.QTextEdit(self.frame_10)
        self.textEdit_12.setGeometry(QtCore.QRect(420, 150, 371, 31))
        self.textEdit_12.setObjectName(_fromUtf8("textEdit_12"))
	self.textEdit_12.setText(setOut[8][:-1])
        self.label_29 = QtGui.QLabel(self.frame_10)
        self.label_29.setGeometry(QtCore.QRect(420, 190, 371, 17))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_29.setFont(font)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.textEdit_13 = QtGui.QTextEdit(self.frame_10)
        self.textEdit_13.setGeometry(QtCore.QRect(420, 210, 371, 31))
        self.textEdit_13.setObjectName(_fromUtf8("textEdit_13"))
	self.textEdit_13.setText(setOut[9][:-1])
        self.label_30 = QtGui.QLabel(self.frame_10)
        self.label_30.setGeometry(QtCore.QRect(420, 250, 381, 17))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_30.setFont(font)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.textEdit_14 = QtGui.QTextEdit(self.frame_10)
        self.textEdit_14.setGeometry(QtCore.QRect(420, 270, 371, 31))
        self.textEdit_14.setObjectName(_fromUtf8("textEdit_14"))
	self.textEdit_14.setText(setOut[10][:-1])
        self.label_31 = QtGui.QLabel(self.frame_10)
        self.label_31.setGeometry(QtCore.QRect(20, 190, 361, 17))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_31.setFont(font)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.textEdit_15 = QtGui.QTextEdit(self.frame_10)
        self.textEdit_15.setGeometry(QtCore.QRect(20, 210, 371, 31))
        self.textEdit_15.setObjectName(_fromUtf8("textEdit_15"))
	self.textEdit_15.setText(setOut[3][:-1])
        self.label_32 = QtGui.QLabel(self.tab_5)
        self.label_32.setGeometry(QtCore.QRect(120, 420, 151, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.frame_11 = QtGui.QFrame(self.tab_5)
        self.frame_11.setGeometry(QtCore.QRect(80, 450, 221, 91))
        self.frame_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_11.setObjectName(_fromUtf8("frame_11"))
        self.comboBox_2 = QtGui.QComboBox(self.frame_11)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 6, 161, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem("Oxygen")  
        self.comboBox_2.addItem("Plastique")  
        self.comboBox_2.addItem("Cleanlooks")  
        self.comboBox_2.addItem("CDE")  
        self.comboBox_2.addItem("Motif")  
        self.comboBox_2.addItem("GTK+")
    
        thm = str(setOut[11][:-1])
        for i in range(self.comboBox_2.count()):
            if self.comboBox_2.itemText(i) == thm:
                self.comboBox_2.setCurrentIndex(i)
                break

        self.pushButton_16 = QtGui.QPushButton(self.frame_11)
        self.pushButton_16.setGeometry(QtCore.QRect(60, 46, 98, 31))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
	self.pushButton_16.clicked.connect(self.changeTheme)

        self.label_33 = QtGui.QLabel(self.tab_5)
        self.label_33.setGeometry(QtCore.QRect(370, 420, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.frame_12 = QtGui.QFrame(self.tab_5)
        self.frame_12.setGeometry(QtCore.QRect(330, 450, 561, 91))
        self.frame_12.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_12.setObjectName(_fromUtf8("frame_12"))
        self.label_37 = QtGui.QLabel(self.frame_12)
        self.label_37.setGeometry(QtCore.QRect(20, 16, 411, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_37.setFont(font)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.checkBox_2 = QtGui.QCheckBox(self.frame_12)
        self.checkBox_2.setGeometry(QtCore.QRect(360, 10, 111, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setText(_fromUtf8(""))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        if setOut[12][:-1] == "True":
            self.checkBox_2.setCheckState(QtCore.Qt.Checked)
        else:
            self.checkBox_2.setCheckState(QtCore.Qt.Unchecked)
        self.label_38 = QtGui.QLabel(self.frame_12)
        self.label_38.setGeometry(QtCore.QRect(20, 36, 441, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_38.setFont(font)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.textEdit_17 = QtGui.QTextEdit(self.frame_12)
        self.textEdit_17.setGeometry(QtCore.QRect(360, 40, 45, 31))
        self.textEdit_17.setObjectName(_fromUtf8("textEdit_17"))
        self.textEdit_17.setText(setOut[13][:-1])

        self.label_39 = QtGui.QLabel(self.frame_12)
        self.label_39.setGeometry(QtCore.QRect(20, 46, 241, 51))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_39.setFont(font)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.pushButton_18 = QtGui.QPushButton(self.frame_12)
        self.pushButton_18.setGeometry(QtCore.QRect(430, 20, 91, 41))
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.pushButton_18.clicked.connect(self.generalSet)

        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1059, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuYard_m = QtGui.QMenu(self.menubar)
        self.menuYard_m.setObjectName(_fromUtf8("menuYard_m"))
        self.menuAyarlar = QtGui.QMenu(self.menubar)
        self.menuAyarlar.setObjectName(_fromUtf8("menuAyarlar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionYard_m_Konular = QtGui.QAction(MainWindow)
        self.actionYard_m_Konular.setObjectName(_fromUtf8("actionYard_m_Konular"))
        self.actionYard_m_Konular.triggered.connect(showHelp)
        self.actionHakk_nda = QtGui.QAction(MainWindow)
        self.actionHakk_nda.setObjectName(_fromUtf8("actionHakk_nda"))
        self.actionHakk_nda.triggered.connect(about)

        self.actionAyarlar = QtGui.QAction(MainWindow)
        self.actionAyarlar.setObjectName(_fromUtf8("actionAyarlar"))

        self.menuYard_m.addAction(self.actionYard_m_Konular)
        self.menuYard_m.addAction(self.actionHakk_nda)
        self.menuAyarlar.addAction(self.actionAyarlar)
        self.menubar.addAction(self.menuAyarlar.menuAction())
        self.menubar.addAction(self.menuYard_m.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #periodic control
        newThread = Thread(target=self.periodic)
        newThread.start()
        #program kapandiginda yasamaya devam eder.

	#get used apps on different thread.
	usedAppsThread = Thread(target=getUsedApps)
	usedAppsThread.start()
	
    def applyRestriction(self):
	name = str(self.comboBox.currentText())
	onWidget = []
	for i in range(self.listWidget.count()):
	    onWidget.append(str(self.listWidget.item(i).text()))
	message = self.getMessageList(name, "appSettings/karaliste.txt", onWidget, 0)
	if len(message) > 0:
	  showNotification(name, message)
	usrDt = getUserData("appSettings/karaliste.txt", name)
	for dt in usrDt:
	    self.removeFromFile("appSettings/karaliste.txt", dt, name)
	lineName = '$' + name
	self.removeLineFromFile("appSettings/karaliste.txt", lineName)
	toWrite = [lineName]
	for ow in onWidget:
	    toWrite.append(ow)           
	f = open("appSettings/karaliste.txt", 'a')
	for url in toWrite:
	    f.write(url + '\n')
	f.close()
	os.system('sudo sh resetIPTable.sh')
	f = open("appSettings/karaliste.txt", "r")
	sites = f.readlines()
	f.close()
	user = None
	for i in range(len(sites)):
	    if '$' == sites[i][0]:
		user = sites[i][1:-1]
	    else:
		if sites[i] == '\n':
		    continue
		URL = sites[i][:-1]
		query = "host " + URL + " | grep \"has address \" | cut -d' ' -f4"
		IPs = (subprocess.check_output(query, shell=True).split('\n'))[:-1]
		for IP in IPs:
		    command = "sudo iptables -A OUTPUT -o " + interface() + " -m owner --uid-owner " + user + " -d " + IP + " -j REJECT"
		    os.system(command)
	for i in [4,6]:
	    command = "sudo iptables-save > /etc/iptables/rules.v%d" %i 
	    os.system(command)
	showMsgBox("Pardus Gozcu", "Degisiklikler kaydedildi.")

    def addBadWord(self):
	dlg = QtGui.QInputDialog()                 
        dlg.setInputMode(QtGui.QInputDialog.TextInput) 
        dlg.setWindowTitle("Yasaklanacak Kelime")
        dlg.setLabelText("Kelimeyi giriniz:")                        
        dlg.resize(500,100)                             
        ok = dlg.exec_()                                
        word = dlg.textValue()
        if ok:
	    try:
		word = str(word)
		self.listWidget_5.addItems([word])	   
	    except:
		showMsgBox("Pardus Gozcu", "Yasakli kelime URL ile eslestirileceginden URL formatina uygun olmalidir. Turkce karakterleri kullanamazsiniz.")

    def removeBadWord(self):
	self.listWidget_5.takeItem(self.listWidget_5.currentRow())

    def applyBadWord(self):
	userName = str(self.comboBox.currentText())
	words = getUserData("appSettings/kelime.txt", userName)
	onWidget = []
        for i in range(self.listWidget_5.count()):
	    onWidget.append(str(self.listWidget_5.item(i).text()))
	message = self.getMessageList(userName, "appSettings/kelime.txt", onWidget, 2)
	if len(message) > 0:
	    showNotification(userName, message)
	for word in words:
	    cmd = "sudo iptables -D OUTPUT -p tcp --dport 80 -m string --algo bm --string " + word + " -m  owner --uid-owner " + userName + " -j DROP"
	    os.system(cmd)
            self.removeFromFile("appSettings/kelime.txt", word, userName)
        lineName = '$' + userName
        self.removeLineFromFile("appSettings/kelime.txt", lineName)
        toWrite = [lineName]
        for word in onWidget:
	    cmd = "sudo iptables -A OUTPUT -p tcp --dport 80 -m string --algo bm --string " + word + " -m  owner --uid-owner " + userName + " -j DROP"
	    os.system(cmd)
            toWrite.append(word)
        f = open("appSettings/kelime.txt", 'a')
        for word in toWrite:
    	    f.write(word + '\n')
	f.close()
        for i in [4,6]:
            cmd = "sudo iptables-save > /etc/iptables/rules.v%d" %i 
            os.system(cmd)
	showMsgBox("Pardus Gozcu", "Degisiklikler kaydedildi.")

    def cikar(self):
        self.listWidget.takeItem(self.listWidget.currentRow())
        
    def removeFromFile(self, filePath, url, name):
	f = open(filePath, "r")
        lns = f.readlines()
        f.close()
        index = 0
        while (index < len(lns)) and (lns[index] != url + "\n"):
            index += 1
        try:
            del lns[index]
        except:
            del lns[index-1]
        f = open(filePath, "w")
        for ln in lns:
            f.write(ln)

    def itemSelect(self):
	self.listWidget.clear()
        self.listWidget.addItems(getUserData("appSettings/karaliste.txt", str(self.comboBox.currentText())))
        self.listWidget_5.clear()
        self.listWidget_5.addItems(getUserData("appSettings/kelime.txt", str(self.comboBox.currentText())))


    def itemSelect2(self):
        self.listWidget_3.clear()
        self.listWidget_3.addItems(getUserData("appSettings/uygulamalar.txt", str(self.comboBox_4.currentText())))

    def restrictTime(self):
        if self.radioButton_2.isChecked():
            path = "appSettings/zamankisit.txt"
        else:
            path = "appSettings/netkisit.txt"
	name = str(self.comboBox_3.currentText())
        f = open(path, "r")
        data = f.readlines()
        f.close()
        for i in range(len(data)):
            if ('$' + name) in data[i]:
                del data[i]
                while (len(data) > i) and not ('$' in  data[i]):
                    del data[i]
                break
        data.append('$' + name + '\n')
        for i in range(7):  
            for j in range(24):
                item = self.tableWidget.item(i, j)
                if item.checkState() == 2:
                    line = "%d %d\n" %(i, j)
                    data.append(line)
        f = open(path, "w")
        for item in data:
              f.write(item)
        f.close()
        self.loginRights()

    def userChange(self):
	for i in range(7):
	    for j in range(24):
		item = QtGui.QTableWidgetItem()
                item.setCheckState(QtCore.Qt.Unchecked)
                self.tableWidget.setItem(i, j, item)
        if self.radioButton_2.isChecked():
            times = getTimes(str(self.comboBox_3.currentText()), "appSettings/zamankisit.txt")
        else:
            times = getTimes(str(self.comboBox_3.currentText()), "appSettings/netkisit.txt")
        for x in times:
            item = QtGui.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Checked)
            self.tableWidget.setItem(int(x[0]), int(x[1]), item)

    def loginRights(self):
        msg = self.readSettings()
        if self.radioButton_2.isChecked():
            usageOrNet = 1
            path = "appSettings/zamankisit.txt"
        else:
            usageOrNet = 0
            path = "appSettings/netkisit.txt"
	userList = user()
        for usr in userList:
            if isLegal(usr, path):
		remain = remainingSeconds(usr, path)
                h = datetime.datetime.now().hour
                hrs = getBannedHoursUser(((datetime.datetime.now() + datetime.timedelta(hours=24)).isoweekday() - 1), "appSettings/zamankisit.txt", usr)
                if (h == 23) and (0 in hrs):
                    remain = (60 - datetime.datetime.now().minute) * 60
                if usageOrNet: 
                    self.unlockUser(usr)
                    if remain != -1:
                        executer(remain, self.forbid, usr)
                        if usr == str(self.comboBox_3.currentText()) and usr in activeUser():
			    message = msg[6][:-1]
			    message = message.replace('3', str(remain/60))
                            if h == 23:
                                sumHour = 1 
                                for i in range(1, len(hrs)):
                                    if hrs[i] == hrs[i-1] + 1:
                                        sumHour += 1                
                                message = message.replace('X', str(sumHour * 60))
                            else:
			        message = message.replace('X', str((timeToEndBan(usr, path) - remain) / 60))
			    showNotification(usr, message)
                else:
                    reconnect(usr)
                    if usr == str(self.comboBox_3.currentText()) and usr in activeUser():
			showNotification(usr, msg[5][:-1])
                    if remain != -1:
                        executer(remain, self.forbidNet, usr)
            else:
                if usageOrNet:
                    self.forbid(usr)
                else:
                    self.forbidNet(usr)
                    if usr == str(self.comboBox_3.currentText()) and usr in activeUser():
			showNotification(usr, msg[4][:-1])
	showMsgBox("Pardus Gozcu", "Degisiklikler kaydedildi.")

    def forbid(self, userName):
	cmd = "sudo passwd -l %s" %userName
        os.system(cmd)
	executer(timeToEndBan(userName, "appSettings/zamankisit.txt"), self.unlockUser, userName)
	killLogOut(userName)

    def forbidNet(self, userName):
        disconnect(userName)
	executer(timeToEndBan(userName, "appSettings/netkisit.txt"), reconnect, userName)
   
    def unlockUser(self, userName):
	cmd = "sudo passwd -u %s" %userName
        os.system(cmd)
	
    def periodic(self):
	while True:
	    print "Periodic Check" 
	    cmd = "last | fgrep \"still logged in\" | cut -d\" \" -f1"
	    users = list(set((subprocess.check_output(cmd, shell=True).split('\n'))[:-1]))
	    for usr in users:
                if isLegal(usr, "appSettings/zamankisit.txt"):
		    self.unlockUser(usr)
		else:
		    self.forbid(usr)
            for usr in users:
                if isLegal(usr, "appSettings/netkisit.txt"):
                    reconnect(usr)
                else:
                    self.forbidNet(usr)
            now = datetime.datetime.now()
            msg = self.readSettings()
            if ((now.minute == 59 and now.second > 30) or (now.minute == 0 and now.second < 29)):
                if now.minute == 59:
                    h = now.hour + 1
                elif now.minute == 0:
                    h = now.hour
                for usr in users:		    
                    hrs = getBannedHoursTodayUser(usr, "appSettings/netkisit.txt")
                    prevhrs = hrs
                    prev = h - 1
                    if h == 0:
			prev = 23
			if datetime.datetime.now().minute == 59:
			    hrs = getBannedHoursUser(((datetime.datetime.now() + datetime.timedelta(hours=24)).isoweekday() - 1), "appSettings/netkisit.txt", usr)			    
			elif datetime.datetime.now().minute == 0:
			    prevhrs = getBannedHoursUser(((datetime.datetime.now() - datetime.timedelta(hours=24)).isoweekday() - 1), "appSettings/netkisit.txt", usr)
                    if (h in hrs) and (prev not in prevhrs):
                        showNotification(usr, msg[4][:-1])
                    elif (h not in hrs) and (prev in prevhrs):
                        showNotification(usr, msg[5][:-1])
            if now.minute == 57:
                h = now.hour
                nxt = h + 1
                for usr in users:
                    if isLegal(usr, "appSettings/zamankisit.txt"):
                        hrs = getBannedHoursTodayUser(usr, "appSettings/zamankisit.txt")
                        if h == 23:
			    nxt = 0
			    hrs = getBannedHoursUser(((datetime.datetime.now() + datetime.timedelta(hours=24)).isoweekday() - 1), "appSettings/zamankisit.txt", usr)
                        if nxt in hrs:
                            message = msg[6][:-1]
                            mn = 60 - datetime.datetime.now().minute
			    message = message.replace('3', str(mn))
                            if h == 23:								
				sumHour = 1 
				for i in range(1, len(hrs)):
				    if hrs[i] == hrs[i-1] + 1:
					sumHour += 1				
				message = message.replace('X', str(sumHour * 60))
                            else:				
				message = message.replace('X', str(timeToEndBan(usr, "appSettings/zamankisit.txt") / 60 - mn))
                            showNotification(usr, message)
	    sleep(60)

    def showTip(self):
        showMsgBox("Pardus Gozcu", "Kullanicilarin sisteme giris yapabilecegi ve Internet'e erisebilecekleri zamanlari duzenleyebilirsiniz. Isaretlediginiz zaman dilimleri engellenecektir.")

    def addToList(self):
	application = str(self.listWidget_2.currentItem().text())
        available = False
        for i in range(self.listWidget_3.count()):
            if application == str(self.listWidget_3.item(i).text()):
                available = True
		showMsgBox("Pardus Gozcu", "Uygulama zaten karalistede!")
                break
        if not available:
	    self.listWidget_3.addItem(application)

    def removeApp(self):
        self.listWidget_3.takeItem(self.listWidget_3.currentRow())

    def confirmAppRestrict(self):
        name = str(self.comboBox_4.currentText())
	onWidget = []
	for i in range(self.listWidget_3.count()):
            onWidget.append(str(self.listWidget_3.item(i).text()))
	message = self.getMessageList(name, "appSettings/uygulamalar.txt", onWidget, 7)
	if len(message) > 0:
	    showNotification(name, message)
        bannedApps = getUserData("appSettings/uygulamalar.txt", name)
        for app in bannedApps:
            path = "/usr/share/applications/" + app + ".desktop"
            try:
                allowApp(name, path)
            except:
                allowApp(name, app)
            bins = getAll(app)
            for b in bins:
                allowApp(name, b)
            self.removeFromFile("appSettings/uygulamalar.txt", app, name)
        lineName = '$' + name
        self.removeLineFromFile("appSettings/uygulamalar.txt", lineName)
        toWrite = [lineName]
        for i in range(self.listWidget_3.count()):
            appName = str(self.listWidget_3.item(i).text())
            path = "/usr/share/applications/" + appName + ".desktop"
            denyApp(name, path)
            bins = getAll(appName)
            for b in bins:
                denyApp(name, b)
            toWrite.append(appName)
            ID = getAppProcessID(name, appName)
            for I in ID:
                cmd = "sudo kill " + I
                os.system(cmd)
        f = open("appSettings/uygulamalar.txt", 'a')
        for app in toWrite:
            f.write(app + '\n')
        f.close()
	showMsgBox("Pardus Gozcu", "Degisiklikler kaydedildi.")

    def removeLineFromFile(self, file_, line):
        f = open(file_, 'r')
        lines = f.readlines()
        f.close()
        for i in range(len(lines)):
            if line in lines[i]:
                del lines[i]
                break
        f = open(file_, 'w')
        for l in lines:
            f.write(l)
        f.close()

    def userChange2(self):
        user = str(self.comboBox_5.currentText())
        tasks = getUserTasksPS(user)
	self.listWidget_4.clear()
        self.listWidget_4.addItems(tasks)

    def Kill(self):
	userName = str(self.comboBox_5.currentText())
	taskName = str(self.listWidget_4.currentItem().text())
        message = self.readSettings()[9][:-1]
        message = message.replace('$', taskName)
        showNotification(userName, message)
	self.listWidget_4.takeItem(self.listWidget_4.currentRow())
	data = getUserTasksIDSource(userName, taskName)
	IDs = data[0]
	for ID in IDs:
	    cmd = "kill -9 " + ID
	    try:
		os.system(cmd)
	    except:
		pass
	showMsgBox("Pardus Gozcu", "Uygulama Durduruldu.")
	return [data, taskName]

    def KillForbid(self):
        userName = str(self.comboBox_5.currentText())
	come = self.Kill()
	data = come[0]
	Sources = data[1]
	for Source in Sources:
	    denyApp(userName, Source)
        taskName = come[1]
        message = self.readSettings()[10][:-1]
        message = message.replace('$', taskName)
        showNotification(userName, message)                        
	ud = ['$' + userName + '\n']
        ud += getUserData("appSettings/uygulamalar.txt", userName)
        for i in range(1, len(ud)):
            self.removeFromFile("appSettings/uygulamalar.txt", ud[i], userName)
        self.removeLineFromFile("appSettings/uygulamalar.txt", '$' + userName)
        ud.append('\n' + Sources[0])
        f = open("appSettings/uygulamalar.txt", 'a')
        for u in ud:
            f.write(u)
        f.close()
	showMsgBox("Pardus Gozcu", "Degisiklikler Kaydedildi.")

    def showLog(self):
        userName = str(self.comboBox_5.currentText())
        fileName = "appSettings/log/" + userName + ".txt"
        root = Tk()
        root.title("Pardus Gözcü Sistem Kayıtları")
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
        root.geometry("+%d+%d" % (x, y))
        root.resizable(0,0)
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill=Y)
        _font = tkFont.Font(family="Helvetica", size=18, weight="bold")
        text = Text(root, font=_font)
        text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text.yview)
        if os.path.isfile(fileName):
            os.remove(fileName)
        self.createLog(userName)
        f = open(fileName, 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            text.insert(INSERT, line)
        text.config(state=DISABLED)
        text.pack()
        root.mainloop()

    def createLog(self, userName):
        ms = {"Jan" : "Ocak", "Feb" : "Şu0bat", "Mar" : "Mart", "Apr" : "Nisan", "May" : "Mayıs", "Jun" : "Haziran", "Jul" : "Temmuz", "Aug" : "Ağustos", "Sep" : "Eylül", "Oct" : "Ekim", "Nov" : "Kasım", "Dec" : "Aralık"}
        ds = {"Mon" : "Pazartesi", "Tue" : "        Salı", "Wed" : " Çarşamba", "Thu" : " Perşembe", "Fri" : "       Cuma", "Sat" : "Cumartesi", "Sun" : "      Pazar"}
        log = []
        log.append("__________________PARDUS GÖZCÜ____________________")
        log.append("================SİSTEM KAYITLARI=================")
        log.append(" ")
        log.append("************Kullanıcı Giriş Zamanları*****************")
        log.append(" ")
	cmd = "last " + userName
	lastOut = subprocess.check_output(cmd, shell=True).split('\n')
        if len(lastOut) > 3:
	    log.append("  Tarih                    Giriş Zamanı     Çıkış Zamanı")
            log.append(" ")
	    for lO in lastOut:
	        lO = lO.split(' ')
	        lO = [l for l in lO if l != '']
                if len(lO) > 8:
                    month = ""
                    day = ""
                    try:
                        month = ms[lO[-6]]
                    except:
                        pass
                    try:
                        day = ds[lO[-7]]
                    except:
                        pass
	            logLine = lO[-5] + " " + month + " " + day + "        " + lO[-4] + "                   "
                    if lO[-3] == "still":
                        logLine += "Çıkış Yapılmadı"
                    else:
                        if lO[-2] == "down":
                            logLine += "Sistem Kapatıldı"
                        elif lO[-2] == "crash":
                            logLine += "Olağandışı Sonlanma"
                        else:
                            logLine += lO[-2]
	        log.append(logLine)
        else:
            log.append("Kullanıcı için giriş kaydı bulunamadı.")
        log.append(" ")
        log.append("************Kullanılan Uygulamalar****************")
	log.append(" ")
	length = len(log)
	f = open("appSettings/log/kullanilan.txt", 'r')
	uA = f.readlines()
	for ua in uA:
	    log.append(ua[:-1])
	if len(log) == length:
	    log.append("Kayıtlar inceleniyor... Uygulamaları görmek için 30 sn. sonra tekrar deneyiniz.")
	log.append(" ")
        log.append("************Konsole Komut Geçmişi*****************")
	log.append(" ")
	cmd = "cat /home/" + userName + "/.bash_history"
	try:
	    out = subprocess.check_output(cmd, shell=True).split('\n')
	    for o in out:
	        log.append(o)	
	except:
	    log.append("Kullanıcı için Konsole kaydı bulunamadı.")
        log.append(" ")
        log.append("************İnternet Geçmişi**********************")
	SQL_STATEMENT = 'SELECT urls.url, visit_time FROM visits, urls WHERE visits.url=urls.id;'
	paths = ["/home/" + userName + "/.config/google-chrome/Default/History", "/home/" + userName + "/.config/chromium/Default/History"]
	for path in paths:
	    if os.path.isfile(path):
		log.append(" ")
		if "chromium" in path:
		    log.append("------------------Chromium Tarayıcı Geçmişi---------------------")
		    log.append(" ")
		    log.append("    Tarih        Saat                  URL")
        	    log.append(" ")
		else:
		    log.append("------------------Google Chrome Tarayıcı Geçmişi----------------")
                    log.append(" ")
		    log.append("    Tarih        Saat                  URL")
                    log.append(" ")
		try:
		    cmd = "fuser " + path
		    out = subprocess.check_output(cmd, shell=True).split(' ')
		    out = [o for o in out if o != '']
		    for o in out:
			cmd = "kill -9 " + o
			os.system(cmd)
		except:
		    pass
		c = sqlite3.connect(path) 
		for row in c.execute(SQL_STATEMENT):
		    date_time = self.dateFromWebkit(row[1], 1601)
		    log.append(str(date_time)[0:19] + "      " + row[0])
		c.close()
            else:
                if "chromium" in path:
                    log.append("\nChromium için kayıt bulunamadı.")
                else:
                    log.append("\nGoogle Chrome için kayıt bulunamadı.")
        SQL_STATEMENT = "SELECT url, visit_count, last_visit_date FROM moz_places WHERE visit_count > 0 order by last_visit_date asc;"
        cmd = "find /home/" + userName + "/.mozilla/firefox/ -name '*.default'"
        try:
            path = subprocess.check_output(cmd, shell=True)[:-1] + "/places.sqlite"
            if os.path.isfile(path):
	        log.append(" ")
	        log.append("--------------Mozilla Firefox Tarayıcı Geçmişi--------------")
                log.append(" ")
	        log.append("    Tarih        Saat                  URL")
                log.append(" ")
                try:
                    cmd = "fuser " + path
                    out = subprocess.check_output(cmd, shell=True).split(' ')
                    out = [o for o in out if o != '']
                    for o in out:
                        cmd = "kill -9 " + o
                        os.system(cmd)
                except:
                    pass
                c = sqlite3.connect(path) 
                for row in c.execute(SQL_STATEMENT):
                    date_time = self.dateFromWebkit(row[2], 1970)
                    log.append(str(date_time) + "        " + row[0])
                c.close()
        except:
            log.append("\nMozilla Firefox için kayıt bulunamadı.")
        log.append(" ")
        setOut = self.readSettings()
        constant = setOut[13][:-1]
        log.append("************Son " + constant + " Gün İçerisinde Değiştirilmiş Dosyalar****************")
	log.append(" ")
	try:
	    cmd = "find /home/" + userName + " -type f -mtime -" + constant + " | grep -v '/\.'"
	    out = subprocess.check_output(cmd, shell=True).split('\n')
	    for o in out:
	        log.append(o)
	    log.append(" ")
	except:
	    log.append("Değiştirilmiş dosya bulunamadı.")
        fileName = "appSettings/log/" + userName + ".txt"
        f = open(fileName, 'w')
        for l in log:
            f.write(l + '\n')
        f.close()

    def deleteLog(self):
	userName = str(self.comboBox_5.currentText())
        fileName = "appSettings/log/" + userName + ".txt"
        if os.path.isfile(fileName):
            os.remove(fileName)
	showMsgBox("Pardus Gozcu", "Kullanicinin gecici kayit dosyasi temizlendi.")

    def createArchieve(self):
	userName = str(self.comboBox_5.currentText())
        fileName = "appSettings/log/" + userName + ".txt"
        if not os.path.isfile(fileName):
            self.createLog(userName)
        fileName = "appSettings/log/" + userName + ".txt"
        out = fileName[:-3] + "tar.gz"
        tar = tarfile.open(out, "w:gz")
        tar.add(fileName)
        tar.close()
	showMsgBox("Pardus Gozcu", "Arsiv Olusturuldu.")

    def dateFromWebkit(self, webkitTimestamp, startDate):
    	epochStart = datetime.datetime(startDate, 1, 1) 
    	delta = datetime.timedelta(microseconds=int(webkitTimestamp))
    	return epochStart + delta

    def notification(self):
        userName = str(self.comboBox_5.currentText())
        message = str(self.textEdit_4.toPlainText().toUtf8())
	showNotification(userName, message)
	self.textEdit_4.clear()
	showMsgBox("Pardus Gozcu", "Mesaj Iletildi.")

    def currentUsers(self):
        self.listWidget_6.clear()
        self.listWidget_6.addItems(activeUser())

    def updateMessage(self):
	out = self.readSettings()
	out[0] = str(self.textEdit_5.toPlainText().toUtf8()) + '\n'
	out[1] = str(self.textEdit_6.toPlainText().toUtf8()) + '\n'
	out[2] = str(self.textEdit_7.toPlainText().toUtf8()) + '\n'
	out[3] = str(self.textEdit_15.toPlainText().toUtf8()) + '\n'
	out[4] = str(self.textEdit_9.toPlainText().toUtf8()) + '\n'
	out[5] = str(self.textEdit_10.toPlainText().toUtf8()) + '\n'
	out[6] = str(self.textEdit_8.toPlainText().toUtf8()) + '\n'
	out[7] = str(self.textEdit_11.toPlainText().toUtf8()) + '\n'
	out[8] = str(self.textEdit_12.toPlainText().toUtf8()) + '\n'
	out[9] = str(self.textEdit_13.toPlainText().toUtf8()) + '\n'
	out[10] = str(self.textEdit_14.toPlainText().toUtf8()) + '\n'
	f = open("appSettings/ayarlar.txt", 'w')
	for o in out:
	    f.write(o)
	f.close()
        showMsgBox("Pardus Gozcu", "Degisiklikler kaydedildi.")

    def changeTheme(self):
	theme = str(self.comboBox_2.currentText())
        out = self.readSettings()
	out[11] = theme + '\n'
	f = open("appSettings/ayarlar.txt", 'w')
	for o in out:
	    f.write(o)
	f.close()
	showMsgBox("Pardus Gozcu", "Temaniz ayarlandi. Degisiklik sonraki acilistan itibaren uygulanacaktir.")

    def generalSet(self):
        out = self.readSettings()
        user = out[14][:-1]
        f = open("/etc/rc.local", 'r')
        rclines = f.readlines()
        f.close()
        rclines = [rc[:-1] for rc in rclines]
        if self.checkBox_2.checkState() == QtCore.Qt.Checked:
            out[12] = "True" + '\n'
            if not 'sleep 30' in rclines:
                for i in range(len(rclines)):
                    if rclines[i] == "exit 0":
                        del rclines[i]
                        break
                From = getFROM(user)
                rclines.append("sleep 30")
                rclines.append("cd /usr/local/pardusgozcu")
                rclines.append("export XAUTHORITY=/home/" + user + "/.Xauthority")
                rclines.append("sudo DISPLAY=:" + From + " /usr/bin/python /usr/local/pardusgozcu/gui.py &")
                rclines.append("exit 0")
                rclines = [rc + '\n' for rc in rclines]
                f = open("/etc/rc.local", 'w')
                for rc in rclines:
                    f.write(rc)
                f.close()
		cmd = "sudo chmod 700 /etc/rc.local"
		os.system(cmd)
        else:
            out[12] = "False" + '\n'
            for i in range(len(rclines)):
                if rclines[i] == "sleep 30":
                    for j in range(4):
                        del rclines[i]
                    break
	    rclines = [rc + '\n' for rc in rclines]
            f = open("/etc/rc.local", 'w')
            for rc in rclines:
                f.write(rc)
            f.close()
        out[13] = str(self.textEdit_17.toPlainText()) + '\n'
        f = open("appSettings/ayarlar.txt", 'w')
        for o in out:
            f.write(o)
        f.close()
        showMsgBox("Pardus Gozcu", "Degisiklikler Kaydedildi.")

    def readSettings(self):
	f = open("appSettings/ayarlar.txt", 'r')
	out = f.readlines()
	f.close()
	return out

    def getMessageList(self, userName, path, onWidget, t):
	out = getUserData(path, userName)
	old = set(out)
	onWidget = set(onWidget)
	ints = old.intersection(onWidget)
	allowd = list(old - ints)
	forbid = list(onWidget - ints) 
	msg = self.readSettings()
	message = ""
	messageN = ""
	if len(forbid) > 0:
	    for f in forbid:
		message += (f + ', ')
	    message = message[:-2]
	    message = msg[t].replace('$', message) + '\n'
	if len(allowd) > 0:
	    for a in allowd:
		messageN += (a + ', ')
	    messageN = messageN[:-2]
	    message += msg[t+1].replace('$', messageN) 
	return message

    def retranslateUi(self, MainWindow):
	MainWindow.setWindowTitle(_translate("MainWindow", "Pardus Gözcü", None))
        self.label.setText(_translate("MainWindow", "Kullanıcılar", None))
        self.label_2.setText(_translate("MainWindow", "Site Adı ve IP Kara Listesi", None))
        self.ekleButon.setText(_translate("MainWindow", "Ekle", None))
        self.pushButton_2.setText(_translate("MainWindow", "Çıkar", None))
        self.label_3.setText(_translate("MainWindow", "Açıklama", None))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Bu modül ile IP engelleme, URL filtreleme,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">URL içerisinde kelime filtreleme,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">bant genişliği sınırlama</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gibi işlemler yapılarak kullanıcıların, yönetici tarafından uygun bulunmayan</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">alanlara erişimi kısıtlanabilir.</p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "Yasaklı Kelimeler", None))
        self.pushButton_3.setText(_translate("MainWindow", "Ekle", None))
        self.pushButton_4.setText(_translate("MainWindow", "Çıkar", None))
        self.label_5.setText(_translate("MainWindow", "Bant Genişliği", None))
        self.label_7.setText(_translate("MainWindow", "Yükleme Limiti (Kb/s)", None))
        self.label_8.setText(_translate("MainWindow", "İndirme Limiti (Kb/s)", None))
        self.pushButton_5.setText(_translate("MainWindow", "Güncelle", None))
        self.listeUygButton.setText(_translate("MainWindow", "Uygula", None))
        self.pushButton_8.setText(_translate("MainWindow", "Uygula", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "İçerik Filtresi", None))
        self.label_9.setText(_translate("MainWindow", "Kullanıcılar", None))
        self.label_10.setText(_translate("MainWindow", "Zaman Çizelgesi", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Pazartesi", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Salı", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Çarşamba", None))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Perşembe", None))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cuma", None))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Cumartesi", None))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Pazar", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "00:00", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "01:00", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "02:00", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "03:00", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "04:00", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "05:00", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "06:00", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "07:00", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "08:00", None))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "09:00", None))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "10:00", None))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "11:00", None))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "12:00", None))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "13:00", None))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "14:00", None))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "15:00", None))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "16:00", None))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "17:00", None))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "18:00", None))
        item = self.tableWidget.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "19:00", None))
        item = self.tableWidget.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "20:00", None))
        item = self.tableWidget.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "21:00", None))
        item = self.tableWidget.horizontalHeaderItem(22)
        item.setText(_translate("MainWindow", "22:00", None))
        item = self.tableWidget.horizontalHeaderItem(23)
        item.setText(_translate("MainWindow", "23:00", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Onayla", None))
        self.radioButton.setText(_translate("MainWindow", "İnternet Erişimini Kısıtla", None))
        self.radioButton_2.setText(_translate("MainWindow", "Kullanımı Kısıtla", None))
        self.tipButton.setText(_translate("MainWindow", "İpucu", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Kullanım Kontrolü", None))
        self.label_11.setText(_translate("MainWindow", "Kullanıcılar", None))
        self.label_12.setText(_translate("MainWindow", "Uygulama Kara Listesi", None))
        self.pushButton_6.setText(_translate("MainWindow", "Ekle", None))
        self.pushButton_7.setText(_translate("MainWindow", "Çıkar", None))
        self.label_13.setText(_translate("MainWindow", "Açıklama", None))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Bu modülün işlevi her kullanıcı için belirlenmiş yasaklı yazılımların kullanımını engellemektir. İçerik Filtresi Modülü\'nde olduğu gibi her kullanıcı için ayrı yasaklama yapılabilir. Bir uygulamayı yasakladığınızda ilgili kullanıcıya Ayarlar bölümünden özelleştirilebilir bir mesaj görüntülenecektir.</p></body></html>", None))
        self.pushButton_9.setText(_translate("MainWindow", "Uygula", None))
        self.label_14.setText(_translate("MainWindow", "Uygulama Listesi", None))
        self.pushButton_13.setText(_translate("MainWindow", "Yenile", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Kullanım Yönetimi", None))
        self.logsButton.setText(_translate("MainWindow", "Kayıtları Görüntüle", None))
        self.resetLogsButton.setText(_translate("MainWindow", "Kayıtları Temizle", None))
        self.archieveButton.setText(_translate("MainWindow", "Arşiv Dosyası Oluştur", None))
        self.label_16.setText(_translate("MainWindow", "Kullanıcılar", None))
        self.label_15.setText(_translate("MainWindow", "İşlem Kaydı", None))
        self.label_17.setText(_translate("MainWindow", "Etkin Görevler", None))
        self.killButton.setText(_translate("MainWindow", "Durdur", None))
        self.pushButton_10.setText(_translate("MainWindow", "Durdur/Yasakla", None))
        self.label_18.setText(_translate("MainWindow", "Açıklama", None))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Bu modül ile kullanıcıların işlem kaydını görüntüleyebilir, etkin görevlerine müdahalede bulunabilir ve  anlık ileti gönderebilirsiniz.</p></body></html>", None))
        self.label_19.setText(_translate("MainWindow", "İleti Gönder", None))
        self.pushButton_11.setText(_translate("MainWindow", "Gönder", None))
	self.pushButton_12.setText(_translate("MainWindow", "Yenile", None))
        self.label_20.setText(_translate("MainWindow", "Aktif Kullanıcılar", None))
	self.pushButton_14.setText(_translate("MainWindow", "Güncelle", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Gözetleme", None))
	#
	self.label_6.setText(_translate("MainWindow", "Kullanıcı Mesajları", None))
        self.pushButton_15.setText(_translate("MainWindow", "Güncelle", None))
        self.label_21.setText(_translate("MainWindow", "Web adresi yasaklandığında gösterilecek mesaj:", None))
        self.label_22.setText(_translate("MainWindow", "Web adresi yasağı kaldırıldığında gösterilecek mesaj:", None))
        self.label_23.setText(_translate("MainWindow", "Kelime yasaklandığında gösterilecek mesaj:", None))
        self.label_24.setText(_translate("MainWindow", "Kullanım süresi bitmeden önce gösterilecek mesaj:", None))
        self.label_25.setText(_translate("MainWindow", "Internet erişimi engellendiğinde gösterilecek mesaj:", None))
        self.label_26.setText(_translate("MainWindow", "Internet erişimine izin verildiğinde gösterilecek mesaj:", None))
        self.label_27.setText(_translate("MainWindow", "Uygulama yasaklandığında gösterilecek mesaj:", None))
        self.label_28.setText(_translate("MainWindow", "Uygulama yasağı kaldırılıdığında gösterilecek mesaj:", None))
        self.label_29.setText(_translate("MainWindow", "Uygulama durdurulduğunda gösterilecek mesaj:", None))
        self.label_30.setText(_translate("MainWindow", "Uygulama durdurulup/yasaklandığında gösterilecek mesaj:", None))
        self.label_31.setText(_translate("MainWindow", "Kelime yasağı kaldırıldığında gösterilecek mesaj:", None))
        self.label_32.setText(_translate("MainWindow", "Uygulama Teması", None))
        self.pushButton_16.setText(_translate("MainWindow", "Uygula", None))
        self.label_33.setText(_translate("MainWindow", "Genel", None))
        self.label_37.setText(_translate("MainWindow", "Pardus Gözcü\'yü bilgisayarın her açılışından başlat", None))
        self.label_38.setText(_translate("MainWindow", "Sistem kayıtlarında değişiklik yapılan dosyaları son ", None))
        self.label_39.setText(_translate("MainWindow", "gün için görüntüle.", None))
        self.pushButton_18.setText(_translate("MainWindow", "Uygula", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Ayarlar", None))
	#
        self.menuYard_m.setTitle(_translate("MainWindow", "Yardım", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionYard_m_Konular.setText(_translate("MainWindow", "Yardım Konuları", None))
        self.actionHakk_nda.setText(_translate("MainWindow", "Hakkında", None))
	self.actionAyarlar.setText(_translate("MainWindow", "Ayarlar", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
