from calendar import MONDAY
import sys 
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import *

class mainwindow (QWidget):  #taking functionality from Qwidget
    def __init__(self, parent =None): #constructor making a new object, parent goes within another widget
        super(mainwindow, self).__init__(parent)
        self.resize (500,200)
        self.setWindowTitle('Read Across America')

        self.lblmon= QLabel (self)
        self.lblmon.setText ('Minutes read Monday')
        self.lblmon.move(50,50)
        
        self.lbltue= QLabel (self)
        self.lbltue.setText ('Minutes read Tuesday')
        self.lbltue.move(50,100)

        font = QFont()
        font.setFamily ('Britannic')
        font.setPointSize (12)
        self.lblmon.setFont (font)
        self.lbltue.setFont (font)

        self.txtmon= QLineEdit (self)
        self.txtmon.move (250,50)
        self.txtmon.setFont(font)
        self.txtmon.resize (40,30)

        self.txttue=QLineEdit (self)
        self.txttue.setFont(font)
        self.txttue.move (250,100)
        self.txttue.resize (40,30)


        self.button=QPushButton (self)
        self.button.move (150,150)
        self.button.setText('Submit')

        self.button.clicked.connect (self.getminutes)

    def getminutes(self):
        monday=self.txtmon.text()
        tuesday= self.txttue.text()
        print (monday+ ':'+ tuesday)




def main():
    app= QApplication (sys.argv)
    w = mainwindow ()
    w.show ()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
