# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Rachel Abbie Fernand\Documents\1Q1819\COE125\Copy\Ret.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_BackForm(object):
    def setupUi(self, BackForm):
        BackForm.setObjectName("BackForm")
        BackForm.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(BackForm)
        self.centralwidget.setObjectName("centralwidget")
        self.confrimbtn = QtWidgets.QPushButton(self.centralwidget)
        self.confrimbtn.setGeometry(QtCore.QRect(460, 440, 112, 34))
        self.confrimbtn.setObjectName("confrimbtn")
        self.LineStudNum = QtWidgets.QLineEdit(self.centralwidget)
        self.LineStudNum.setGeometry(QtCore.QRect(300, 170, 261, 25))
        self.LineStudNum.setObjectName("LineStudNum")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 170, 131, 19))
        self.label_3.setObjectName("label_3")
        self.Okbtn = QtWidgets.QPushButton(self.centralwidget)
        self.Okbtn.setGeometry(QtCore.QRect(450, 200, 112, 34))
        self.Okbtn.setObjectName("Okbtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 300, 401, 121))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 10, 411, 111))
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
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 80, 251, 81))
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
        self.label_8.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        font.setUnderline(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        BackForm.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BackForm)
        self.statusbar.setObjectName("statusbar")
        BackForm.setStatusBar(self.statusbar)
        
        self.Okbtn.setDisabled(True)
        self.confrimbtn.setDisabled(True)
        self.LineStudNum.textChanged.connect(self.disableButton)
        
        
        self.Okbtn.clicked.connect(self.search)
        self.confrimbtn.clicked.connect(self.remove)

        self.retranslateUi(BackForm)
        QtCore.QMetaObject.connectSlotsByName(BackForm)

    def retranslateUi(self, BackForm):
        _translate = QtCore.QCoreApplication.translate
        BackForm.setWindowTitle(_translate("BackForm", "Return Equipment"))
        self.confrimbtn.setText(_translate("BackForm", "CONFIRM"))
        self.label_3.setText(_translate("BackForm", "Student Number: "))
        self.Okbtn.setText(_translate("BackForm", "OK"))
        self.label.setText(_translate("BackForm", "show"))
        self.label_2.setText(_translate("BackForm", "CISCO BORROWING SYSTEM "))
        self.label_8.setText(_translate("BackForm", "R E T U R N"))

    def search(self):
        conn = sqlite3.connect('StudentInfo.db')
        with conn:
            c = conn.cursor()
        c.execute("SELECT * FROM users2 WHERE StudentNumber=:sn", {'sn':self.LineStudNum.text()})
        info = c.fetchall()
        for row in info:
            name = row[0]
            sn = row[1]
            subj = row[2]
            room = row[3]
            prof = row[4]
        self.label.setText(name+" "+sn+"/n"+subj+"/n"+room+"/n"+prof)    
            
    def remove(self):
        conn = sqlite3.connect('StudentInfo.db')
        with conn:
            c = conn.cursor()
        c.execute("DELETE FROM users2 WHERE StudentNumber=:sn", {'sn':self.LineStudNum.text()})
        conn.commit()
        self.label.setText("Return Successful")
        
    def disableButton(self):
        if len(self.LineStudNum.text())>0:
            self.Okbtn.setDisabled(False)
            self.confrimbtn.setDisabled(False)
        else:
            self.Okbtn.setDisabled(True)
            self.confrimbtn.setDisabled(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BackForm = QtWidgets.QMainWindow()
    ui = Ui_BackForm()
    ui.setupUi(BackForm)
    BackForm.show()
    sys.exit(app.exec_())

