from math import log2
def f(x):
    f=x**2+x+1+log2(x)
    return f
blist=[]
while True:
    try:
        y=int(input())
    except:
        break
    else:
        x=1
        while f(x)<y:
            x+=1
        x=x-0.5
        for i in range(2,100):
            if f(x)>y:
                x=x-0.5**i
            else:
                x=x+0.5**i
        blist.append(round(x,4))
for i in blist:
    print(i)
        
