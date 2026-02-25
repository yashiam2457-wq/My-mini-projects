import mysql.connector as my
mys=my.connect(host='localhost',user='root',passwd='1234')
myc=mys.cursor()
print('mysql-command>')
myc.execute('use student;')
myc.execute('select *from class12;')
#s=int(input('starting of record:'))
#for i in range(4):
w=myc.fetchall()
for i in w:
    print('success')
    print(i)
#r=int(input('no of records:'))
#for k in range(r):
#   for m in myc:
#       print(j)
mys.close()
