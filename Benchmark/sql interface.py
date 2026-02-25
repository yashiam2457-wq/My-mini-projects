import mysql.connector as my
mys=my.connect(host='localhost',user='root',passwd='1234')
myc=mys.cursor()
while True:
    w=input('mysql-command>')
    myc.execute(w)
    print('Command executed Successfully')
    for i in w:
        if i[0].lower()=='select' or 'show':
            for j in myc:
                print(j)
        else:
            mys.commit()
mys.close()
