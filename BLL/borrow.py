# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Proj\Main\borrow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from borrow1 import Ui_borrow1
import sqlite3

class Ui_borrow(object):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_borrow1()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, borrow):
        borrow.setObjectName("borrow")
        borrow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(borrow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(290, 300, 241, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 180, 131, 19))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 300, 131, 19))
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 140, 61, 19))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 180, 241, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 50, 411, 111))
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 360, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 220, 131, 19))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 220, 241, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 260, 241, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 260, 131, 19))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 140, 241, 25))
        self.lineEdit.setObjectName("lineEdit")
        borrow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(borrow)
        self.statusbar.setObjectName("statusbar")
        borrow.setStatusBar(self.statusbar)
        
        self.pushButton.setDisabled(True)
        self.lineEdit.textChanged.connect(self.disableButton)
        self.lineEdit_2.textChanged.connect(self.disableButton)
        self.lineEdit_3.textChanged.connect(self.disableButton)
        self.lineEdit_4.textChanged.connect(self.disableButton)
        self.lineEdit_5.textChanged.connect(self.disableButton)
        self.pushButton.clicked.connect(self.database)
        self.pushButton.clicked.connect(self.openWindow)

        self.retranslateUi(borrow)
        QtCore.QMetaObject.connectSlotsByName(borrow)

    def retranslateUi(self, borrow):
        _translate = QtCore.QCoreApplication.translate
        borrow.setWindowTitle(_translate("borrow", "MainWindow"))
        self.label_3.setText(_translate("borrow", "Student Number: "))
        self.label_6.setText(_translate("borrow", "Professor:"))
        self.label.setText(_translate("borrow", "Name:"))
        self.label_2.setText(_translate("borrow", "CISCO BORROWING SYSTEM "))
        self.pushButton.setText(_translate("borrow", "OK"))
        self.label_4.setText(_translate("borrow", "Section/Subject:"))
        self.label_5.setText(_translate("borrow", "Room:"))

    def database(self):
        conn = sqlite3.connect('StudentTable2.db')
        with conn:
            c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS users2 (First text,StudentNumber text,Course text, Room text, Professor text)""")
        c.execute("INSERT INTO users2 VALUES (:First, :StudentNumber, :Course, :Room, :Professor)",
              {'First': self.lineEdit.text(), 'StudentNumber': self.lineEdit_2.text(), 'Course': self.lineEdit_3.text(), 'Room': self.lineEdit_4.text(), 'Professor': self.lineEdit_5.text()})
        conn.commit()
        
    def disableButton(self):
        if len(self.lineEdit.text())>0 and len(self.lineEdit_2.text())>0 and len(self.lineEdit_3.text())>0 and len(self.lineEdit_4.text())>0 and len(self.lineEdit_5.text())>0:
            self.pushButton.setDisabled(False)
        else:
            self.pushButton.setDisabled(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    borrow = QtWidgets.QMainWindow()
    ui = Ui_borrow()
    ui.setupUi(borrow)
    borrow.show()
    sys.exit(app.exec_())

