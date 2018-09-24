# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Proj\Main\back1.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_back1(object):
    def setupUi(self, back1):
        back1.setObjectName("back1")
        back1.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(back1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 260, 401, 121))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 200, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 150, 261, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 160, 131, 19))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 20, 411, 111))
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
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 400, 112, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        back1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(back1)
        self.statusbar.setObjectName("statusbar")
        back1.setStatusBar(self.statusbar)
        
        self.pushButton.setDisabled(True)
        self.pushButton_2.setDisabled(True)
        self.lineEdit_2.textChanged.connect(self.disableButton)

        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.remove)
        

        self.retranslateUi(back1)
        QtCore.QMetaObject.connectSlotsByName(back1)

    def retranslateUi(self, back1):
        _translate = QtCore.QCoreApplication.translate
        back1.setWindowTitle(_translate("back1", "MainWindow"))
        self.label.setText(_translate("back1", "show"))
        self.pushButton.setText(_translate("back1", "OK"))
        self.label_3.setText(_translate("back1", "Student Number: "))
        self.label_2.setText(_translate("back1", "CISCO BORROWING SYSTEM "))
        self.pushButton_2.setText(_translate("back1", "CONFIRM"))
    
    def search(self):
        conn = sqlite3.connect('StudentTable2.db')
        with conn:
            c = conn.cursor()
        c.execute("SELECT * FROM users2 WHERE StudentNumber=:sn", {'sn':self.lineEdit_2.text()})
        info = c.fetchall()
        for row in info:
            name = row[0]
            sn = row[1]
            subj = row[2]
            room = row[3]
            prof = row[4]
        self.label.setText(name+sn+subj+room+prof)    
        #if info is not None:  
        #else:
            #self.label.setText("Not Found!")
            
    def remove(self):
        conn = sqlite3.connect('StudentTable2.db')
        with conn:
            c = conn.cursor()
        c.execute("DELETE FROM users2 WHERE StudentNumber=:sn", {'sn':self.lineEdit_2.text()})
        conn.commit()
        self.label.setText("Return Successful")
        
    def disableButton(self):
        if len(self.lineEdit_2.text())>0:
            self.pushButton.setDisabled(False)
            self.pushButton_2.setDisabled(False)
        else:
            self.pushButton.setDisabled(True)
            self.pushButton_2.setDisabled(True)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    back1 = QtWidgets.QMainWindow()
    ui = Ui_back1()
    ui.setupUi(back1)
    back1.show()
    sys.exit(app.exec_())

