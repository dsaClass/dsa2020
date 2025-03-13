n,m=map(int,input().split())
a=list(map(int,input().split()))
for i in range(m):
    check=input().split()
    if(check[0]=='C'):
        for j in range(n):
            a[j]=(a[j]+int(check[1]))%65536
    else:
        s=0
        k=int(check[1])
        for j in range(n):
            if((a[j]//2**(k))%2==1):
                s+=1
        print(s)
    
