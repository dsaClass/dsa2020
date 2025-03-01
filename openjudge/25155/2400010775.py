a=list(map(int,input().split()))
n,m=a[0],a[1]

mtrx=[[0 for _ in range(n)] for _ in range(n)]

vs=[0 for _ in range(n)]

for i in range(m):
    a=list(map(int,input().split()))
    mtrx[a[0]][a[1]]=1
    mtrx[a[1]][a[0]]=1

a1=[]   
def dfs(i):
    global a1
    a1.append(str(i))
    vs[i]=1
    for j in range(n):
        if mtrx[i][j]==1 and vs[j]==0:
            vs[j]=1
            dfs(j)
            
for i in range(n):
    if vs[i]==0:
        dfs(i)
        
print(' '.join(a1))