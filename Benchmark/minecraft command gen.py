x="/fill -675 191 -825 -675 191 -784 minecraft:gold_block"
y=x[6:35].split(" ")
for i in range(5):
    y[0]=y[3]=str(int(y[0])-1)
    y[1]=y[4]=str(int(y[1])+1)
    y[2]=str(int(y[2])+1)
    y[5]=str(int(y[5])-1)
    print(x[:6]+ " ".join(y) + x[35:])
    #/fill -651 167 -849 -651 167 -760 minecraft:gold_block
