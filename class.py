class Books:
    def __init__(self,title ='',pages=''):
        self.title=title
        self.pages=pages

    def name (self):
        print (self.title)

    def pagecount (self):
        print (self.pages)

Name= input ("What is the name of the book? ")
Pages= input ('How many pages is this book? ')

b= Books(Name, Pages)

b.name()
b.pagecount()
