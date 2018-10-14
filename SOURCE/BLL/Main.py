from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(800, 600)
        MainForm.setEnabled(True)
        MainForm.setMinimumSize(QtCore.QSize(800, 600))
        MainForm.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainForm)
        self.centralwidget.setObjectName("centralwidget")
        self.borrowbtn = QtWidgets.QPushButton(self.centralwidget)
        self.borrowbtn.setGeometry(QtCore.QRect(220, 340, 126, 40))
        self.borrowbtn.setText("")
        self.borrowbtn.setFlat(True)
        self.borrowbtn.setObjectName("borrowbtn")
        
        self.borrowbtn.setStyleSheet("QPushButton {background-image: url(button_borrow.png) 0 0 0 0 stretch stretch; }")
        
        self.returnbtn = QtWidgets.QPushButton(self.centralwidget)
        self.returnbtn.setGeometry(QtCore.QRect(420, 340, 115, 40))
        self.returnbtn.setText("")
        self.returnbtn.setFlat(True)
        self.returnbtn.setObjectName("returnbtn")
        
        self.returnbtn.setStyleSheet("QPushButton {background-image: url(button_return.png) 0 0 0 0 stretch stretch; }")
        
        MainForm.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainForm)
        self.statusbar.setObjectName("statusbar")
        MainForm.setStatusBar(self.statusbar)

        MainForm.setStyleSheet("#MainForm { background-image: url(main.jpg) 0 0 0 0 stretch stretch; }")
        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Cisco Borrowing System"))

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QMainWindow()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec_())

