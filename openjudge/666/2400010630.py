def pg(i,m,n):
    if i*n>m:
        return 0
    else:
        if n==1:
            return 1
        else:
            s=0
            for j in range(i,int(m/n)+1):
                s+=pg(j,m-j,n-1)
            return s
t=int(input())
for i in range(t):
    m,n=input().split()
    m=int(m)
    n=int(n)
    print(pg(0,m,n))
