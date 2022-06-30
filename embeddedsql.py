import pyodbc

connect = 'DRIVER={MySQL ODBC 8.0 Unicode Driver}; SERVER=localhost; PORT=3306;DATABASE=northwind; UID=root; PASSWORD=Cerulean051;'
db = pyodbc.connect(connect)
lname = input('give me a last name to search for: ')
sql = "select * from employees where `last name`='"+lname+"'"
crsr = db.cursor()
res = crsr.execute(sql)
for row in res:
    print(row.__getattribute__('First Name') + ' ' + row.__getattribute__('Last Name'))

crsr.close()

cat= input ("give me a category")
cat = cat.strip()
sql= "select `product name`,`category`, `discontinued` from products where `category` = '"+cat +"'"
crsr = db.cursor()
res = crsr.execute(sql)
for row in res:
    print(row.__getattribute__('product name') + ' ' + row.__getattribute__('category') + " "+ row.__getattribute__ ('discontinued'))


sql = "select *from customers where `Job Title` = '?'"
crsr = db.cursor()
res = crsr.execute(sql,)
for row in res:
    print(row.__getattribute__('Job Title'))

crsr.close()
db.close()