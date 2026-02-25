import requests
import PIL
import pickle as p
urls=[]
file={}
a=[["Anime","Naruto",0],["Anime","Fairy Tail",0],["Anime","Bleach",0],["Anime","One Piece",0],["Anime","Jujutsu Kaisen",0],
       ["Anime","Akame Ga Kill",0],["Anime","Danmachi",0],["Anime","Dandadan",0],["Anime","Hidden Dungeon Only I can Enter",0],
       ["Anime","Steins;Gate",0],["Anime","Code Geass",0],["Anime","Death Note",0],["Anime","Evangelion",0],["Anime","Attack On Titan",0],
       ["Anime","Haikyuu",0],["Anime","One Punch Man",0],["Anime","Re:Zero",0],["Anime","Erased",0],["Anime","Black Clover",0],
       ["Anime","Sword Art Online",0],["Anime","Frieren",0],["Anime","Noragami",0],["Anime","KonoSuba",0],["Anime","Darling in The Franxx",0],
       ["Anime","Overlord",0],["Anime","Rising of a Shield Hero",0],["Anime","Kakegurui",0],["Anime","Assassination Classroom",0],
       ["Anime","Pokemon",0],["Anime","Classroom of Elite",0],["Anime","Apothecary Diaries",0],["Anime","Demon Slayer",0],
       ["Anime","Bunny Girl Senpai",0],["Anime","Ghost in the Shell",0],["Anime","Eminence in the Shadow",0],["Anime","My Hero Academia",0],
       ["Anime","ChainSaw Man",0],["Anime","Future Diary",0],["Anime","Spy x Family",0],["Anime","Solo Leveling",0],["Anime","Zom 100",0],
       ["Anime","7th Time Loop",0], ["Anime","Cautious Hero",0],["Anime","Unwanted Undead Adventurer",0],["Anime","Summer Time Rendering",0],
       ["Anime","7 deadly Sins",0],["Anime","Kaiju no 8",0],["Anime","Why Does Nobody Remember Me in This World",0],["Anime","Cyberpunk Edge Runner",0],
       ["Anime","Arifureta",0],["Anime","Oshi No Ko",0],["Anime","I am Quiting Heroing",0],["Anime","How a Realist Hero Rebuilt the Kingdom",0],
       ["Anime","Let This Grieving Soul Retire",0],["Anime","Kengin Ashura",0],["Anime","Asterisk War",0],["Anime","Hunter x Hunter",0],
       ["Anime","Orient",0],["Anime","I\'m the Evil Lord of an Intergalactic Empire",0],["Anime","Deadman Wonderland",0],["Anime","Witch Craft Works",0],
       ["Anime","Mashle",0],["Anime","Prison School",0],["Anime","Plunderer",0],["Video Game","Tekken",0],["Anime","Zero Louise",0],
       ["Video Game","Street Fighter",0],["Video Game","King of Fighter",0],["Video Game","Soul Calibur",0],["Video Game","Resident Evil",0],
       ["Video Game","Cyberpunk 2077",0],["Video Game","Metroid",0],["Video Game","Bayonetta",0],["Video Game","Nier Automata",0],
       ["Video Game","God of War",0],["Video Game","Legend of Zelda",0],["Video Game","Bioshock",0],["Video Game","Metal Gear Solid",0],
       ["Video Game","Red Dead Redemption",0],["Video Game","Last of Us",0],["Video Game","Mario",0],["Video Game","Detroit:Become Human",0],
       ["Video Game","Final Fantasy",0],["Video Game","Dead or Alive",0],["SuperHero","Marvel",0],["SuperHero","DC",0],["Video Game","Mortal Kombat",0]]
def datacount(sav):
    # category- [cat, subcat, count]
    # character- [name, subcat, link]
    x=""
    with open(sav,"w") as f:
        with open("Superherolist.txt", "r",encoding="utf-8-sig") as f1:
            x=f1.readlines()
            for i in a:
                c=0
                if i[0]=="SuperHero":
                    for j in x:
                        if i[1].lower()==j.split(",")[0][2:len(j.split(",")[0])-1].lower():
                            c=c+1
                print(f"{i[1]} = {c}")
                f.write(f"{i[0]},{i[1]},{c}\n")
        f.close()
    with open(sav,'r') as s:
        r=s.readlines()
        for i in r:
            print(i,end="\n")
#dataprep("C:\\Users\\Loq\\Documents\\programs\\minipro\\MyFMKgame\\category.txt")

#File compatibility check
'''a=""
c=""
with open("C:\\Users\\Loq\\Documents\\programs\\Superherolist.txt",'r',encoding="utf-8-sig") as f:
    with open("C:\\Users\\Loq\\Documents\\programs\\minipro\\MyFMKgame\\category.txt",'r') as rem:
        a=rem.read().split('\n')
        b=[i.split(",")[1] for i in a]
    c=f.read().split("\n")
    d=[i.split(",")[0] for i in c]
    for i in b:
        if i not in d:
            print(i)
'''

# n- list of characters to download
# newline is must for searching images
# Make sure that API is unstable so beware befpre doing preview
n=''''''
QUERIES = n.split('\n')

import asyncio
import aiohttp
from duckduckgo_search import DDGS
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import os
import time
IMAGES_PER_QUERY = 9
MIN_WIDTH = 1280
MIN_HEIGHT = 720
MAX_CONCURRENT_DOWNLOADS = 12
REQUEST_TIMEOUT = 4
QUERY_DELAY = 0.8
HEADERS = {"User-Agent": "Mozilla/5.0"}
def get_candidate_urls(query):
    """FAST: pre-filter using DDG metadata"""
    urls = []
    with DDGS() as ddgs:
        for r in ddgs.images(
            keywords=query,
            safesearch="off",
            size="Large",
            max_results=120
        ):
            if (
                r.get("width", 0) >= MIN_WIDTH and
                r.get("height", 0) >= MIN_HEIGHT
            ):
                urls.append(r["image"])

            if len(urls) >= IMAGES_PER_QUERY * 2:
                break
    return urls
async def fetch_image(session, sem, url):
    async with sem:
        try:
            async with session.get(url, timeout=REQUEST_TIMEOUT) as r:
                data = await r.read()
                img = Image.open(BytesIO(data)).convert("RGB")
                return img, data
        except:
            return None, None
async def download_images(urls, needed):
    images, raw = [], []
    sem = asyncio.Semaphore(MAX_CONCURRENT_DOWNLOADS)
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        tasks = [fetch_image(session, sem, u) for u in urls]
        for coro in asyncio.as_completed(tasks):
            img, data = await coro
            if img:
                images.append(img)
                raw.append(data)

            if len(images) == needed:
                break
    return images, raw
def preview(images, query):
    plt.figure(figsize=(16, 10))
    for i, img in enumerate(images):
        plt.subplot(3, 3, i + 1)
        plt.imshow(img)
        plt.axis("off")
        plt.title(f"ID {i}", fontsize=11)
    plt.suptitle(query, fontsize=18)
    plt.tight_layout()
    plt.show()
import os
import struct
import mmap

# mmap file for database file for game
FILE = "Superhero.mmap"

HEADER_FORMAT = "QIIQ"  # total_size, s1_len, s2_len, img_len
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
def add_record(s1: str, s2: str, image_path: str):
    s1_b = s1.encode()
    s2_b = s2.encode()
    with open(image_path, "rb") as img_file:
        img_b = img_file.read()
    total_size = HEADER_SIZE + len(s1_b) + len(s2_b) + len(img_b)
    header = struct.pack(
        HEADER_FORMAT,
        total_size,
        len(s1_b),
        len(s2_b),
        len(img_b)
    )
    record = header + s1_b + s2_b + img_b
    with open(FILE, "ab") as f:
        f.write(record)
def delete_record(file_path, target_s1, target_s2):
    if not os.path.exists(file_path):
        print("File not found")
        return False
    temp_path = file_path + ".tmp"
    deleted = False
    with open(file_path, "rb") as f_in, open(temp_path, "wb") as f_out:
        mm_local = mmap.mmap(f_in.fileno(), 0, access=mmap.ACCESS_READ)
        offset = 0
        size = len(mm_local)
        while offset + HEADER_SIZE <= size:
            total_size, s1_len, s2_len, img_len = struct.unpack_from(
                HEADER_FORMAT, mm_local, offset
            )
            base = offset + HEADER_SIZE
            s1 = mm_local[base:base+s1_len].decode().strip()
            base += s1_len
            s2 = mm_local[base:base+s2_len].decode().strip()
            record_bytes = mm_local[offset:offset+total_size]
            if not deleted and s1 == target_s1 and s2 == target_s2:
                print("Deleted:", s1, s2)
                deleted = True
            else:
                f_out.write(record_bytes)
            offset += total_size
        mm_local.close()
    os.replace(temp_path, file_path)
    return deleted
'''
if __name__ == "__main__":
    os.makedirs("downloads", exist_ok=True)
    loop = asyncio.get_event_loop()
    for qi, query in enumerate(QUERIES):
        print(f"\n[{qi+1}/{len(QUERIES)}] {query}")
        urls = get_candidate_urls(query)
        if len(urls) < IMAGES_PER_QUERY:
            print("Not enough high-res candidates, skipping.")
            continue
        images, raw = loop.run_until_complete(
            download_images(urls, IMAGES_PER_QUERY)
        )
        if len(images) < IMAGES_PER_QUERY:
            print("Download failed, skipping.")
            continue
        preview(images, query)
        choice = input(
            "Download IDs (e.g. 0,2,5) | n | q: "
        ).lower()
        if choice == "q":
            break
        if choice != "n":
            for i in map(int, choice.split(",")):
                fname = f"downloads/{query.replace(' ','_')}_{i}.jpg"
                with open(fname, "wb") as f:
                    f.write(raw[i])
                print(f"Saved → {fname}")
        time.sleep(QUERY_DELAY)
    print("\nDone.")'''