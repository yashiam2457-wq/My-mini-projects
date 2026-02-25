import random
while True:
    x=eval(input('Enter your options:'))
    y=len(x)
    while True:
        z=random.randrange(y)
        print('Your random choice is ',x[z])
        w=input('Spin again(y/n):')
        if w.lower()=='n':
            break
    a=input('Spin again with new options(y/n):')
    if a.lower()=='n':
        break
    
    
