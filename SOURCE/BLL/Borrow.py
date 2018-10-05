# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Rachel Abbie Fernand\Documents\1Q1819\COE125\Project\Borrow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Borrow1 import Ui_BorrowForm1
import sqlite3



class Ui_BorrowForm(object):
    
    def setupUi(self, BorrowForm):
        BorrowForm.setObjectName("BorrowForm")
        BorrowForm.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(BorrowForm)
        self.centralwidget.setObjectName("centralwidget")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(340, 430, 112, 34))
        self.BackButton.setObjectName("BackButton")
        self.OkButton = QtWidgets.QPushButton(self.centralwidget)
        self.OkButton.setGeometry(QtCore.QRect(480, 430, 112, 34))
        self.OkButton.setObjectName("OkButton")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 10, 411, 111))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("AR BONNIE")
        font.setPointSize(20)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(190, 80, 561, 111))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_7.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(36)
        font.setUnderline(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.line0 = QtWidgets.QLineEdit(self.centralwidget)
        self.line0.setGeometry(QtCore.QRect(340, 220, 281, 25))
        self.line0.setObjectName("line0")
        self.line1 = QtWidgets.QLineEdit(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(340, 260, 281, 25))
        self.line1.setObjectName("line1")
        self.line2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(340, 300, 281, 25))
        self.line2.setObjectName("line2")
        self.line3 = QtWidgets.QLineEdit(self.centralwidget)
        self.line3.setGeometry(QtCore.QRect(340, 340, 281, 25))
        self.line3.setObjectName("line3")
        self.line4 = QtWidgets.QLineEdit(self.centralwidget)
        self.line4.setGeometry(QtCore.QRect(340, 380, 281, 25))
        self.line4.setObjectName("line4")
        self.Name = QtWidgets.QLabel(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(180, 220, 68, 19))
        self.Name.setObjectName("Name")
        self.StudNum = QtWidgets.QLabel(self.centralwidget)
        self.StudNum.setGeometry(QtCore.QRect(180, 260, 141, 19))
        self.StudNum.setObjectName("StudNum")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 300, 131, 19))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 340, 68, 19))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 380, 68, 19))
        self.label_4.setObjectName("label_4")
        BorrowForm.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BorrowForm)
        self.statusbar.setObjectName("statusbar")
        BorrowForm.setStatusBar(self.statusbar)

        self.OkButton.clicked.connect(self.openBorrowForm1)

        self.OkButton.setDisabled(True)
        self.line0.textChanged.connect(self.disableButton)
        self.line1.textChanged.connect(self.disableButton)
        self.line2.textChanged.connect(self.disableButton)
        self.line3.textChanged.connect(self.disableButton)
        self.line4.textChanged.connect(self.disableButton)
        self.OkButton.clicked.connect(self.database)
        
        self.OkButton.clicked.connect(self.openBorrowForm1)
        
        self.retranslateUi(BorrowForm)
        QtCore.QMetaObject.connectSlotsByName(BorrowForm)

    def retranslateUi(self, BorrowForm):
        _translate = QtCore.QCoreApplication.translate
        BorrowForm.setWindowTitle(_translate("BorrowForm", "SecondWindow"))
        self.BackButton.setText(_translate("BorrowForm", "BACK"))
        self.OkButton.setText(_translate("BorrowForm", "OK"))
        self.label_2.setText(_translate("BorrowForm", "CISCO BORROWING SYSTEM "))
        self.label_7.setText(_translate("BorrowForm", "B O R R O W"))
        self.Name.setText(_translate("BorrowForm", "Name:"))
        self.StudNum.setText(_translate("BorrowForm", "Student Number:"))
        self.label.setText(_translate("BorrowForm", "Course/Section:"))
        self.label_3.setText(_translate("BorrowForm", "Room:"))
        self.label_4.setText(_translate("BorrowForm", "Professor:"))

    def database(self):
        conn = sqlite3.connect('StudentInfo.db')
        with conn:
            c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS users2 (First text,StudentNumber text,Course text, Room text, Professor text)""")
        c.execute("INSERT INTO users2 VALUES (:First, :StudentNumber, :Course, :Room, :Professor)",
              {'First': self.line0.text(), 'StudentNumber': self.line1.text(), 'Course': self.line2.text(), 'Room': self.line3.text(), 'Professor': self.line4.text()})
        conn.commit()

    def disableButton(self):
        if len(self.line0.text())>0 and len(self.line1.text())>0 and len(self.line2.text())>0 and len(self.line3.text())>0 and len(self.line4.text())>0:
            self.OkButton.setDisabled(False)
        else:
            self.OkButton.setDisabled(True)
            
    def openBorrowForm1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_BorrowForm1()
        self.ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BorrowForm = QtWidgets.QMainWindow()
    ui = Ui_BorrowForm()
    ui.setupUi(BorrowForm)
    BorrowForm.show()
    sys.exit(app.exec_())

