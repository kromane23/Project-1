
import pyodbc
from calendar import TUESDAY
import sys
import os
from turtle import onclick, title
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from readinglog import *


class mainwindow(QWidget):
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)
        self.resize(900,900)
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
                        '4. Parent Signature at the bottom and signed form returned by Monday, March 28, 2022 \n ')
        label.move (5,5)

        label =QLabel(self)
        label.setFont(font)
        label.setText('Minutes Read')
        label.move(150, 100)
        summinutes=0

        if os.path.exists ("Total Minutes Read"):
            f=open ('Total Minutes Read', 'r')
            for n in f:
                summinutes= summinutes+int(n)


        label =QLabel(self)
        label.setFont(font)
        label.setText('Total Minutes \nThis Week:'+str(summinutes))
        label.move(5, 575)
        
        label = QLabel(self)
        label.setFont(font)
        label.setText('Book Title(s)')
        label.move(300, 100)

        label = QLabel(self)
        label.setFont(font)
        label.setText(' Pages ')
        label.move(700, 100)


        labels = [ " Monday: ", "Tuesday: ","Wednesday: ","Thursday: ","Friday: ","Saturday: ","Sunday: "]
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
            self.pages.append (txt)
            labelMove = labelMove + 60
            txtMove = txtMove + 60

            # txt= QLineEdit (self)
            # txt.resize (40,30)
            # txt.move (145,575)

            self.btn = QPushButton(self)
            self.btn.move(690,575)
            self.btn.setText("Submit")

            self.btn.clicked.connect(self.submitdata)

            self.txtfname = QLineEdit(self)
            self.txtfname.resize (100,30)
            self.txtfname.move(100,625)
            label = QLabel(self)
            label.setFont(font)
            label.setText('First Name')
            label.move(15,625)

            self.txtlname = QLineEdit(self)
            self.txtlname.resize (100,30)
            self.txtlname.move(350,625)
            label = QLabel(self)
            label.setFont(font)
            label.setText('Last Name')
            label.move(250,625)
    
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

    def getcount (self,sql):
        connect = 'DRIVER={MySQL ODBC 8.0 Unicode Driver}; SERVER=localhost; PORT=3306;DATABASE=readinglog; UID=root; PASSWORD=Cerulean051;'
        db = pyodbc.connect(connect) 
        crsr = db.cursor()
        res = crsr.execute(sql)
        row=crsr.fetchone()
        return row.c


    def submitdata (self):
        connect = 'DRIVER={MySQL ODBC 8.0 Unicode Driver}; SERVER=localhost; PORT=3306;DATABASE=readinglog; UID=root; PASSWORD=Cerulean051;'
        db = pyodbc.connect(connect)
        c=self.getcount("select count(*) as c from student where `first name` = '"+self.txtfname.text()+"' and `last name`= '"+self.txtlname.text ()+"'")
        if c == 0:
            sql = "insert into student (`first name`,`last name`) values ('"+ self.txtfname.text()+"','" +self.txtlname.text()+"')"
            print (sql)
            crsr = db.cursor()
            res = crsr.execute(sql)
        c=self.getcount("select count(*) as c from book where `title` = '"+self.books [0].text()+"'")
        if c == 0:
            sql= "insert into book (`title`) values ('"+self.books [0].text()+"')"
            print (sql)
            crsr = db.cursor()
            res = crsr.execute(sql)

        sql="select idstudent from `student` where `first name` ='"+ self.txtfname.text()+"' and `last name` = '"+ self.txtlname.text()+"' "
        crsr = db.cursor()
        res = crsr.execute(sql)
        row = crsr.fetchone()
        studentid=row.idstudent

        sql= "select idbook from `book` where `title` = '" +self.books [0].text()+ "' "
        crsr = db.cursor()
        res = crsr.execute(sql)
        row = crsr.fetchone()
        bookid=row.idbook
        
        sql= "insert into relationship (`pages`,`idbook`,`minutesread`,`idname`) values ("+self.pages [0].text()+","+str(bookid)+","+self.txts[0].text()+","+str(studentid)+")"
        print (sql)
        crsr = db.cursor()
        res = crsr.execute(sql)
       

        db.commit()
        print (sql)
        self.getminutes ()
        self.getbooks ()
        self.getpages()
        print ('minutes Mon:'+self.Monday+' Tues:  '+ self.Tuesday+' Wed:  '+ self.Wednesday+' Thurs: '+self.Thursday+' Friday: '+self.Friday+' Sat: '+self.Saturday+' Sun: '+self.Sunday) 
        print ('titleMon:'+self.monbooks+' Tues:  '+ self.tuesbooks+' Wed:  '+ self.wedbooks+' Thurs: '+self.thursbooks+' Friday: '+self.fribooks+' Sat: '+self.satbooks+' Sun: '+self.sunbooks)
        print ('pagesMon:'+self.monpages+' Tues:  '+ self.tuespages+' Wed:  '+ self.wedpages+' Thurs: '+self.thurspages+' Friday: '+self.fripages+' Sat: '+self.satpages+' Sun: '+self.sunpages)

        minutesread=[]
        for x in [self.Monday, self.Tuesday, self.Wednesday]:
            if x.isdigit ():
                minutesread.append(int(x))
            else:
                minutesread.append(0)
        pagesread=[]
        for x in [self.monpages, self.tuespages,self.wedpages]:
            if x.isdigit ():
                pagesread.append (int(x))
            else:
                pagesread.append(0)

        booksread =[(self.monbooks),(self.tuesbooks),(self.wedbooks),(self.thursbooks),(self.fribooks),(self.satbooks),(self.sunbooks)]
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


# select `id,` `first name`, `last name`, `grade`
    # from student