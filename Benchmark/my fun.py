import platform,os,pyscreenshot,math,random,pickle,csv,time
from pynput.keyboard import Key,Listener
from PIL import Image
import datetime
import functools
import numpy as np
import cv2
import pyzbar.pyzbar
import qrcode.constants
import sounddevice
from scipy.io.wavfile import write
import wavio
import pyautogui
import qrcode
import psutil
import pyzbar
app={
    "fire fox":"firefox -u"
}
def dist(x):
    m=x*0.621371
    print(x,'km=',m,'miles')
def num(x):
    print(x,'in decimal')
    print(bin(x),'in binary')
    print(oct(x),'in octadecimal')
    print(hex(x),'in hexadecimal')
def leap(w):
    if w%4 ==0:
        if w%100 ==0:
            if w%400 !=0:
                return 366
            else:
                return 365
def datetime():
    x= int(input('year:'))
    y= int(input('month:'))
    z= int(input('day:'))
    a= int(input('hour:'))
    b= int(input('minute:'))
    c= int(input('seconds:'))
    d=(x*12)+y
    print('in months:',d)
    e=(d*365.25)+z
    print('in days:',int(e))
    f=(int(e)*24)+a
    print("in hours:",f)
    g=(f*60)+b
    print("in minutes:",g)
    h=(g*60)+c
    print("in seconds:",h)
def fac(x):
    w=1
    for i in range(1,x+1):
        w=w*i
    print('Factorial of',x,'is',w)
def comp(p,r=5,t=1):
    c=r*t*p/100
    print('Compound Interest-',c)
def prime(x):
    for i in range(2,x):
        if (x%i)==0:
            print(x,'is not a Prime No.')
            break
    else:
        print(x,'is a Prime No.')
def prime2(x):
    print('Prime No.',end='-')
    for i in range(2,x+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end='')
def pal(x):
    e=x
    r=0
    while e>0:
        d=x%10
        r=r*10+d
        e=e//10
    if x==e:
        print('Palindrome')
    else:
        print('Not a Palindrome')    
def timer1(t):
    while t:
        m,s=divmod(t,60)
        h,m=divmod(m,60)
        print("{:03d}:{:02d}:{:02d}".format(h,m,s),end="\r")
        time.sleep(1)
        t=t-1
timer1(3600)
def openapp(a):
    try:
        if platform.system()=="Windows":
            p="Start "+a
        elif platform.system()=="Linux":
            p=app[a.lower()]
        os.system(p)
    except Exception as e:
        print(e)
        print('Application Not Found')
def timer2():
    t=datetime.date()
    print("year-month-day hour:minute:seconds")
    w=str(input('Enter Date and Time:'))
    w=datetime.date(w)
    z=w-t
    if z<=0:
        print('Sorry sir but you have already passed that day with ',str(-z))
    else:
        print('Time Remaining till that time comes is ',str(z))
k=[]
def keypress(key):
    k.append(key)
    writef(k)
def writef(k):
    f=open("keylogs.txt","w")
    for key in k:
        #if key==Key.enter:
        #    key="\n"
        r=str(key).replace("'","")
        f.write(r)
        #f.write(" ")
def rel(key):
    if key==Key.esc:
        return False
    elif key==Key.enter:
        return True
def keylog():
    k=[]
    with Listener(on_press=keypress,on_release=rel) as listener:
        listener.join()
def binfilecheck():
    f=input("Enter file:")
    s=open(f,'rb')
    try:
        while True:
            print(pickle.load(s))
    except EOFError:
        s.close()
def shot():
    time.sleep(5)
    image=pyscreenshot.grab()
    image.show()
    image.save("screenshot1.png")
@functools.cache
def record(freq = 44100,duration = 5):
    recording = sounddevice.rec(int(duration * freq), samplerate=freq, channels=2)
    sounddevice.wait()
    write("recording0.wav", freq, recording)
    wavio.write("recording1.wav", recording, freq, sampwidth=2)
def record_screen(t):
    screen_size = (1929,1080)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, screen_size)
    fps=120
    p=0
    while True:
        ti=time.time()
        img = pyautogui.screenshot()
        if ti>1/fps:
            p=time.time()
            frame=np.array(img)
            frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
        cv2.waitKey(1)    
        cv2.imshow('Screen Recording', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    out.release()
    cv2.destroyAllWindows()
def qrgen(link,name):
    qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=20,border=1)
    qr.add_data(link)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black",back_color="white")
    img.save(name)
    print("Complete")
    Image.open(name).show()
def qrread(file=""):
    if file=="":
        time.sleep(5)
        sr=pyautogui.screenshot()
    else:
        sr=cv2.imread(file)
        conqr=cv2.cvtColor(np.array(sr),cv2.COLOR_RGB2BGR)
        decoded=pyzbar.pyzbar.decode(conqr)
        for i in decoded:
            d=i.data.decode("utf-8")
            print(d)
#qrgen("https://www.youtube.com/watch?v=7kL7q4hfhLw","test.png")
def click():
    x,y=0,time.time()
    while (time.time()<=y+5):
        pyautogui.click()
        x=x+1
    print(x)
#depth feed
y=[]
def tcheck(l,i=[]):
    for a,b in enumerate(l):
        n=i+[a]
        if isinstance(b,list):
            tcheck(b,n)
        else:
            y.append(str(b)+"".join(f"[{k}]" for k in n))    
    return y        