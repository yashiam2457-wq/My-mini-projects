import mysql.connector as my
mys=my.connect(host='localhost',user='root',passwd='1234')
myc=mys.cursor()
while True:
    c=[]
    print('MySql Successfuly Connected')
    print('DATABASES')
    myc.execute('show databases;')
    myr=myc.fetchall()
    for i in myr:
        print(i)
    a=input('Choose your database:')
    if a.lower()=='exit':
        break
    myc.execute('use '+a+';')
    print('TABLES')
    myc.execute('show tables;')
    for j in myc:
        print(j)
    b=input('Choose your table:')
    if b.lower()=='exit':
        break
    print('Menu')
    print('A-Add a record to your table')
    print('B-Remove a record from your table')
    print('C-Check your record from your table')
    d=input('Choose your choice(A,B,C):')
    if d.lower()=='a':
        myc.execute('desc '+b+';')
        for k in myc:
            if k[1][:7]=='varchar'or k[:4]=='char':
                f=input(k[0]+':')
                c.append(f)
            else:
                f=int(input(k[0]+':'))
                c.append(f)
        myc.execute('insert into '+b+' values(',c,';')
    if d.lower()=='b':
        myc.execute('desc '+b+';')
        for k in myc:
            if k[3]=='PRI':
                g=int(input('Enter the',k[0],':'))
        myc.execute('delete from '+b+' where '+k[0]+'=='+g+';')
        myc.commit()
    if d.lower()=='c':
        myc.execute('select * from '+b+';')
        for l in myc:
            print(l)
    if d.lower()=='exit':
        break
mys.close()
