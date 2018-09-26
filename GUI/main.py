# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Proj\Main\main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from borrow import Ui_borrow
from back1 import Ui_back1

class Ui_main(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_borrow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def openWindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_back1()
        self.ui.setupUi(self.window)
        self.window.show()

        
        
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.First = QtWidgets.QLabel(self.centralwidget)
        self.First.setGeometry(QtCore.QRect(210, 40, 411, 111))
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
        self.First.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("AR BONNIE")
        font.setPointSize(20)
        font.setUnderline(True)
        self.First.setFont(font)
        self.First.setObjectName("First")
        self.rt = QtWidgets.QPushButton(self.centralwidget)
        self.rt.setGeometry(QtCore.QRect(460, 300, 141, 51))
        self.rt.setObjectName("rt")

        self.rt.clicked.connect(self.openWindow1)
        
        self.br = QtWidgets.QPushButton(self.centralwidget)
        self.br.setGeometry(QtCore.QRect(170, 310, 151, 51))
        self.br.setObjectName("br")
        
        self.br.clicked.connect(self.openWindow)
        
        main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "MainWindow"))
        self.First.setText(_translate("main", "CISCO BORROWING SYSTEM "))
        self.rt.setText(_translate("main", "RETURN"))
        self.br.setText(_translate("main", "BORROW"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())

