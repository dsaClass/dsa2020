def f(l,n,m):
    bdp=[0]*n
    ndp=[0]*n
    bdp[0]=l[0][0]
    ndp[0]=l[0][1]
    for i in range(1,n):
        bdp[i]=max(bdp[i-1]+l[i][0],ndp[i-1]+l[i][0]-m)
        ndp[i]=max(ndp[i-1]+l[i][1],bdp[i-1]+l[i][1]-m)
    return max(bdp[n-1],ndp[n-1])
n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
print(f(l,n,m))
