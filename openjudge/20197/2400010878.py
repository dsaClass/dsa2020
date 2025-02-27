n,m=map(int,input().split())
s=n*m
count=0
while s >0:
    if n>=m:
        s-=m*m
        n,m=m,(n-m)
        count+=1
    else:
        s -= n * n
        m,n=n,(m-n)
        count+=1
print(count)