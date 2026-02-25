import mysql.connector as my
mys=my.connect(host='localhost',user='root',passwd='1234')
myc=mys.cursor()
myc.execute('use test;')
a=int(input('No of record to be insurted:'))
for i in range(a):
    b=int(input('ComID:'))
    c=input('Name:')
    d=input('Gender:')
    myc.execute('insert into employee values(b,c,d);')
    myc.commit()
mys.close()
