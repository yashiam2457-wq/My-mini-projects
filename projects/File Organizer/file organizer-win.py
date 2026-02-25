import os
import shutil
import time
import urllib,re
import urllib.request
files={
    "Docs":[".doc",".docx",".odt",".txt",".pages",".rtf",".wpd",".wps",".pdf",".ppt"],
    "Sheets":[".csv",".numbers",".ods",".xls",".xlsx"],
    "Web":[".asp",".aspx"".css",".htm",".html",".jps",".php",".xml"],
    "Image":[".png",".jpg",".ico",".gif",".bmp",".jpeg",".raw",".tif",".tiff"],
    "Media":[".aif",".mov",".mp3",".mp4",".mpg",".wav",".wma",".wmv",".m4a"],
    "Prorams":[".c",".cpp",".cs",".js",".java",".json",".py",".sql",".swift",".vb"],
    "Compressed":[".zip",".rar",".7z"],
    "Executable":[".exe",".apk",".msi",".bin",".bat"]}
def downloadinfo(url):
    #f=urllib.request.urlopen(url)
    #meta=f.info()
    #print("File size:",f.length)
    print("File info:",urllib.request.urlopen(url).info().get("Content-Length"))
    #print(byte_converter(int(meta.get("Content-Length"))))
    x=input("Continue[y/n]:")
    if x.lower()=="y":
        try:
            os.system("wget -y"+url)
            #for windows
            #os.system(f"curl -O {url}")
            print("File is downloaded")
        except FileNotFoundError:
            print("File not found")
        except PermissionError:
            print("Link permission denied")
def byte_converter(byte):
    if byte<1024:
        return str(byte)+" Bytes"
    elif byte>1024 and byte<(1024**2):
        return str(round(byte/1024,4))+" KB"
    elif byte>(1024**2) and byte<(1024**3):
        return str(round(byte/(1024**2),4))+" MB"
    elif byte>(1024*3) and byte<(1024**4):
        return str(round(byte/(1024**3),4))+" GB"
    elif byte>(1024**4) and byte<(1024**5):
        return str(round(byte/(1024**4),4))+" TB"
    elif byte>(1024*5) and byte<(1024**6):
        return str(round(byte/(1024**5),4))+" PB"
    elif byte>(1024**6) and byte<(1024**7):
        return str(round(byte/(1024**6),4))+" EB"
    elif byte>(1024*7) and byte<(1024**8):
        return str(round(byte/(1024**7),4))+" ZB"
    elif byte>(1024**8) and byte<(1024**9):
        return str(round(byte/(1024**8)),4)+" YB"
    else:
        return str(round(byte),4)+" Size is to Big"
#For Windows
def search(file,dir):
    os.chdir(dir)
    dirfile=os.listdir(dir)
    f=0
    for i in dirfile:
        if os.path.isdir(os.path.join(dir,i)):
            f,loc=search(file,os.path.join(dir,i))
        elif os.path.isfile(os.path.join(dir,i)):
            if file==i:
                f=1
                loc=os.path.join(dir.i)
                break
    if f==0:
        print("File not found")
    else:
        print("File Found at:",loc)

def rename(file1,dir):
    t=input("Enter the new name:")
    if t=="":
        i=0         
        while True:
            try:
                i=i+1
                fname=file1.split(".")
                if len(fname)!=1:            
                    file2=fname[0]+"({i})."+fname[1]
                    os.chdir(dir)
                    os.rename(file1,file2)
                    break
                else:
                    file2=fname[0]+"({i})"
                    os.chdir(file1)
                    os.rename(file1,file2)
                    break
            except FileExistsError:
                    continue
    else:
        while True:
            try:
                fname=file1.split(".")
                if len(fname)!=1:            
                    file2=t+"."+fname[1]
                    os.chdir(dir)
                    os.rename(file1,file2)
                    break
                else:
                    os.chdir(file1)
                    os.rename(file1,t)
                    break
            except FileExistsError:
                rename(file1,dir)

def delete(file1,dir):##
    try:
        os.chdir(dir)
        if os.path.isfile(file1):
            os.remove(file1)
        elif os.path.isdir(file1):
            if os.listdir(file1)==0:
                os.removedirs(file1)
    except FileNotFoundError:
        if os.path.isfile(file1):
            print("File not found")
        else:
            print("Directory not found")

def move(file1,from1,to):##
    x=os.listdir(from1)
    y=os.listdir(to)
    if file1 not in y and file1 in x:
        os.chdir(to)
        z1=from1+"\\"+file1
        z2=to+"\\"+file1
        os.system("move "+z1)
    elif file1 not in x:
            print("FIle/directory not found")
    elif file1 in y:
            while True:
                print("File/directory exists:\n1-Compare the files/Directory and choose\n2-Rename this file/directory\n3-move file/directory anyway\n4-Cancel {a}")
                w=input("Choose:")
                if w=="1":
                    if os.path.isfile(file1):
                        print("Info of existing file:\n")
                        print("Name:",os.path.basename(z1))
                        print("Size:",byte_converter(os.path.getsize(z1)))
                        print("Created on:",time.ctime(os.path.getctime(z1)))
                        print("Modified on:",time.ctime(os.path.getmtime(z1)))
                        print("Last access on:",time.ctime(os.path.getatime(z1)))
                        print("Info of moving file:\n")
                        print("Size:",byte_converter(os.path.getsize(z2)))
                        print("Created on:",time.ctime(os.path.getctime(z2)))
                        print("Modified on:",time.ctime(os.path.getmtime(z2)))
                        print("Last access on:",time.ctime(os.path.getatime(z2)))
                    else:
                        print("Info of existing directory:\n")
                        print("No of folders:{}\nNo of files:{}".format(cont(z1)))     
                        print("Size:",byte_converter(os.path.getsize(z1)))
                        print("Created on:",time.ctime(os.path.getctime(z1)))
                        print("Modified on:",time.ctime(os.path.getmtime(z1)))
                        print("Last access on:",time.ctime(os.path.getatime(z1)))
                        print("Info of moving directory:\n")
                        print("No of folders:{}\nNo of files:{}".format(cont(z2)))
                        print("Size:",byte_converter(os.path.getsize(z2)))
                        print("Created on:",time.ctime(os.path.getctime(z2)))
                        print("Modified on:",time.ctime(os.path.getmtime(z2)))
                        print("Last access on:",time.ctime(os.path.getatime(z2)))
                        while True:
                            r=int(input("Choose what to do:\n1-Rename file\n2-move anyway\n3-Cancel"))
                            if r==1:
                                rename(file1,y)
                                break
                            elif r==2:
                                delete(file1,to)
                                copy(file1,from1,to)
                                delete(file1,from1)
                                break
                            elif r==3:
                                print("File move cancel")
                                break
                            else:
                                continue
                elif w==2:
                    rename(file1,y)
                    break
                elif w==3:
                    delete(file1,to)
                    copy(file1,from1,to)
                    break
                elif w==4:
                    print("File copy cancel")
                    break
                else:
                    continue    
def copy(file1,from1,to):##
    x=os.listdir(from1)
    y=os.listdir(to)
    if file1 not in y and file1 in x:
        os.chdir(to)
        z1=from1+"\\"+file1
        z2=to+"\\"+file1
        os.system("copy "+z1)
    elif file1 not in x:
            print("FIle/directory not found")
    elif file1 in y:
            while True:
                print("File/directory exists:\n1-Compare the files/Directory and choose\n2-Rename this file/directory\n3-copy file/directory anyway\n4-Cancel {a}")
                w=input("Choose:")
                if w=="1":
                    if os.path.isfile(file1):
                        print("Info of existing file:\n")
                        print("Size:",byte_converter(os.path.getsize(z1)))
                        print("Created on:",time.ctime(os.path.getctime(z1)))
                        print("Modified on:",time.ctime(os.path.getmtime(z1)))
                        print("Last access on:",time.ctime(os.path.getatime(z1)))
                        print("Info of moving file:\n")
                        print("Size:",byte_converter(os.path.getsize(z2)))
                        print("Created on:",time.ctime(os.path.getctime(z2)))
                        print("Modified on:",time.ctime(os.path.getmtime(z2)))
                        print("Last access on:",time.ctime(os.path.getatime(z2)))
                    else:
                        print("Info of existing directory:\n")
                        print("No of folders:{}\nNo of files:{}".format(cont(z1)))     
                        print("Size:",byte_converter(os.path.getsize(z1)))
                        print("Created on:",time.ctime(os.path.getctime(z1)))
                        print("Modified on:",time.ctime(os.path.getmtime(z1)))
                        print("Last access on:",time.ctime(os.path.getatime(z1)))
                        print("Info of copying directory:\n")
                        print("No of folders:{}\nNo of files:{}".format(cont(z2)))
                        print("Size:",byte_converter(os.path.getsize(z2)))
                        print("Created on:",time.ctime(os.path.getctime(z2)))
                        print("Modified on:",time.ctime(os.path.getmtime(z2)))
                        print("Last access on:",time.ctime(os.path.getatime(z2)))
                        while True:
                            r=int(input("Choose what to do:\n1-Rename file\n2-copy anyway\n3-Cancel"))
                            if r==1:
                                rename(file1,y)
                                break
                            elif r==2:
                                delete(file1,to)
                                copy(file1,from1,to)
                                break
                            elif r==3:
                                print("File copy cancel")
                                break
                            else:
                                continue
                elif w==2:
                    rename(file1,y)
                    break
                elif w==3:
                    delete(file1,to)
                    copy(file1,from1,to)
                    break
                elif w==4:
                    print("File copy cancel")
                    break
                else:
                    continue

def cont(dir,d=0,f=0):
    os.chdir(dir)
    t=os.listdir(dir)
    for i in t:
        if os.path.isdir(os.path.join(dir,i)):
            f,d=cont(dir+"\\"+i,d,f)
            d=d+1
        else:
            f=f+1
    return f,d

def cont_ext(dir,d=0,ext={}):
    os.chdir(dir)
    t=os.listdir(dir)
    for i in t:
        if os.path.isdir(os.path.join(dir,i)):
            d,ext=cont(dir+"\\"+i,d,ext)
            d=d+1
        else:
            e=i.split(".")[-1]
            if e in ext.keys():
                ext.update({e:ext.get(e)+1})
            else:
                ext.update({e:1})
    return d,ext
def organize(dir):
    os.chdir(dir)
    file=os.listdir(dir)
    for i in file:
        for j in files:
            if os.path.splitext(i)[1] in files.get(j):
                if not os.path.exists(j[0]):
                    os.mkdir(dir+j[0])
                    move(i,dir,dir+j[0])
                else:
                    move(i,dir,dir+j[0])
            else:
                if not os.path.exists("Folder"):
                    os.mkdir(dir+"\\Folder")
                    move(i,dir,dir+"\\Folder")
                else:
                    move(i,dir,dir+"\\Folder")
    print("FIles Organized")
#organize("C:\\Users\\test\\Downloads\\Quiz-Game-with-Shuffled-Answers-PPTVBA")