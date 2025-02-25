a=list(map(int,input().split()))
n,m=a[0],a[1]

mtrx=[[0 for _ in range(n)] for _ in range(n)]

vs=[0 for _ in range(n)]

for i in range(m):
    a=list(map(int,input().split()))
    mtrx[a[0]][a[1]]=1
    mtrx[a[1]][a[0]]=1
 
lp=0
def dfs(i,k):
    global lp
    vs[i]=1
    for j in range(n):
        if mtrx[i][j]==1 and vs[j]==0:
            vs[j]=1
            dfs(j,i)
        elif mtrx[i][j]==1 and j!=k and vs[j]==1:
            lp=1
            
cnn=0      
for i in range(n):
    if vs[i]==0:
        dfs(i,i)
        cnn+=1
        

if cnn==1:
    print('connected:yes')
else:
    print('connected:no')
    
if lp==0:
    print('loop:no')
else:
    print('loop:yes')
    
