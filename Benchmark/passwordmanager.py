import pickle
import os
import random
#password storage
def passacc():
    while True:
        f=open("user.dat",'rb')
        user=input("Enter the Username:")
        s=pickle.load(f)
        if user==s[0]:
            for i in range(3):
                passw=input("Enter the Password:")
                if passw==s[1]:
                    print("Access Granted")
                    f1=open("passwords.dat","rb")
                    e=pickle.load(f1)
                    for i in e:
                        print(i)
                    f1.close()
                    break
                else:
                    print("Access Denied!")
        else:
            print("User not found")
            f.close()
            break
        break
def pass_sav():
    while True:
        f1=open("passwords.dat","rb")
        user=input("Enter User name/ID:")
        site=input("Enter Website:")
        passw=input("Enter Password:")
        #[site,id,pass]
        dum=[]
        while True:
            s=pickle.load(f1)
            dum.append(s)
            for i in dum:    
                if dum[i][0]==site or dum[i][1]==user:
                    dum[i][2]=passw
                    break
                else:
                    dum.append([site,user,passw])
            break
        f2=open("passwords.dat","wb")
        pickle.dump(dum,f2)
        f2.close()
        f1.close()
        break
#pass generation
def pass_gen():
    passg=""
    re="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-=_+/[]\\\{\};;\'\"?.,<>"
    leng=int(input("Password length:"))
    for i in range(leng):
        passg=passg+re[random.randrange(len(re))]
    print(passg)
def otp_strong():
    passg=""
    re="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-=_+/[]\\\{\};;\'\"?.,<>"
    for i in range(random.randrange(15)):
        passg=passg+re[random.randrange(len(re))]
    print("OTP=> ",passg)
def otp_med():
    passg=""
    re="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    for i in range(random.randrange(15)):
        passg=passg+re[random.randrange(len(re))]
    print("OTP=>",passg)
def otp():
    passg=""
    re="1234567890"
    for i in range(6):
        passg=passg+re[random.randrange(len(re))]
    print("OTP=>",passg)
#pass suggestion
p=""
def passcheck():
    p=input("Enter PassWord:")
    #al="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY"
    #num="1234567890"
    sp="`~!@#$%^&*()-=_+/[]\\\{\};;\'\"?.,<>"
    f=0 #strong
    if len(p)>=8:
        if p.isalpha():
            if p.isnumeric():
                for i in sp:
                    if i not in p:
                        f=1 #medium
            else:
                for i in sp:
                    if i not in p:
                        f=2#poor
        else:
            if p.isnumeric():
                for i in sp:
                    if i not in p:
                        f=2
            else:
                for i in sp:
                    if i not in p:
                        f=3#very poor
    else:
        print("Password not long enough")
        passcheck()
    if f==0:
        print("PassWord Strength is Strong:",p)
    elif f==1:
        print("PassWord Strength is Medium:",p)
    elif f==2:
        print("PassWord Strength is Poor:",p)
    else:
        print("PassWord Strength is Very Poor:",p)
#password apply