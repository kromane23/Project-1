from calendar import TUESDAY
import sys
from turtle import onclick
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from readinglog import *


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
        self.books =[]
        self.pages =[]
        labelMove = 125
        txtMove = 125


        for l in labels:
            label = QLabel(self)
            label.setText(l)
            label.move(5, labelMove)
            txt = QLineEdit(self)
            txt.resize (40,30)
            txt.setText ("0")
            txt.move(150, txtMove)
            self.txts.append(txt)
            label.setFont(font)
            txt = QLineEdit(self)
            txt.resize (300,30)
            txt.move(300, txtMove)
            self.books.append (txt)
            txt = QLineEdit(self)
            txt.resize (60,30)
            txt.move(700,txtMove)
            txt.setText("0")
            self.pages.append (txt)
            labelMove = labelMove + 60
            txtMove = txtMove + 60

        txt= QLineEdit (self)
        txt.resize (40,30)
        txt.move (145,575)

        self.btn = QPushButton(self)
        self.btn.move(690,575)
        self.btn.setText("Submit")

        self.btn.clicked.connect(self.submitdata)
    
    def getminutes(self):
        self.Monday= self.txts[0].text()
        self.Tuesday= self.txts[1].text()
        self.Wednesday=self.txts[2].text()
        self.Thursday=self.txts[3].text()
        self.Friday=self.txts[4].text()
        self.Saturday=self.txts[5].text()
        self.Sunday=self.txts[6].text()
        
    def getbooks (self):
        self.monbooks= self.books [0].text()
        self.tuesbooks= self.books [1].text ()
        self.wedbooks= self.books [2].text ()
        self.thursbooks= self.books [3].text ()
        self.fribooks= self.books [4].text ()
        self.satbooks = self.books [5].text ()
        self.sunbooks =self.books [6].text ()
    
    def getpages (self):
        self.monpages= self.pages [0].text()
        self.tuespages= self.pages [1].text ()
        self.wedpages= self.pages [2].text ()
        self.thurspages= self.pages [3].text ()
        self.fripages= self.pages [4].text ()
        self.satpages = self.pages [5].text ()
        self.sunpages =self.pages [6].text ()

    def submitdata (self):
        self.getminutes ()
        self.getbooks ()
        self.getpages()
        print ('minutes Mon:'+self.Monday+' Tues:  '+ self.Tuesday+' Wed:  '+ self.Wednesday+' Thurs: '+self.Thursday+' Friday: '+self.Friday+' Sat: '+self.Saturday+' Sun: '+self.Sunday) 
        print ('titleMon:'+self.monbooks+' Tues:  '+ self.tuesbooks+' Wed:  '+ self.wedbooks+' Thurs: '+self.thursbooks+' Friday: '+self.fribooks+' Sat: '+self.satbooks+' Sun: '+self.sunbooks)
        print ('pagesMon:'+self.monpages+' Tues:  '+ self.tuespages+' Wed:  '+ self.wedpages+' Thurs: '+self.thurspages+' Friday: '+self.fripages+' Sat: '+self.satpages+' Sun: '+self.sunpages)


        minutesread = [int(self.Monday), int(self.Tuesday), int(self.Wednesday), int(self.Thursday), int(self.Friday), int(self.Saturday), int(self.Sunday)]
        booksread =[(self.monbooks),(self.tuesbooks),(self.wedbooks),(self.thursbooks),(self.fribooks),(self.satbooks),(self.sunbooks)]
        pagesread=[int(self.monpages), int(self.tuespages),int(self.wedpages),int(self.thurspages),int(self.fripages), int(self.satpages),int(self.sunpages)]
        rl=readinglog(booksread, minutesread,pagesread)
        rl.savetofile ()


def main():
    app = QApplication(sys.argv)
    w = mainwindow()
    w.show ()           
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

onclick()
rl=readinglog(booksread, minutesread,pagesread)
rl.savetofile
