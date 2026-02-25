'''import matplotlib.pyplot as plt
import numpy
x=numpy.array([0,1,2,3,4,5])
y=numpy.array([2,10,6,4,4,12])
#plt.plot(x,y,marker="o",color="b")
ca=["A","B","C","D","E","F"]
#plt.barh(x,y,color="b")
#plt.scatter(x,y,color="skyblue")
#plt.pie(y,labels=ca)
#plt.fill_between(x,y,color="b")
plt.title("Test Pie Chart")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(axis="y",linestyle="solid",alpha=1)
plt.show()'''
'''import numpy
import statistics
x=[[1,2,3,4,5,6],[7,8,9,10,11,12]]
y=numpy.array(x)
#print(numpy.array(x),x,sep='\n')
#print(numpy.sum(y),sum(y),sep="\n")
#print(numpy.mean(y),statistics.mean(x[0]),sep="\n")
#print(numpy.transpose(x))
print(y*10)'''
#plt.pie(s,labels=l,colors=c,startangle=90,shadow=True,explode=(0,0,0,0.1,0),autopct="%1.1f%%")
'''import pandas
import numpy
x={"A":[1,2,3,4,5,6],"B":[7,8,9,10,11,12],"C":[13,14,15,16,17,numpy.nan]}
y=pandas.DataFrame(x)
#print(x,y,sep="\n")
#print(y.loc[2,"A"])
#print(y.loc[4,:])
#print(y.loc[:,["A","C"]])
#y.isna()
#y.fillna(4)
#z=y.apply(lambda x:x**2)
#print(y.describe())
#print(y.dtypes)
#print(y.info())
#print(y.shape)
#print(y["A"]>3)
#print(y[y["A"].isin([1,3,5])])
#print(y.iloc[2:4,1:])
y.iloc[0:4,2]="anonymous"
print(y.head())'''
def isfib(x):
    s1,s2=int(pow(5*x*x+4,1/2)),int(pow(5*x*x-4,1/2))
    return ((s1*s1==5*x*x+4)or(s2*s2==5*x*x-4))
def lsno(l,x):
    e=[i for i in l if i<x]
    return e
def rmvn(s,n):
    return (s[:n]+s[n+1:])
def digwor(f):
    try:
        with open(f,"r") as t:
            x=t.read()
            for i in x:
                w=i.split(" ")
                d=[e for e in w if e.isdigit()]
                print(d)
    except FileNotFoundError:
        print("File not found")
import pandas as pd
import matplotlib.pyplot as plt
def reddat(f):
    d=pd.read_csv(f)
    if d.empty:
        print("Enpty dataset")
        return None
    if len(d.columns)<2:
        print("dataset is too small")
        return None
    l=d.iloc[:,-1].values
    dat=d.iloc[:,:-1].values
    plt.figure()
    plt.scatter(dat[:,0],dat[:,1])
    plt.xlabel(d.columns[0])
    plt.ylabel(d.columns[1])
    plt.grid(True)
    plt.show()
    return dat,l
def factor(x):
    return [i for i in range(1,x+1) if (x%i==0)]
def csqr(x):
    return len([i for i in range(1,x+1) if((int(pow(i,1/2))**2)==i)])
def select(ls):
    for i in range(len(ls)):
        m=i
        for j in range(i+1,len(ls)):
            if ls[j]<ls[m]:
                m=j
                ls[i],ls[m]=ls[m],ls[i]
    return ls
'''import matplotlib.pyplot as plt
x=["Meat","Banana","Avocardo","Sweet Potato","Spinach","watermelon","Coconut water","Bean","Legumes","Tomato"]
y1=[250,130,140,120,20,20,10,50,40,19]
y2=[40,55,20,30,40,32,10,26,25,20]
y3=[8,5,3,6,1,1.5,0,2,1.5,2.5]
plt.plot(x,y1,label="Calories",color="b")
plt.plot(x,y2,label="Potassium",color="r")
plt.plot(x,y3,label="Fat",color="y")
plt.title("Food characteristics Chart")
plt.xlabel("Food")
plt.ylabel("Characteristics")
plt.legend()
plt.grid(True)
plt.show()'''
