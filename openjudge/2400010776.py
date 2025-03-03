l=input().split(maxsplit=2)
r=int(l[0])
c=int(l[1])
print(l[2])
def f(x):
    zhi=str(bin(ord(x)))
    return zhi[-5:]
m=''
for i in l[2]:
    m=m+f(i)
m=m+'0'*(r*c-len(m))
z=[]
for _ in range(r):
    z.append([0]*c)
t1,t2=0,0
num=0

for _ in range(r*c):
    z[t1][t2]=m[num]
    num+=1
    if t1<=r//2:
        if t2 <=c//2:
            if t1<=t2+1:
                t2+=1
            else:
                t1-=1
        else:
            if t1+t2>=c-1:
                t1+=1
            else:
                t2+=1
    else:
        if t2 <= c // 2:
            if t1+t2>=r:
                t2-=1
            else:
                t1-=1
        else:
            if t1-r>=t2-c:
                t2-=1
            else:
                t1+=1
for i in range(r):
    for j in range(c):
        print(z[i][j],end='')

