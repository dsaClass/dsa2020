def f(maze,x,y,visited,n,m):
    if x==n-1 and y==m-1:
        return 1
    visited[x][y]=True  #标记走过的点
    count=0
    d=[(-1,0),(1,0),(0,-1),(0,1)]
    for dx,dy in d:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maze[nx][ny]=='.':
            count+=f(maze,nx,ny,visited,n,m)
    visited[x][y]=False  #取消标记，使接下来的其他路径可以使用
    return count
n,m=map(int,input().split())
maze=[]
for i in range(n):
    maze.append(list(input()))
visited=[[False]*m for _ in range(n)]
print(f(maze,0,0,visited,n,m))
