import random,os,sys
folder=os.listdir(os.getcwd())
file=random.choice(folder)
ext3=['.mp3']
print('First random pick: '+file)
while file[-4:] not in ext3 :
    print('Not an MP3 file  : '+file)
    file=random.choice(folder)
else:
    os.startfile(file)
    print('Song name: '+file)
sys.exit()
