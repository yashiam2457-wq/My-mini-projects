import csv
print('------------HOSTEL MANAGEMENT-----------')
print('----------------Project-----------------')
print('Made By : Yash Gupta')
while True:
    print('MAIN MENU')
    print('1-ADDMISSION FORM')
    print('2-VIEW HOSTEL RECORDS')
    print('3-UPDATE HOSTEL RECORDS')
    print('4-EXIT')
    x=int(input('Choose your option(1-4):'))
    if x==1:
        o=open('hostel.csv','r')
        h=input('ENTER YOUR ROLL NO.:')
        n=input('ENTER YOUR NAME:')
        r=input('ENTER YOUR ROOM NUMBER:')
        p=input('ENTER YOUR FEES PAID:')
        b=input('ENTER YOUR BALANCE:')
        x=[h,n,r,p,b]
        p=csv.reader(o)
        m=list(p)
        o.close()
        o=open('hostel.csv','a')
        w=csv.writer(o)
        m=[]
        m.append(x)
        w.writerows(m)
        o.close()
        print('RECORD SUCCESSFLLY ADDED')
    elif x==2:
        o=open('hostel.csv')
        p=csv.reader(o)
        m=list(p)
        h=input('ENTER YOUR ROLL NO.:')
        try:
            for i in m:
                if i[0]==h:
                    w=i
                    break
                else:
                    w='RECORD NOT FOUND'
        except Exception:
            print(w)
            o.close()
    elif x==3:
        o=open('hostel.csv')
        p=csv.reader(o)
        m=list(p)
        h=input('ENTER YOUR ROLL NO.:')
        o.close()
        for i in m:
            if i[0]==h:
                s=m.index(i)
                while True:
                    o=open('hostel.csv','w')
                    print("What you want to modify?")
                    print("1-Name")
                    print("2-Room No.")
                    print("3-Fees Paid")
                    print("4-Balance")
                    print('5-Exit')
                    c=int(input('ENTER YOUR CHOICE:'))
                    if c==1:
                        n=input("ENTER NEW NAME:")
                        o.seek(s)
                        x=[i[0],n,i[2],i[3],i[4]]
                        m.insert(s,x)
                        w=csv.writer(o)
                        w.writerows(m)
                        o.close()
                        print('RECORD SUCCESSFULLY UPDATED')
                        break
                    elif c==2:
                        r=input('ENTER NEW ROOM NUMBER:')
                        o.seek(s)
                        x=[i[0],i[1],r,i[3],i[4]]
                        m.insert(s,x)
                        w=csv.writer(o)
                        w.writerows(m)
                        o.close()
                        print('RECORD SUCCESSFULLY UPDATED')
                        break
                    elif c==3:
                        p=input('ENTER NEW FEES PAID:')
                        o.seek(s)
                        x=[i[0],i[1],i[2],p,i[4]]
                        m.insert(s,x)
                        w=csv.writer(o)
                        w.writerows(m)
                        o.close()
                        print('RECORD SUCCESSFULLY UPDATED')
                        break
                    elif c==4:
                        b=input('ENTER NEW BALANCE:')
                        o.seek(s)
                        x=[i[0],i[1],i[2],i[3],b]
                        m.insert(s,x)
                        w=csv.writer(o)
                        w.writerows(m)
                        o.close()
                        print('RECORD SUCCESSFULLY UPDATED')
                        break
                    elif c<=5:
                        o.close()
                        break
                    break
            elif i[0]!=h:
                print('RECORD NOT FOUND')
                break
    elif x<=4:
        break
        
        
        
        
