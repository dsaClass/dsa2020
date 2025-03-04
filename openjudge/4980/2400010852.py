import heapq
s=int(input())
for _ in range(s):
    n,m=map(int,input().split())
    maze=[]
    for _ in range(n):
        row=list(input().strip())
        maze.append(row)
    for i in range(n):
        for j in range(m):
            if maze[i][j]=='r':
                start=(i,j)
            elif maze[i][j]=='a':
                end=(i,j)
    dist=[[float('inf')]*m for _ in range(n)]
    a,b=start
    dist[a][b]=0
    heap=[]
    heapq.heappush(heap,(0,a,b))
    directions=[(0,1),(0,-1),(1,0),(-1,0)]
    found=False
    while heap:
        t,i,j=heapq.heappop(heap)
        if (i,j)==end:
            print(t)
            found=True
            break
        if t>dist[i][j]:
            continue
        for dx,dy in directions:
            di,dj=i+dx,j+dy
            if 0<=di<n and 0<=dj<m:
                c=maze[di][dj]
                if c=='#':
                    continue
                elif c=='x':
                    new_t=t+2
                else:
                    new_t=t+1
                if new_t<dist[di][dj]:
                    dist[di][dj]=new_t
                    heapq.heappush(heap,(new_t,di,dj))
    if not found:
            print('Impossible')
