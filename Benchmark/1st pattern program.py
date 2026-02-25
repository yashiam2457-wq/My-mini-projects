print("1:Simple Number Triangle Pattern")
for a in range(6):
    for b in range(a):
        print(a, end=" ")
    print(" ")
print("2:Inverted Pyramid of Numbers")
b=0
for a in range(5, 0, -1):
    b += 1
    for c in range(1, a + 1):
        print(b, end=' ')
    print('\r')
print("3:Half Pyramid Pattern of Numbers")
for x in range(1, 6):
    for y in range(1,x+1):
        print(y, end=' ')
    print("")
print("4:Inverted Pyramid of Descending Numbers")
for a in range(5, 0, -1):
    for b in range(0, a):
        print(a, end=' ')
    print("\r")
print("5:Inverted Pyramid of the Same Digit")
for a in range(5, 0, -1):
    for b in range(0, a):
        print(5, end=' ')
    print("\r")
print("6:Reverse Pyramid of Numbers")
for a in range(1,6):
    for b in range(a,0, -1):
        print(b, end=' ')
    print("")
print("7:Inverted Half Pyramid Number Pattern")
for a in range(5, 0, -1):
    for b in range(0, a + 1):
        print(b, end=' ')
    print("\r")
print("8:Pyramid of Natural Numbers Less Than 10")
z=1
a=2
for x in range(3):
    for y in range(1, a):
        print(z, end=' ')
        z += 1
    print(" ")
    a += 2
print("9:Reverse Pattern of Digits from 10")
c=1
d=2
e=d
for a in range(2, 6):
    for b in range(c, d):
        e -= 1
        print(e, end='')
    print("")
    c = d
    d += a
    e=d
print("10:Unique Pyramid Pattern of Digits")
for a in range(1, 7):
    for b in range(1, a - 1):
        print(b, end=" ")
    for b in range(a - 1, 0, -1):
        print(b, end=" ")
    print(" ")
print("11:Connected Inverted Pyramid Pattern of Numbers")
for a in range(0, 6):
    for b in range(5, a, -1):
        print(b, end='')
    for c in range(a):
        print(end='')
    for d in range(a + 1, 6):
        print(d, end='')
    print('\n')
print("12:Even Number Pyramid Pattern")
l=10
for b in range(1, 6):
   e=l
   for c in range(b):
      print(e, end=' ')
      e -= 2
   print("\r")
print("13:Pyramid of Horizontal Tables")
for x in range(0, 7):
    for y in range(0, x + 1):
        print(x * y, end=' ')
    print('')
print("14:Pyramid Pattern of Alternate Numbers")
a=1
while a <= 5:
    b = 1
    while b <= a:
        print((a * 2 - 1), end=" ")
        b = b + 1
    a = a + 1
    print('')
print("15:Mirrored Pyramid (Right-angled Triangle) Pattern of Numbers")
for x in range(1, 6):
   y= 1
   for z in range(6, 0, -1):
      if z > x:
         print(" ", end=' ')
      else:
         print(y, end=' ')
         y += 1
   print("")
print("16:Equilateral Triangle with Stars (Asterisk Symbol)")
m = 12
for x in range(0, 7):
    for y in range(0, m):
        print(end=" ")
    m = m - 1
    for y in range(0, x + 1):
        print("A", end=' ')
    print(" ")
print("17:Downward Triangle Pattern of Stars")
c=8
for a in range(5, -1, -1):
    for b in range(c, 0, -1):
        print(end=" ")
    c = c + 1
    for b in range(0, a + 1):
        print("* ", end=" ")
    print("")
print("18:Pyramid Pattern of Stars")
for x in range(0, 5):
    for y in range(0, x + 1):
        print("* ", end='')
    print("\r")
print("19:Half Pyramid Pattern of Alphabets")
for x in range(1, 6):
    for y in range(65, x+65):
        ch = chr(y)
        print(ch, end=" ")
    print("")
print("20:Horizontal Pyramid Pattern of Stars")
for x in range(0,5):   
    for y in range(0, x + 1):  
        print("*", end=' ') 
    print(" ")    
for i in range( 6+ 1, 0, -1):  
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")
#word revese triangle
x='PYTHON'
for i in range(len(x),0,-1):
    for j in range(0,i):
        print(x[j],end='')
    print('\r')
'''x=[23,12,45,67,55]
y=0
for i in x:
	if y<i:
		y=i
print(y)'''
