def dfs(x,y,visited,map,count):
    visited[x][y]=True
    count+=1
    row=len(map)#行数
    col=len(map[0])#列数
    directions=[(0,1),(1,0),(-1,0),(0,-1)]
    for dx,dy in directions:
        nx=x+dx
        ny=y+dy
        if 0<=nx<=row-1 and 0<=ny<=col-1 and not visited[nx][ny] and map[nx][ny]==0:
            count=dfs(nx,ny,visited,map,count)
    return count
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    maps=[[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        a=input()
        a=list(str(a))
        for j in range(n):
            if a[j]=='#':
                maps[i][j]=1
            elif  a[j]=='.':
                
                maps[i][j]=0
            else:
                maps[i][j]=0
                current_x=i
                current_y=j 
    visited=[[0 for _ in range(n)] for _ in range(m)]
    print(dfs(current_x,current_y,visited,maps,0))