import random
o={}
w=int(input('No of options:'))
for i in range(1,w+1):
    p=input('Option'+str(i)+':')
    if p not in o:
        o.update({i:p})
print(o)
for i in range(3):
    r=random.randint(1,w)
    print('Random Pick:',o.get(r))

    
