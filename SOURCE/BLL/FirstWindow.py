# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Rachel Abbie Fernand\Documents\1Q1819\COE125\Project\FirstWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Borrow import Ui_BorrowForm
from Ret import Ui_BackForm

class Ui_FirstForm(object):

    def openBorrowForm(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_BorrowForm()
        self.ui.setupUi(self.window)
        self.window.show()
        FirstForm.close()
        
    def openBackForm(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_BackForm()
        self.ui.setupUi(self.window)
        self.window.show()
        #FirstForm.close()

    
    def setupUi(self, FirstForm):
        FirstForm.setObjectName("FirstForm")
        FirstForm.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(FirstForm)
        self.centralwidget.setObjectName("centralwidget")
        self.BorrowBttn = QtWidgets.QPushButton(self.centralwidget)
        self.BorrowBttn.setGeometry(QtCore.QRect(170, 320, 181, 71))
        font = QtGui.QFont()
        font.setFamily("AR BONNIE")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.BorrowBttn.setFont(font)
        self.BorrowBttn.setObjectName("BorrowBttn")

        self.BorrowBttn.clicked.connect(self.openBorrowForm)
        
        self.ReturnBttn = QtWidgets.QPushButton(self.centralwidget)
        self.ReturnBttn.setGeometry(QtCore.QRect(420, 320, 181, 71))
        font = QtGui.QFont()
        font.setFamily("AR BONNIE")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ReturnBttn.setFont(font)
        self.ReturnBttn.setObjectName("ReturnBttn")
        
        self.ReturnBttn.clicked.connect(self.openBackForm)
        
        self.MainForm = QtWidgets.QLabel(self.centralwidget)
        self.MainForm.setGeometry(QtCore.QRect(40, 50, 761, 111))
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
        self.MainForm.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(25)
        font.setUnderline(True)
        self.MainForm.setFont(font)
        self.MainForm.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.MainForm.setObjectName("MainForm")
        FirstForm.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FirstForm)
        self.statusbar.setObjectName("statusbar")
        FirstForm.setStatusBar(self.statusbar)

        self.retranslateUi(FirstForm)
        QtCore.QMetaObject.connectSlotsByName(FirstForm)

    def retranslateUi(self, FirstForm):
        _translate = QtCore.QCoreApplication.translate
        self.BorrowBttn.setText(_translate("FirstForm", "BORROW"))
        self.ReturnBttn.setText(_translate("FirstForm", "RETURN"))
        self.MainForm.setText(_translate("FirstForm", "CISCO BORROWING SYSTEM "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FirstForm = QtWidgets.QMainWindow()
    ui = Ui_FirstForm()
    ui.setupUi(FirstForm)
    FirstForm.show()
    sys.exit(app.exec_())

