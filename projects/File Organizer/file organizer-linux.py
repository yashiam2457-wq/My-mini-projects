import urllib.parse
import pytube.exceptions
import os,time,urllib,urllib.request,requests
import pytube,zipfile
import bs4
import webbrowser
import json,tqdm
import subprocess
from googleapiclient.discovery import build
import sandboxie
from bs4 import BeautifulSoup
files={
    "Docs":[".doc",".docx",".odt",".txt",".pages",".rtf",".wpd",".wps",".pdf",".ppt"],
    "Sheets":[".csv",".numbers",".ods",".xls",".xlsx"],
    "Web":[".asp",".aspx",".css",".htm",".html",".jps",".php",".xml"],
    "Image":[".png",".jpg",".ico",".gif",".bmp",".jpeg",".raw",".tif",".tiff"],
    "Media":[".aif",".mov",".mp3",".mp4",".mpg",".wav",".wma",".wmv"],
    "Prorams":[".c",".cpp",".cs",".js",".java",".json",".py",".sql",".swift",".vb"],
    "Compressed":[".zip",".rar",".7z"],
    "Executable":[".exe",".apk",".msi",".bin",".bat",".deb",".whl"]}
ext1=[".doc",".docx",".txt",".pages",".pdf",".ppt",".csv",".xls",".xlsx",
      ".css",".htm",".html",".php",".xml",".png",".jpg",".ico",".gif",".bmp",".jpeg",".raw"
      ".mov",".mp3",".mp4",".wav",".c",".cpp",".cs",".js",".java",".json",".py",".sql",".swift",".vb"
      ,".zip",".rar",".7z",".exe",".apk",".msi",".bin",".bat",".deb",".whl"]
urldl=(
    "https://www.google.com","https://www.youtube.com","https://www.twitter.com",
    "https://www.reddit.com","https://www.github.com","https://www.stackoverflow.com",
    "https://www.stackexchange.com","https://www.mega.nz","https://www.mediafire.com",
    "https://www.archive.org","https://www.sourceforge.net","https://www.curseforge.com",
    "https://mail.google.com","https://drive.google.com","https://www.dropbox.com",
    "https://www.web.whatsapp.com"
)
urllogin={
    "https://www.google.com","https://www.youtube.com","https://www.reddit.com","https://www.github.com",
    "https://www.mega.nz","https://mail.google.com","https://drive.google.com","https://www.dropbox.com",
    "https://www.web.whatsapp.com","https://www.chess.com","https://www.coursera.com","https://www.pokemonshowdown.com",
    "https://www.stream.com"
}
def downloadinfo(url):
    req=urllib.request.Request(url)
    res=urllib.request.urlopen(req)
    print(f"Name:{res.info().get("Content-Name")}")
    print(f"Type:{res.info().get("Content-Type")}")
    print(f"Size:{byte_converter(res.info().get("Content-Length"))}")
    return res.info().get("Content-Length")
def videoinfo(url):
    r=requests.get(url)
    s=BeautifulSoup(r.text,"html.parser")
    print(f"Title:{s.find("span",class_="watch-title").text.replace("\n","")}")
    print(f"Views:{s.find("div",class_="watch-view-count").text}")
    print(f"Like:{s.find("span",class_="like-button-renderer").span.button.text}")
    #print(f"Channel:{s.find("span",class_="watch-title").text.replace("\n","")}")
def maldownloadcheckl(url):
    headers = {"x-apikey": "912209ff3a9a93cfd9ca2c3593ed615416b50648e456fef70adb0af28d86636d"}
    if not url.startswith("/"):
        url = "https://www.virustotal.com/api/v3/urls"
        params = {"url": url}
        res=requests.post(url, headers=headers, params=params)
        resjson = json.loads(res.text)
        return resjson
def maldownloadcheckf(url):
    result = subprocess.run(["clamscan", url], capture_output=True, text=True)
    output = result.stdout.strip()
    if "Infected" in output:
        print("file can contain malware")
    else:
        print("file is clear")
def downloadlinkredir(url):
    res=requests.get(url)
    soup=bs4(res.content,"html.parse")
    links=soup.find_all("a",href=True)
    dl=[]
    for i in links:
        href=i["href"]
        for j in ext1:
            if href.endswith(j):
                dl.append(href)
            else:
                deep=downloadlinkredir(href)
                dl.extend(deep)
    print("All desired links:")
    for k in range(1,len(dl)):
        print(k,dl[k-1])
    return dl
def conndownloadcheck(url):
    if urllib.request.urlopen(url).info().get("Content-length")>20971520:#20mb
        try:
            res=requests.get(url,timeout=10)
            res.raise_for_status()
            try:
                r=subprocess.run(["speedtest-cli","--simple"],capture_output=True, text=True)
                speed=float(r.stdout.split("\n")[1].split(" ")[0])
                if speed>5:
                    print("Stable connection")
            except subprocess.CalledProcessError as e:
                print(e)
                print("Speed is slow")
        except requests.exceptions.RequestException as e:
            print(e)
            print("Poor connection")    
vid=[".avi",".mp4",".mkv",".mov"]
aud=[".wav",".mp3",".aac"]
api_key="AIzaSyA41e3gMDkNEjqhqSOpObsg490aQiIG-z4"#youtube api key
def mp4convert(file,ext):
    pass
'''def youtubedownload(url="",dir="/home/yash/Desktop"):
    while True:
        va=input("Enter Download Music or Video[aud/vid]:").lower()
        if url.startswith("https://www.youtube.com/") or url.startswith("https://www.youtube.com/watch?v="):
            yt=pytube.YouTube(url)
            if va=="vid":
                print("Video Resolutions:")
                for t in yt.streams.filter(progressive=True):
                    print(t.resolution(),end="||")
                r=input("Enter resolution:")
                print(vid,sep="||")
                fo=input("Enter format for video:")
                try:
                    if r:
                        yd=yt.streams.filter(progressive=True,resolution=r).first()
                    else:
                        yd=yt.streams.filter(progressive=True).order_by("resolution").desc().first()
                    print("Size",yd._filesize())
                    c=input("Continue Download[y/n]:")
                    if c.lower()=="y":
                        yd.download(dir)
                        break
                except (pytube.exceptions.RegexMatchError, AttributeError) as e:
                    print(f"Error getting resolution: {e}")
                    continue  # Retry download loop
                except pytube.exceptions.PytubeError as e:
                    print(f"Rate limit exceeded: {e}")
                    break
            elif va=="aud":
                print("Audio formats:")
                print(aud,sep="||")
                fo=input("Enter format for audio:")
                yd=yt.streams.filter(progressive=True).get_lowest_resolution()
                print("Size",yd._filesize())
                c=input("Continue Download[y/n]:")
                if c.lower()=="y":
                    yd.download(dir)
                    break
            else:
                print("Invalid!!!")
                break
        else:
            req=pytube.Search().list(part="snippet",query=url,maxResults=15)
            res=req.execute()
        for i in range(len(res["items"])):
            print(f"{i+1}=>\nTitle: {i['snippet']['title']}")
            print(f"Channel:{i['snippet']["channelTitle"]}")
            print(f"Video ID: {i['id']['videoId']}")
        try:
            x=input("Video no:")
            url1=f"https://www.youtube.com/watch?v={res["items"][i-1]['id']['videoId']}"
            youtubedownload(url1,dir)
            break
        except (ValueError,IndexError):
            print("Invalid video no:try again")
            continue
'''
def filedownload(url="", dir="/home/yash/Desktop"):
    while True:
        res=requests.head(url)
        if res.status_code==200:
            ct=res.headers.get("Content-Type")
            cdi=res.headers.get("Content-Disposition")
            par=urllib.parse.urlparse(url)
            if ct and ct.startswith("application/") or cdi and "filename=" or "file=" in cdi:
                for i in ext1:
                    if url.endswith(i):
                        file=urllib.parse.urlparse(url).path.split('/')[-1]
                        res1=requests.get(url,stream=True)
                        with open(file,"wb") as f:
                            try:
                                for chunk in res1.iter_content(chunk_size=8192):
                                    if not chunk:
                                        break
                                    f.write(chunk)
                                print("File downloaded Successfully")
                                executiontest(dir+"/"+file)
                                break
                            except (requests.exceptions.RequestException,IOError) as e:
                                print(e)
                    else:
                        print(f"File extention is .{urllib.parse.urlparse(url).path.split(".")[-1]}\nFile Cannot be downloaded")
                        break
                    break
            elif par.path.endswith("/") and (ct and ct.startswith("text/")):
                folder=urllib.parse.urlparse(url).path.split('/')[-1]
                zipname=f"{folder}.zip"
                try:
                    with zipfile.ZipFile(zipname,"w",zipfile.ZIP_DEFLATED) as zf:
                        for file in requests.get(url):
                            furl=f"{url}/{file}"
                            fres=requests.get(furl)
                            if fres.status_code==200:
                                zf.writestr(file,fres.content)
                    print("Folder Downloaded Successfully")
                    executiontest(dir+"/"+zipname)
                    break
                except Exception as e:
                    print(e,"\nFolder cannot be downloaded")
                    break
            else:
                x=downloadlinkredir(url)
                y=int(input("Enter Download link no:"))
                filedownload(x[y-1])
                break
def downloadparts(url,start,end,parts):
    pass
def downloader(dir="/home/yash/Downloads"):
    while True:
        print(f"File Downloader\nDownload:\n1-Video/Music\n2-Files from url\n3-Exit")
        d=int(input("Enter choice:"))
        if d==1:
            url=input("Enter Video Title/Music Title or paste URL:")
            conndownloadcheck(url)
            break
        elif d==2:
            url=input("Paste Download Link:")
            conndownloadcheck(url)
            x=requests.head(url).headers.get("Content-Size")
            if x<=20971520:
                maldownloadcheckl(url)
                filedownload(url,dir)
                break
            else:
                filedownload(url,dir)
                maldownloadcheckf(url)
                break
        elif d==3:
            break
        else:
            print("Invalid choice")
            continue
def executiontest(file):
    exe=sandboxie.Sandboxie()
    exe.create_sandbox(box="test",options={"Enabled":"yes"})
    try:
        exe.start(file,box="test",wait=False)
        for i in exe.running_processes(box="test"):
            print(i)
        exe.terminate_all_processes(box="test")
        exe.delete_contents(box="test")
        exe.destroy_sandbox(box="test")
    except Exception as e:
        exe.terminate_all_processes(box="test")
        exe.delete_contents(box="test")
        exe.destroy_sandbox(box="test")
        print(e)
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
def searchfile(file,dir,f=0):
    dirfile=os.listdir(dir)        
    try:    
        for i in dirfile:
            if os.path.isfile(dir+"/"+i):
                if i==file:
                    print("found in "+dir)
            elif os.path.isdir(dir+"/"+i):
                searchfile(file,dir+"/"+i,f)
    except FileNotFoundError:
        print("not found")
#searchfile("Readme.asset","/home/yash/My project")

def rename(file,dir,i=1,n=""):
    if n=="":
        while True:
            try:
                if os.path.isfile(dir+"/"+file):
                    x=dir+"/"+n+"[{}]".format(i)+os.path.splitext(file)[1]
                    try:
                        os.rename(dir+"/"+file,x)
                    except FileExistsError:
                        i=i+1
                        rename(file,dir,i)
                    print("done")
                elif os.path.isdir(dir+"/"+file):
                    x=dir+"/"+n
                    try:
                       os.rename(dir+"/"+file,x)
                    except Exception:
                        i=i+1
                        rename(file,dir,i)
                    print("done")
            except FileNotFoundError:
                print("not found")

def delete(file,dir):
    try:
        if os.path.isfile(dir+"/"+file):
            if os.path.exists(dir+"/"+file):
                os.remove(dir+"/"+file)
                print("Deleted:"+file)
        elif os.path.isdir(dir+"/"+file):
            if os.listdir(dir+"/"+file)==[]:
                os.rmdir(dir+"/"+file)
            else:
                delete(file,dir+"/"+file)
        print("done")
    except Exception as e:
        print(e)
def copy(file,fromd,todir):
    try:
        if os.path.exists(fromd+"/"+file):
            if not os.path.exists(todir+"/"+file):
                os.system("cp -r "+fromd+"/"+file+"/. "+todir)
            else:
                while True:
                    print("File/directory exists:Compare the files/Directory and choose\n1-Rename this file/directory\n2-perform process anyway\n3-Cancel process")
                    print("Processing file:\n")
                    print("Name:",os.path.basename(fromd+"/"+file))
                    print("Size:",byte_converter(os.path.getsize(fromd+"/"+file)))
                    print("Created on:",time.ctime(os.path.getctime(fromd+"/"+file)))
                    print("Modified on:",time.ctime(os.path.getmtime(fromd+"/"+file)))
                    print("Last access on:",time.ctime(os.path.getatime(fromd+"/"+file)))
                    print("Existing file:\n")
                    print("Name:",os.path.basename(todir+"/"+file))
                    print("Size:",byte_converter(os.path.getsize(todir+"/"+file)))
                    print("Created on:",time.ctime(os.path.getctime(todir+"/"+file)))
                    print("Modified on:",time.ctime(os.path.getmtime(todir+"/"+file)))
                    print("Last access on:",time.ctime(os.path.getatime(todir+"/"+file)))
                    a=input("Choose:")
                    if a==1:
                        rename(file,fromd,i=1,x=input("Enter the new name:"))
                        copy(file,fromd,todir)
                    elif a==2:
                        os.system("cp -r "+fromd+"/"+file+"/. "+todir)
                    elif a==3:
                        print("Process cancelled")
                        break
                    else:
                        break
        print("done")
    except Exception as e:
        print(e)
def move(file,fromd,todir):
    try:
        copy(file,fromd,todir)
        delete(file,fromd)
        print("move done")
    except Exception as e:
        print(e)
def cont(dir,t=0,ext={},f=0):
    if os.path.isfile(dir):
        e=dir.split(".")[-1]
        if e not in ext:
            ext.update({"."+e:1})
        else:
            ext[e]=ext.get(e)+1
        f=sum(ext.values())
    else:
        for i in os.listdir(dir):
            t=t+1
            cont(i,t,ext,f)
    print("dir:{}\nfile:{}\n,ext:{}".format(t,f,ext))
def organizer(dir):
    pass