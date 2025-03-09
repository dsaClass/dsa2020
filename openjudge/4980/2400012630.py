from heapq import heappush, heappop

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(matrix,start) :
    n,m=len(matrix),len(matrix[0])
    visited=[[False]*m for _ in range(n)]
    q=[]
    heappush(q,(0,start[0],start[1]))
    visited[start[0]][start[1]]=True
    while len(q)!=0:
        time,x,y=heappop(q)
        for i in range(4) :
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if matrix[nx][ny]=="a" :
                    return time+1
                elif matrix[nx][ny]=="@" :
                    heappush(q,(time+1,nx,ny))
                    visited[nx][ny]=True
                elif matrix[nx][ny]=="x" :
                    heappush(q,(time+2,nx,ny))
                    visited[nx][ny]=True
    return "Impossible"

S=int(input())
for _ in range(S) :
    N,M=map(int,input().split())
    matrix=[list(input()) for _ in range(N)]
    start=None
    ans=[]
    for i in range(N) :
        for j in range(M) :
            if matrix[i][j] == "r" :
                start=(i,j)
                break
    print(bfs(matrix,start))