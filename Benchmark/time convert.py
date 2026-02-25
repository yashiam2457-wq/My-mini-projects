x= int(input('year:'))
if x%4 ==0:
    if x%100 ==0:
        if x%400 ==0:
            q=366
        else:
            q=365
    else:
        q=366
else:
    q=365
d=x*12
print('in months:',d)
f=x*52
print('in weeks:',f)
e=x*q
print('in days:',e)
g=24*e
print('in hours:',g)
h=g*60
print('in minutes:',h)
i=h*60
print('in seconds:',i)
