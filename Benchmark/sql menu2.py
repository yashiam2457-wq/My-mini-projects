import mysql.connector as my
mys=my.connect(host='localhost',user='root',passwd='1234')
myc=mys.cursor()
while True:
    c=[]
    r=v=ac=''
    print('MySql Successfuly Connected')
    print('DATABASES')
    myc.execute('show databases;')
    myr=myc.fetchall()
    for i in myr:
        print(i)
    a=input('Choose your database(if not exist type \'no\'):')
    if a.lower()=='no':
        x=input('Enter name of database to Create:')
        myc.execute('create database '+x+';')
        mys.commit()
    if a.lower()=='exit':
        break
    myc.execute('use '+a+';')
    print('TABLES')
    myc.execute('show tables;')
    for j in myc:
        print(j)
    de=input('Do you want to delete database or table from your Directory(or exit):')
    if de.lower()=='database':
        ded=input('Database you want to delete:')
        myc.execute('delete database '+ded+';')
        mys.commit()
    if de.lower()=='table':
        det=input('Table you want to delete:')
        myc.execute('delete table '+det+';')
        mys.commit()
    if de.lower()=='exit':
        break
    b=input('Choose your table(if not exist type \'no\'):')
    if b.lower()=='no':
        b=input('Enter name of table to Create:')
        z=input('Columns in table with attribute:')
        myc.execute('create table '+b+'('+z+');')
        mys.commit()
    if b.lower()=='exit':
        break
    print('Menu')
    print('A-Add record to the table')
    print('B-Remove record from the table')
    print('C-Check record from the table')
    d=input('Choose your choice(A,B,C,exit):')
    if d.lower()=='a':
        m=int(input('How many records are to be Added:'))
        myc.execute('desc '+b+';')
        for n in range(m):
            for k in myc:
                if k[1][:7]=='varchar'or k[:4]=='char':
                    f=input(k[0]+':')
                    c.append(f)
                else:
                    f=int(input(k[0]+':'))
                    c.append(f)
            c=tuple(c)
            q='insert into '+b+' values'+str(c)+';'
            print(q)
            myc.execute(q)
            mys.commit()
            print('Record Added Successfully')
    if d.lower()=='b':
        myc.execute('desc '+b+';')
        for k in myc:
            print(k)
            if k[3]=='PRI':
                g=input('Enter the '+k[0]+':')
                break
            elif k[1][:3]=='int':
                g=input('Enter the '+k[0]+':')
                break
        x='delete from '+b+' where '+k[0]+'='+g+';'
        print(x)
#        myc.execute(x)
#        mys.commit()
    if d.lower()=='c':
        print('1-Get all records')
        print('2-Get records as your condition')
        print('3-Get all sections')
        o=int(input('Choose your choice(1,2,3,exit):'))
        if o==1:
            myc.execute('select * from '+b+';')
            for l in myc:
                print(l)
        if o==2:
            p=int(input('Enter no of conditions:'))
            for q in range(p):
                s=input('Enter the condition:')
                r=r+' '+s
            myc.execute('select * from '+b+' where '+r+';')
            for l in myc:
                print(l)
        if o==3:
            myc.execute('desc '+b+';')
            print('Sections')
            for l in myc:
                print(l)
            t=int(input('Enter no of sections you want to get:'))
            ag=input('Distinct by:')
            for u in range(t):
                w=input('Section:')
                v=v+' '+w
            myc.execute('select'+v+' from '+b+' group by '+ag+';')
            for af in myc:
                print(af)
    if d.lower()=='exit':
        break
    ae=input('Do you want to continue(y/n):')
    if ae=='n':
        break
mys.close()
