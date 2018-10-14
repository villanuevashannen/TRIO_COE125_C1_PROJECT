from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIntValidator
from Student1 import Student
import sqlite3

conn = sqlite3.connect('CiscoLab.db')
with conn:
    c = conn.cursor()
    
class Ui_BorrowForm(object):
    ctr = 0
    existctr = 0
    sn = ''
    def setupUi(self, BorrowForm):
        BorrowForm.setObjectName("BorrowForm")
        BorrowForm.resize(800, 600)
        BorrowForm.setEnabled(True)
        BorrowForm.setMinimumSize(QtCore.QSize(800, 600))
        BorrowForm.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(BorrowForm)
        self.centralwidget.setObjectName("centralwidget")
        self.labelName = QtWidgets.QLabel(self.centralwidget)
        self.labelName.setGeometry(QtCore.QRect(140, 230, 68, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelName.setFont(font)
        self.labelName.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelName.setObjectName("labelName")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(-560, 350, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.line0 = QtWidgets.QLineEdit(self.centralwidget)
        self.line0.setGeometry(QtCore.QRect(330, 190, 331, 25))
        self.line0.setObjectName("line0")
        self.labelStudNum = QtWidgets.QLabel(self.centralwidget)
        self.labelStudNum.setGeometry(QtCore.QRect(140, 190, 161, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelStudNum.setFont(font)
        self.labelStudNum.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelStudNum.setObjectName("labelStudNum")
        self.line1 = QtWidgets.QLineEdit(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(330, 230, 331, 25))
        self.line1.setObjectName("line1")
        self.line2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(330, 270, 331, 25))
        self.line2.setObjectName("line2")
        self.line3 = QtWidgets.QLineEdit(self.centralwidget)
        self.line3.setGeometry(QtCore.QRect(330, 310, 331, 25))
        self.line3.setObjectName("line3")
        self.line4 = QtWidgets.QLineEdit(self.centralwidget)
        self.line4.setGeometry(QtCore.QRect(330, 350, 331, 25))
        self.line4.setObjectName("line4")
        self.labelSection = QtWidgets.QLabel(self.centralwidget)
        self.labelSection.setGeometry(QtCore.QRect(140, 270, 161, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelSection.setFont(font)
        self.labelSection.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelSection.setObjectName("labelSection")
        self.labelRoom = QtWidgets.QLabel(self.centralwidget)
        self.labelRoom.setGeometry(QtCore.QRect(140, 310, 101, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelRoom.setFont(font)
        self.labelRoom.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelRoom.setObjectName("labelRoom")
        self.labelProf = QtWidgets.QLabel(self.centralwidget)
        self.labelProf.setGeometry(QtCore.QRect(140, 350, 161, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelProf.setFont(font)
        self.labelProf.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelProf.setObjectName("labelProf")
        self.clearbtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearbtn.setGeometry(QtCore.QRect(300, 420, 95, 40))
        self.clearbtn.setText("")
        self.clearbtn.setFlat(True)
        self.clearbtn.setObjectName("clearbtn")
        
        self.clearbtn.setStyleSheet("QPushButton {background-image: url(button_clear.png) 0 0 0 0 stretch stretch; }")
        
        self.Okbtn = QtWidgets.QPushButton(self.centralwidget)
        self.Okbtn.setGeometry(QtCore.QRect(440, 420, 61, 40))
        self.Okbtn.setText("")
        self.Okbtn.setFlat(True)
        self.Okbtn.setObjectName("Okbtn")
        
        self.Okbtn.setStyleSheet("QPushButton {background-image: url(button_ok.png) 0 0 0 0 stretch stretch; }")
        
        self.cancelbtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelbtn.setGeometry(QtCore.QRect(550, 420, 111, 40))
        self.cancelbtn.setText("")
        self.cancelbtn.setFlat(True)
        self.cancelbtn.setObjectName("cancelbtn")
        
        self.cancelbtn.setStyleSheet("QPushButton {background-image: url(button_cancel.png) 0 0 0 0 stretch stretch; }")
        
        BorrowForm.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BorrowForm)
        self.statusbar.setObjectName("statusbar")
        BorrowForm.setStatusBar(self.statusbar)

        BorrowForm.setStyleSheet("#BorrowForm { background-image: url(Borrow.jpg) 0 0 0 0 stretch stretch; }")
        self.retranslateUi(BorrowForm)
        QtCore.QMetaObject.connectSlotsByName(BorrowForm)

        self.onlyInt = QIntValidator()
        self.line0.setValidator(self.onlyInt)
        self.line0.textChanged.connect(self.checkIfExist)
        self.clearbtn.clicked.connect(self.clear)


    def retranslateUi(self, BorrowForm):
        _translate = QtCore.QCoreApplication.translate
        BorrowForm.setWindowTitle(_translate("BorrowForm", "Borrow"))
        self.labelName.setText(_translate("BorrowForm", "Name:"))
        self.labelStudNum.setText(_translate("BorrowForm", "Student Number: "))
        self.labelSection.setText(_translate("BorrowForm", "Section:"))
        self.labelRoom.setText(_translate("BorrowForm", "Room:"))
        self.labelProf.setText(_translate("BorrowForm", "Professor"))

    def checkIfExist(self):
        c.execute("SELECT * FROM StudentInfo WHERE StudentNumber=:sn", {'sn':self.line0.text()})
        info = c.fetchone()
        if info is not None:
            self.line1.setText(info[0])
            self.line2.setText(info[2])
            self.line3.setText(info[3])
            self.line4.setText(info[4])
            self.existctr = 1
        else:
            self.line1.setText('')
            self.line2.setText('')
            self.line3.setText('')
            self.line4.setText('')
            self.existctr = 0

    def addStud(self):
        if self.existctr == 0:
            if len(self.line0.text())>0 and len(self.line1.text())>0 and len(self.line2.text())>0 and len(self.line3.text())>0 and len(self.line4.text())>0:
                self.stud = Student(self.line1.text(), self.line0.text(), self.line2.text(), self.line3.text(), self.line4.text())
                Student.addStudInfo(self.stud)
                self.sn = self.line0.text()
                self.ctr = 1
                self.clear()
            else:
                QMessageBox.about(self, "Warning", "Input the required information.")
                self.ctr = 0
        else:
            self.sn = self.line0.text()
            self.ctr = 1
            self.clear()

    def clear(self):
        self.line0.setText('')
        self.line1.setText('')
        self.line2.setText('')
        self.line3.setText('')
        self.line4.setText('')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BorrowForm = QtWidgets.QMainWindow()
    ui = Ui_BorrowForm()
    ui.setupUi(BorrowForm)
    BorrowForm.show()
    sys.exit(app.exec_())

