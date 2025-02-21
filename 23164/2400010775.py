a=list(map(int,input().split()))
n,m=a[0],a[1]

p=[["#" for _ in range(m+2)]]
for i in range(n):
    p.append(['#']+[ch for ch in input()]+['#'])
p.append(["#" for _ in range(m+2)])
max1=0
roomarea=0

q=[[0 for _ in range(m+2)] for _ in range(n+2)]
    
def dfs(i,j):
    global roomarea
    roomarea+=1
    if p[i-1][j]=='.' and q[i-1][j]==0: 
        q[i-1][j]=1
        dfs(i-1,j)
    if p[i+1][j]=='.' and q[i+1][j]==0: 
        q[i+1][j]=1
        dfs(i+1,j)
    if p[i][j-1]=='.' and q[i][j-1]==0: 
        q[i][j-1]=1
        dfs(i,j-1)
    if p[i][j+1]=='.' and q[i][j+1]==0:
        q[i][j+1]=1
        dfs(i,j+1)
        
ans=0
for i in range(n+2):
    for j in range(m+2):
        if p[i][j]=="." and q[i][j]==0:
            roomarea=0
            dfs(i,j)
            max1=max(roomarea,max1)
            ans+=1 
            
print(ans)
print(max1-1)