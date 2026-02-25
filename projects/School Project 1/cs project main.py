import time, pickle, csv
print(25*'-'+'QUIZ'+26*'-')
print(24*'-'+'Project'+24*'-')
print('Made By : Yash Gupta')
def load():
        print("Please Wait! Data is loading...")
        time.sleep(2)
def quest(f,n=10):
        r=w=l=0
        x=time.time()
        y=0
        for i in range(n):
                s=pickle.load(f)
                print('Q',i+1,'-',s[0])
                print('A-',s[1])
                print('B-',s[2])
                print('C-',s[3])
                print('D-',s[4])
                ans1=input('CHOOSE THE CORRECT OPTION(a,b,c,d)or(1,2,3,4):')
                if ans1.lower()=='a' or ans1=='1':
                        if s[1]==s[5]:
                                r=r+1
                                print(7*'='+'Correct Answer'+7*'=')
                        else:
                                w=w+1
                                print(8*'!'+'Wrong Answer'+8*'!')
                elif ans1.lower()=='b' or ans1=='2':
                        if s[2]==s[5]:
                                r=r+1
                                print(7*'='+'Correct Answer'+7*'=')
                        else:
                                w=w+1
                                print(8*'!'+'Wrong Answer'+8*'!')
                elif ans1.lower()=='c' or ans1=='3':
                        if s[3]==s[5]:
                                r=r+1
                                print(7*'='+'Correct Answer'+7*'=')
                        else:
                                w=w+1
                                print(8*'!'+'Wrong Answer'+8*'!')
                elif ans1.lower()=='d' or ans1=='4':
                        if s[4]==s[5]:
                                r=r+1
                                print(7*'='+'Correct Answer'+7*'=')
                        else:
                                w=w+1
                                print(8*'!'+'Wrong Answer'+8*'!')
                elif ans1=='':
                        l=l+1
                        print(8*'#'+'Answer Leave'+8*'#')
                else:
                        l=l+1
                        print('Invalid Choice, Answer is marked as leaved')
                        continue
        y=time.time()
        print('TOTAL CORRECT ANSWER:',r)
        print('TOTAL WRONG ANSWER:',w)
        print('TOTAL ANSWER LEAVED:',l)
        print('TOTAL TIME TAKEN IN QUIZ:',int(y-x),'seconds')
        print('AVERAGE TIME TAKEN IN EACH QUESTION:',int((y-x)/n),'seconds')
        print(24*'+'+'Answers'+24*'+')
        f.seek(0)
        load()
        for i in range(n):
                s=pickle.load(f)
                print('Q',i+1,'-',s[5])
        q=[a,int(y-x),r,o]
        z=open('score.csv','r')
        r=csv.reader(z)
        m=list(r)
        for j in m:
                if (j[0]!=q[0] and j[3]==q[3]) or (j[0]==q[0] and j[3]!=q[3]):
                        if int(j[2])<q[2] and int(j[1])>q[1]:
                                s=m.index(j)
                                m.insert(s,q)
                                m.pop()
                                break
                        elif int(j[2])==q[2] or int(j[1])==q[1]:
                                s=m.index(j)
                                m.insert(s,q)
                                m.pop()
                                break
                elif j[0]==q[0] and j[3]==q[3]:
                        if (int(j[2])!=q[2] and int(j[1])==q[1]) or (int(j[2])==q[2] and int(j[1])!=q[1]):
                                s=m.index(j)
                                m.insert(s,q)
                                m.pop()
                                break
        z.close()
        z=open('score.csv','w',newline='\n')
        w=csv.writer(z)
        w.writerows(m)
        z.close()
while True:
    print(23*'='+'MAIN MENU'+23*'=')
    print('1-START THE QUIZ')
    print('2-RULES')
    print('3-SCORE')
    print('4-CREDITS')
    print('5-EXIT')
    x=input('Choose your option(1-5):')
    load()
    if x=='1':
            while True:
                    a=input('PLAYER NAME:')
                    print(23*'='+'QUIZ MENU'+23*'=')
                    print('1-SUPERHERO QUIZ')
                    print('2-ANIME QUIZ')
                    print('3-SPORTS QUIZ')
                    print('4-CURRENT AFFAIRS QUIZ')
                    print('5-COMPUTER BASED QUIZ')
                    print('6-EXIT')
                    y=input('Choose your option(1-6):')
                    load()
                    if y=='1':
                            s=open('superhero.dat','rb')
                            o='Superhero'
                            quest(s,15)
                            break
                    elif y=='2':
                            while True:
                                    print(20*'='+'ANIME QUIZ MENU'+20*'=')
                                    print('1-NARUTO')
                                    print('2-ONE PIECE')
                                    print('3-JUJUTSU KAISEN')
                                    print('4-POKEMON')
                                    print('5-FULLMETAL ALCHEMIST BROTHERHOOD')
                                    print('6-EXIT')
                                    z=input('Choose your option(1-6):')
                                    load()
                                    if z=='1':
                                            m=open('naruto.dat','rb')
                                            o='Naruto'
                                            quest(m)
                                            break
                                    elif z=='2':
                                            m=open('onepiece.dat','rb')
                                            o='One Piece'
                                            quest(m)
                                            break
                                    elif z=='3':
                                            j=open("jujutsukaisen.dat",'rb')
                                            o='Jujutsu Kaisen'
                                            quest(j)
                                            break
                                    elif z=='4':
                                            p=open('pokemon.dat','rb')
                                            o='Pokemon'
                                            quest(p)
                                            break
                                    elif z=='5':
                                            d=open('fullmetal.dat','rb')
                                            o='Fullmetal Alchemist Brotherhood'
                                            quest(d)
                                            break
                                    elif z=='6':
                                            break
                                    else:
                                            print("Invalid Choice")
                    elif y=='3':
                            while True:
                                    print(20*'='+'SPORTS QUIZ MENU'+19*'=')
                                    print('1-CRICKET')
                                    print('2-VOLLEYBALL')
                                    print('3-FOOTBALL')
                                    print('4-EXIT')
                                    z=input('Choose your option(1-4):')
                                    load()
                                    if z=='1':
                                            c=open('cricket.dat','rb')
                                            o='Cricket'
                                            quest(c)
                                            break
                                    elif z=='2':
                                            v=open('volleyball.dat','rb')
                                            o='Volley Ball'
                                            quest(v)
                                            break
                                    elif z=='3':
                                            f=open('football.dat','rb')
                                            o='Football'
                                            quest(f)
                                            break
                                    elif z=='4':
                                            break
                                    else:
                                            print('Invalid Choice')
                    elif y=='4':
                            a=open('affairs.dat','rb')
                            o='Current Affairs'
                            quest(a)
                            break
                    elif y=='5':
                            c=open('computer.dat','rb')
                            o='Computer Based'
                            quest(c)
                            break
                    elif y=='6':
                            break
    elif x=='2':
            e=open('rules.txt')
            print(e.read())
    elif x=='3':
            e=open('score.csv')
            print(25*'='+'SCORE'+25*'=')
            a=list(csv.reader(e))
            print('PLAYER NAME-TOTAL TIME-RIGHT ANSWER-QUIZ')
            for i in a:
                    print(i)
    elif x=='4':
            e=open('credits.txt')
            print(e.read())
    elif x=='5':
            break
    else:
            continue
