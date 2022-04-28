

from tkinter.messagebox import QUESTION


class Student:
    def __init__(self,name ='',ID=-1, birthdate ='1/1/2000'):
        self.name =name
        self.ID= ID
        self.birthdate = birthdate

    def study (self):
        print (self.name + 'is studying')

    def do_homework (self,course):
        print(self.name +' is doing homework for their' +course+ 'course.')

    def ask_question (self):
        print ('Wait, what?')

    def eat(self):
        print ('Mmmm, dinner')

    def sleep (self):
        print ('snore')

class Teacher:
    def __init__ (self,name ='', ID=-1, birthdate ='1/1/2000'):
        self.name =name
        self.ID =ID
        self.birthdate= birthdate

    def sleep (self):
        print ('snore')





class person:
    def __init__(self,name= '',ID=-1, birthdate='1/1/2000'):
        self.name =name
        self.ID = ID
        self.birthdate = birthdate
    def eat(self):
        print ('Mmmm, dinner')

    def sleep (self):
        print ('snore')

class Student (person):
    def __init__ (self, name= '',ID=-1,birthdate ='1/1/2000',grade= ''):
        person.__init__(self,name,ID,birthdate)
        self.grade=grade
    def study(self):
        print (self.name + 'is studying')
    def study(self):
        print (self.name + 'is studying')
    def do_homework(self,course):
        print(self.name + 'is doing homework for their' + course+ 'course. ')
    def ask_question (self):
        print ('Wait, what?')
    def grade (Self):
        print (Self.name + 'is grade')

class Teacher(person):
    def __init__(self, name='', ID=-1, birthdate='1/1/2000'):
        person.__init__(self,name, ID, birthdate)
    
    def teach(self):
        print (self.name +'is teaching')
    
    def assign_homework (self, course):
        print (self.name + 'assigned homework for their' + course +' course name.')

    def answer_question (self):
        print ('Let me see if I can help')

stud= Student ('George', 100, '2/1/1860','K')
stud.sleep ()
stud.study ()
teach= Teacher ('Martha',101, '9/1/1975')
teach.sleep ()
c = 'CS100B'
teach.assign_homework(c)
per=person ('bill')
per.sleep ()
print(stud.grade)

stud.ask_question()
teach.assign_homework(c)

t= Teacher ('smith')
s= Student ('Jones')

s.sleep()
t.eat ()