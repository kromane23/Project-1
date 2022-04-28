from calendar import TUESDAY
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class mainwindow(QWidget):
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)
        self.resize(800,800)
        self.setWindowTitle("Read Across America Reading Log")
        font = QFont()
        font.setFamily('Arial')
        font.setPointSize(10)
        

        label = QLabel (self)
        label.setFont (font)
        label.setText ('Read Across America Reading Challenge Februrary 14 - March 27, 2022' ' To be eleigible for a free ticket to Silverwood, students must:\n'
                        '1. Read 5 out of 7 days for 6 weeks \n' 
                        '2. K-2nd = 20 min/day 5 days/ week \n'
                        '3. Record number of mninutes read and weekly totals on the calendar. \n'
                        '4. Parent Signature at the bottom and signed form returned by Monday, March 28, 2022 \n')
        label.move (5,5)

        label =QLabel(self)
        label.setFont(font)
        label.setText('Minutes Read')
        label.move(150, 100)

        label =QLabel(self)
        label.setFont(font)
        label.setText('Total Minutes \nThis Week:')
        label.move(5, 575)
        
        label = QLabel(self)
        label.setFont(font)
        label.setText('Book Title(s)')
        label.move(300, 100)

        label = QLabel(self)
        label.setFont(font)
        label.setText('Pages')
        label.move(700, 100)


        labels = ["Monday: ", "Tuesday: ","Wednesday: ","Thursday: ","Friday: ","Saturday: ","Sunday: "]
        self.txts = []
        labelMove = 125
        txtMove = 125


        for l in labels:
            label = QLabel(self)
            label.setText(l)
            label.move(5, labelMove)
            txt = QLineEdit(self)
            txt.resize (40,30)
            txt.move(150, txtMove)
            self.txts.append(txt)
            label.setFont(font)
            txt = QLineEdit(self)
            txt.resize (300,30)
            txt.move(300, txtMove)
            txt = QLineEdit(self)
            txt.resize (60,30)
            txt.move(700,txtMove)
            labelMove = labelMove + 60
            txtMove = txtMove + 60

        txt= QLineEdit (self)
        txt.resize (40,30)
        txt.move (145,575)

        self.btn = QPushButton(self)
        self.btn.move(690,575)
        self.btn.setText("Submit")

        self.btn.clicked.connect(self.getminutes)
    
    def getminutes(self):
        Monday= self.txts[0].text()
        Tuesday= self.txts[1].text()
        Wednesday=self.txts[2].text()
        Thursday=self.txts[3].text()
        Friday=self.txts[4].text()
        Saturday=self.txts[5].text()
        Sunday=self.txts[6].text()
        

        print ('Mon:'+Monday+' Tues:  '+ Tuesday+' Wed:  '+ Wednesday+' Thurs: '+Thursday+' Friday: '+Friday+' Sat: '+Saturday+' Sun: '+Sunday)



def main():
    app = QApplication(sys.argv)
    w = mainwindow()
    w.show ()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
