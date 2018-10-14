from Main import Ui_MainForm
from Borrow import Ui_BorrowForm
from Borrow1 import Ui_BorrowForm1
from Ret import Ui_BackForm
from Student1 import Student
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow, Ui_MainForm):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
class BorrowWindow(QtWidgets.QMainWindow, Ui_BorrowForm):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
class BorrowWindow1(QtWidgets.QMainWindow, Ui_BorrowForm1):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class ReturnWindow(QtWidgets.QMainWindow, Ui_BackForm):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

def changeWindow(w1, w2):
    w1.hide()
    w2.show()  
    
def checkBorrow():
    borrow.addStud()
    if borrow.ctr == 1:
        changeWindow(borrow, borrow1)
        borrow1.showStudInfobyStudNum(borrow.sn)
        borrow1.showAvailable()
 
def checkBorrow1():
    borrow1.bor(borrow.sn)
    if borrow1.ctr == 1:
        changeWindow(borrow1, first)
        
def checkRet():
    if ret.foundctr == 1:
        ret.remove()
        changeWindow(ret,first)
    
        
def cancelBorrow():
    borrow.clear()
    changeWindow(borrow, first)

def cancelRet():
    ret.clear()
    changeWindow(ret, first)

def cancelBorrow1():
    if borrow1.cancelBorrow(borrow.sn) == 0:
        Student.removeStudInfo(borrow.sn)
    borrow1.clear()
    changeWindow(borrow1, first)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    first = MainWindow()
    borrow = BorrowWindow()
    borrow1 = BorrowWindow1()
    ret = ReturnWindow()
    
    first.borrowbtn.clicked.connect(lambda: changeWindow(first, borrow))
    first.returnbtn.clicked.connect(lambda: changeWindow(first, ret))
    
    borrow.cancelbtn.clicked.connect(lambda: cancelBorrow())
    
    #borrow.BackButton.clicked.connect(lambda: changeWindow(borrow, first))
    borrow.Okbtn.clicked.connect(lambda: checkBorrow())
    #borrow.OkButton.clicked.connect(lambda: check())

    borrow1.borrowbtn.clicked.connect(lambda: checkBorrow1())
    borrow1.cancelbtn.clicked.connect(lambda: cancelBorrow1())
    #borrow1.borrowbtn.clicked.connect(lambda: changeWindow(borrow1, first))
    
    ret.confirmbtn.clicked.connect(lambda: checkRet())
    ret.cancelbtn.clicked.connect(lambda: cancelRet())

    first.show()
    sys.exit(app.exec_())