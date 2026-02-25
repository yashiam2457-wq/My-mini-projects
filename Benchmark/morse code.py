#0=. 1=- 
x={'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..','0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.'}
z={' ':'/'}
s='!@#$%^&*()_+=-{\}[]:\';"|,.<>/?'
decode=''
encode=''
while(True):
    print("Enter your choice:\nA-Decode\nB-Encode")
    a=input("")
    if(a=='a' or a=='A' or a=='1'):
        d=input("Enter the morse code:")
        d=d.split('/')
        for i in d:
            i=i.split(' ')
            for j in i:
                for k in x:
                    v=x.get(k)
                    if (j==v):
                        decode=decode+k
            decode=decode+' '
        print("The deocded message:"+decode)
    elif(a=='b' or a=='B' or a=='2'):
        c=input("Enter the string:")
        for i in c:
            for j in s:
                if(i==j):
                    c=c.replace(i,'')
        c=c.lower()
        c=c.split(' ')
        for k in c:
            for l in k:
                for m in x.keys():
                    if(m==l):
                        encode=encode+x.get(m)
                encode=encode+' '
            encode=encode+'/'
        print("Your morse code:"+encode)
    else:
        print("Invalid Input!")
    
