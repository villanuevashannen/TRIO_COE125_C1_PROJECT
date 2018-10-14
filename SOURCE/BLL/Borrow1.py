from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIntValidator
from Inventory import Inventory
import sqlite3

conn = sqlite3.connect('CiscoLab.db')
with conn:
    c = conn.cursor()

class Ui_BorrowForm1(object):
    ctr = 0
    warningctr = 0
    def setupUi(self, BorrowForm1):
        BorrowForm1.setObjectName("BorrowForm1")
        BorrowForm1.resize(800, 600)
        BorrowForm1.setEnabled(True)
        BorrowForm1.setMinimumSize(QtCore.QSize(800, 600))
        BorrowForm1.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(BorrowForm1)
        self.centralwidget.setObjectName("centralwidget")
        self.labelQuantity = QtWidgets.QLabel(self.centralwidget)
        self.labelQuantity.setGeometry(QtCore.QRect(510, 260, 151, 19))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelQuantity.setFont(font)
        self.labelQuantity.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelQuantity.setObjectName("labelQuantity")
        self.labelItem = QtWidgets.QLabel(self.centralwidget)
        self.labelItem.setGeometry(QtCore.QRect(220, 260, 68, 19))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelItem.setFont(font)
        self.labelItem.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelItem.setObjectName("labelItem")
        self.cb0 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb0.setGeometry(QtCore.QRect(220, 300, 101, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cb0.setFont(font)
        self.cb0.setStyleSheet("color: rgb(255, 255, 255);")
        self.cb0.setObjectName("cb0")
        self.l0 = QtWidgets.QLineEdit(self.centralwidget)
        self.l0.setGeometry(QtCore.QRect(530, 300, 51, 25))
        self.l0.setObjectName("l0")
        self.cb1 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb1.setGeometry(QtCore.QRect(220, 330, 101, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cb1.setFont(font)
        self.cb1.setStyleSheet("color: rgb(255, 255, 255);")
        self.cb1.setObjectName("cb1")
        self.l1 = QtWidgets.QLineEdit(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(530, 330, 51, 25))
        self.l1.setObjectName("l1")
        self.cb2 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb2.setGeometry(QtCore.QRect(220, 360, 101, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cb2.setFont(font)
        self.cb2.setStyleSheet("color: rgb(255, 255, 255);")
        self.cb2.setObjectName("cb2")
        self.l2 = QtWidgets.QLineEdit(self.centralwidget)
        self.l2.setGeometry(QtCore.QRect(530, 360, 51, 25))
        self.l2.setObjectName("l2")
        self.cb3 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb3.setGeometry(QtCore.QRect(220, 390, 151, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cb3.setFont(font)
        self.cb3.setStyleSheet("color: rgb(255, 255, 255);")
        self.cb3.setObjectName("cb3")
        self.l3 = QtWidgets.QLineEdit(self.centralwidget)
        self.l3.setGeometry(QtCore.QRect(530, 390, 51, 25))
        self.l3.setObjectName("l3")
        self.cb4 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb4.setGeometry(QtCore.QRect(220, 420, 121, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cb4.setFont(font)
        self.cb4.setStyleSheet("color: rgb(255, 255, 255);")
        self.cb4.setObjectName("cb4")
        self.l4 = QtWidgets.QLineEdit(self.centralwidget)
        self.l4.setGeometry(QtCore.QRect(530, 420, 51, 25))
        self.l4.setObjectName("l4")
        self.cb5 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb5.setGeometry(QtCore.QRect(220, 450, 141, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cb5.setFont(font)
        self.cb5.setStyleSheet("color: rgb(255, 255, 255);")
        self.cb5.setObjectName("cb5")
        self.l5 = QtWidgets.QLineEdit(self.centralwidget)
        self.l5.setGeometry(QtCore.QRect(530, 450, 51, 25))
        self.l5.setObjectName("l5")
        self.labelName = QtWidgets.QLabel(self.centralwidget)
        self.labelName.setGeometry(QtCore.QRect(30, 150, 331, 19))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelName.setFont(font)
        self.labelName.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelName.setObjectName("labelName")
        self.labelStudNum = QtWidgets.QLabel(self.centralwidget)
        self.labelStudNum.setGeometry(QtCore.QRect(30, 180, 331, 19))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelStudNum.setFont(font)
        self.labelStudNum.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelStudNum.setObjectName("labelStudNum")
        self.labelSection = QtWidgets.QLabel(self.centralwidget)
        self.labelSection.setGeometry(QtCore.QRect(370, 150, 181, 19))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelSection.setFont(font)
        self.labelSection.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelSection.setObjectName("labelSection")
        self.labelRoom = QtWidgets.QLabel(self.centralwidget)
        self.labelRoom.setGeometry(QtCore.QRect(370, 180, 181, 19))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelRoom.setFont(font)
        self.labelRoom.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelRoom.setObjectName("labelRoom")
        self.labelRoom_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelRoom_2.setGeometry(QtCore.QRect(550, 150, 241, 19))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelRoom_2.setFont(font)
        self.labelRoom_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelRoom_2.setObjectName("labelRoom_2")
        self.labelAvailable = QtWidgets.QLabel(self.centralwidget)
        self.labelAvailable.setGeometry(QtCore.QRect(340, 260, 151, 19))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelAvailable.setFont(font)
        self.labelAvailable.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelAvailable.setObjectName("labelAvailable")
        self.a0 = QtWidgets.QLabel(self.centralwidget)
        self.a0.setGeometry(QtCore.QRect(400, 300, 68, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.a0.setFont(font)
        self.a0.setStyleSheet("color: rgb(255, 255, 255);")
        self.a0.setObjectName("a0")
        self.a1 = QtWidgets.QLabel(self.centralwidget)
        self.a1.setGeometry(QtCore.QRect(400, 330, 68, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.a1.setFont(font)
        self.a1.setStyleSheet("color: rgb(255, 255, 255);")
        self.a1.setObjectName("a1")
        self.a2 = QtWidgets.QLabel(self.centralwidget)
        self.a2.setGeometry(QtCore.QRect(400, 360, 68, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.a2.setFont(font)
        self.a2.setStyleSheet("color: rgb(255, 255, 255);")
        self.a2.setObjectName("a2")
        self.a3 = QtWidgets.QLabel(self.centralwidget)
        self.a3.setGeometry(QtCore.QRect(400, 390, 68, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.a3.setFont(font)
        self.a3.setStyleSheet("color: rgb(255, 255, 255);")
        self.a3.setObjectName("a3")
        self.a4 = QtWidgets.QLabel(self.centralwidget)
        self.a4.setGeometry(QtCore.QRect(400, 420, 68, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.a4.setFont(font)
        self.a4.setStyleSheet("color: rgb(255, 255, 255);")
        self.a4.setObjectName("a4")
        self.a5 = QtWidgets.QLabel(self.centralwidget)
        self.a5.setGeometry(QtCore.QRect(400, 450, 71, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.a5.setFont(font)
        self.a5.setStyleSheet("color: rgb(255, 255, 255);")
        self.a5.setObjectName("a5")
        self.clearbtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearbtn.setGeometry(QtCore.QRect(250, 500, 95, 40))
        self.clearbtn.setText("")
        self.clearbtn.setFlat(True)
        self.clearbtn.setObjectName("clearbtn")
        
        self.clearbtn.setStyleSheet("QPushButton {background-image: url(button_clear.png) 0 0 0 0 stretch stretch; }")
        
        self.cancelbtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelbtn.setGeometry(QtCore.QRect(560, 500, 111, 40))
        self.cancelbtn.setText("")
        self.cancelbtn.setFlat(True)
        self.cancelbtn.setObjectName("cancelbtn")
        
        self.cancelbtn.setStyleSheet("QPushButton {background-image: url(button_cancel.png) 0 0 0 0 stretch stretch; }")
        
        self.borrowbtn = QtWidgets.QPushButton(self.centralwidget)
        self.borrowbtn.setGeometry(QtCore.QRect(390, 500, 126, 40))
        self.borrowbtn.setText("")
        self.borrowbtn.setFlat(True)
        self.borrowbtn.setObjectName("borrowbtn")
        
        self.borrowbtn.setStyleSheet("QPushButton {background-image: url(button_borrow.png) 0 0 0 0 stretch stretch; }")
        
        
        BorrowForm1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BorrowForm1)
        self.statusbar.setObjectName("statusbar")
        BorrowForm1.setStatusBar(self.statusbar)

        BorrowForm1.setStyleSheet("#BorrowForm1 { background-image: url(Borrow1.jpg) 0 0 0 0 stretch stretch; }")
        self.retranslateUi(BorrowForm1)
        QtCore.QMetaObject.connectSlotsByName(BorrowForm1)

        self.l0.setDisabled(True)
        self.l1.setDisabled(True)
        self.l2.setDisabled(True)
        self.l3.setDisabled(True)
        self.l4.setDisabled(True)
        self.l5.setDisabled(True)
        
        self.cb0.stateChanged.connect(self.ch)
        self.cb1.stateChanged.connect(self.ch)
        self.cb2.stateChanged.connect(self.ch)
        self.cb3.stateChanged.connect(self.ch)
        self.cb4.stateChanged.connect(self.ch)
        self.cb5.stateChanged.connect(self.ch) 
        
        self.onlyInt = QIntValidator()
        self.l0.setValidator(self.onlyInt)
        self.l1.setValidator(self.onlyInt)
        self.l2.setValidator(self.onlyInt)
        self.l3.setValidator(self.onlyInt)
        self.l4.setValidator(self.onlyInt)
        self.l5.setValidator(self.onlyInt)
        
        self.l0.textChanged.connect(self.checkLength)
        self.l1.textChanged.connect(self.checkLength)
        self.l2.textChanged.connect(self.checkLength)
        self.l3.textChanged.connect(self.checkLength)
        self.l4.textChanged.connect(self.checkLength)
        self.l5.textChanged.connect(self.checkLength)
        
        self.clearbtn.clicked.connect(self.clear)


    def retranslateUi(self, BorrowForm1):
        _translate = QtCore.QCoreApplication.translate
        BorrowForm1.setWindowTitle(_translate("BorrowForm1", "Borrow Equipment"))
        self.labelQuantity.setText(_translate("BorrowForm1", "QUANTITY"))
        self.labelItem.setText(_translate("BorrowForm1", "ITEM"))
        self.cb0.setText(_translate("BorrowForm1", "Rack"))
        self.cb1.setText(_translate("BorrowForm1", "Switch"))
        self.cb2.setText(_translate("BorrowForm1", "Router"))
        self.cb3.setText(_translate("BorrowForm1", "Console Cable"))
        self.cb4.setText(_translate("BorrowForm1", "LAN Cable"))
        self.cb5.setText(_translate("BorrowForm1", "Power Cable"))
        self.labelName.setText(_translate("BorrowForm1", "Name:"))
        self.labelStudNum.setText(_translate("BorrowForm1", "Student Number: "))
        self.labelSection.setText(_translate("BorrowForm1", "Section:"))
        self.labelRoom.setText(_translate("BorrowForm1", "Room:"))
        self.labelRoom_2.setText(_translate("BorrowForm1", "Professor:"))
        self.labelAvailable.setText(_translate("BorrowForm1", "AVAILABLE"))
        self.a0.setText(_translate("BorrowForm1", "A1"))
        self.a1.setText(_translate("BorrowForm1", "A1"))
        self.a2.setText(_translate("BorrowForm1", "A1"))
        self.a3.setText(_translate("BorrowForm1", "A1"))
        self.a4.setText(_translate("BorrowForm1", "A1"))
        self.a5.setText(_translate("BorrowForm1", "A1"))

    def checkLength(self):
        if self.cb0.isChecked():
            if len(self.l0.text()) < 0:
                self.warningctr = 1
                return
            else:
                self.warningctr = 0
        
        if self.cb1.isChecked():
            if len(self.l1.text()) < 0:
                self.warningctr = 1
                return
            else:
                self.warningctr = 0
                
        if self.cb2.isChecked():
            if len(self.l2.text()) < 0:
                self.warningctr = 1
                return
            else:
                self.warningctr = 0
                
        if self.cb3.isChecked():
            if len(self.l3.text()) < 0:
                self.warningctr = 1
                return
            else:
                self.warningctr = 0
                
        if self.cb4.isChecked():
            if len(self.l4.text()) < 0:
                self.warningctr = 1
                return
            else:
                self.warningctr = 0
                
        if self.cb5.isChecked():
            if len(self.l5.text()) < 0:
                self.warningctr = 1
                return
            else:
                self.warningctr = 0
    
    def cancelBorrow(self, sn):
        c.execute("SELECT * FROM Borrowed WHERE StudentNumber=:sn", {'sn':sn})
        stud = c.fetchone()
        if stud is not None:
            return 1
        else:
            return 0
        
    
    def showStudInfo(self):
        c.execute("SELECT * FROM StudentInfo ORDER BY rowid DESC LIMIT 1")
        stud = c.fetchone()
        self.labelName.setText("Name: " + stud[0])
        self.labelStudNum.setText("Student Number: " + stud[1])
        self.labelSection.setText("Course/Section: " + stud[2])
        self.labelRoom.setText("Room: " + stud[3])
        self.labelRoom_2.setText("Professor: " + stud[4])
        
    def showStudInfobyStudNum(self, sn):
        c.execute("SELECT * FROM StudentInfo WHERE StudentNumber=:sn", {'sn':sn})
        stud = c.fetchone()
        self.labelName.setText("Name: " + stud[0])
        self.labelStudNum.setText("Student Number: " + stud[1])
        self.labelSection.setText("Course/Section: " + stud[2])
        self.labelRoom.setText("Room: " + stud[3])
        self.labelRoom_2.setText("Professor: " + stud[4])
        
    def showAvailable(self):
        c.execute("SELECT * FROM Inventory")
        av = c.fetchall()
        self.a0.setText(str(av[0][1]))
        self.a1.setText(str(av[1][1]))
        self.a2.setText(str(av[2][1]))
        self.a3.setText(str(av[3][1]))
        self.a4.setText(str(av[4][1]))
        self.a5.setText(str(av[5][1]))
    
    def ch(self):
        if self.cb0.isChecked():
            self.l0.setDisabled(False)
        else:
            self.l0.setDisabled(True)
        
        if self.cb1.isChecked():
            self.l1.setDisabled(False)
        else:
            self.l1.setDisabled(True)
            
        if self.cb2.isChecked():
            self.l2.setDisabled(False)
        else:
            self.l2.setDisabled(True)
            
        if self.cb3.isChecked():
            self.l3.setDisabled(False)
        else:
            self.l3.setDisabled(True)
            
        if self.cb4.isChecked():
            self.l4.setDisabled(False)
        else:
            self.l4.setDisabled(True)
        
        if self.cb5.isChecked():
            self.l5.setDisabled(False)
        else:
            self.l5.setDisabled(True)
            
    def clear(self):
        self.cb0.setChecked(False)
        self.cb1.setChecked(False)
        self.cb2.setChecked(False)
        self.cb3.setChecked(False)
        self.cb4.setChecked(False)
        self.cb5.setChecked(False)
        self.l0.setText('')
        self.l1.setText('')
        self.l2.setText('')
        self.l3.setText('')
        self.l4.setText('')
        self.l5.setText('')
    
    def bor(self, studNum):
        if self.l0.isEnabled() or self.l1.isEnabled() or self.l2.isEnabled() or self.l3.isEnabled() or self.l4.isEnabled() or self.l5.isEnabled():
            if len(self.l0.text())>0 or len(self.l1.text())>0 or len(self.l2.text())>0 or len(self.l3.text())>0 or len(self.l4.text())>0 or len(self.l5.text())>0:

                if self.l0.isEnabled():
                    if len(self.l0.text())>0:
                        rack = int(self.l0.text())
                        if int(self.a0.text()) < rack:
                            self.warningctr = 1
                    else:
                        self.ctr = 0
                        QMessageBox.about(self, "Warning", "Input value for selected items.")
                        return
                else:
                    rack = 0
                
                if self.l1.isEnabled():
                    if len(self.l1.text())>0:
                        switch = int(self.l1.text())
                        if int(self.a1.text()) < switch:
                            self.warningctr = 1
                    else:
                        self.ctr = 0
                        QMessageBox.about(self, "Warning", "Input value for selected items.")
                        return
                else:
                    switch = 0
                    
                if self.l2.isEnabled():
                    if len(self.l2.text())>0:
                        router = int(self.l2.text())
                        if int(self.a2.text()) < router:
                            self.warningctr = 1
                    else:
                        self.ctr = 0
                        QMessageBox.about(self, "Warning", "Input value for selected items.")
                        return
                else:
                    router = 0
                    
                if self.l3.isEnabled():
                    if len(self.l3.text())>0:
                        con = int(self.l3.text())
                        if int(self.a3.text()) < con:
                            self.warningctr = 1
                    else:
                        self.ctr = 0
                        QMessageBox.about(self, "Warning", "Input value for selected items.")
                        return
                else:
                    con = 0
                    
                if self.l4.isEnabled():
                    if len(self.l4.text())>0:    
                        lan = int(self.l4.text())
                        if int(self.a4.text()) < lan:
                            self.warningctr = 1
                    else:
                        self.ctr = 0
                        QMessageBox.about(self, "Warning", "Input value for selected items.")
                        return
                else: 
                    lan = 0
                    
                if self.l5.isEnabled():
                    if len(self.l5.text())>0:    
                        power = int(self.l5.text())
                        if int(self.a0.text()) < power:
                            self.warningctr = 1
                    else:
                        self.ctr = 0
                        QMessageBox.about(self, "Warning", "Input value for selected items.")
                        return
                else:    
                    power = 0
                
                if self.warningctr == 0:
                    self.ctr = 1
                    inv = Inventory(studNum, rack, switch, router, con, lan, power)
                    Inventory.borrowItems(inv)
                    self.clear()
                    QMessageBox.about(self, "Cisco Borrowing System", "Borrow Success!")
                else:
                    self.ctr = 0
                    QMessageBox.about(self, "Warning", "Some items are unavailable.")

            else:
                self.ctr = 0
                QMessageBox.about(self, "Warning", "Input value for selected items.")
        else:
            self.ctr = 0
            QMessageBox.about(self, "Warning", "No items were selected.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BorrowForm1 = QtWidgets.QMainWindow()
    ui = Ui_BorrowForm1()
    ui.setupUi(BorrowForm1)
    BorrowForm1.show()
    sys.exit(app.exec_())

