n=int(input())
an=0
ans=[]
def cf(n,m,zc,a):
    global an
    if zc==1:
        if 1<=n<=9:
            b=a+'0'+str(n)
        else:
            b=a+str(n)
        ans.append(b)
        an+=1
    else:
        x=m
        while True:
            if (x+zc-1)*zc<=n:
                b=a
                if 1<=x<=9:
                    b=b+'0'+str(x)
                else:
                    b=b+str(x)
                cf(n-x,x+2,zc-1,b)
            else:
                break
            x+=2
if n%2==1:
    y=int((n**0.5)*0.5+0.5)
    for i in range(y,0,-1):
        cf(n,1,i*2-1,'')
    

else:
    y=int((n**0.5)*0.5)
    for i in range(y,0,-1):
        cf(n,1,i*2,'')
ans.sort()
for i in ans:
    for j in range(0,len(i),2):
        print(int(i[j:j+2]),end=' ')
    print()
print(an)
    
        
            
    
