#标准的dfs题
from collections import deque
directions=[[-1,0],[1,0],[0,-1],[0,1]]
def fastest(migong,x,y,r,c,k):
    time =0
    queue = deque()
    queue.append((x,y))
    visited=[[[0]*k for i in range(c)] for j in range(r)]
    visited[x][y][0]=1
    while queue:
        time+=1
        for _ in range(len(queue)):
            nx, ny = queue.popleft()
            for i in directions:
                dx, dy = nx + i[0], ny + i[1]
                if 0 <= dx < r and 0 <= dy < c and visited[dx][dy][time%k]==0:
                    if migong[dx][dy] == 'E':
                        return time
                    elif migong[dx][dy] == '.' or migong[dx][dy]=='S':
                        queue.append((dx, dy))
                        visited[dx][dy][time%k]=1
                    else:
                        if time % k == 0:
                            queue.append((dx, dy))
                            visited[dx][dy][time%k]=1
    return 'Oop!'
ans = []
T=int(input())
for i in range(T):
    R,C,K=map(int,input().split())
    migong=[]
    for u in range(R):
        migong.append(list(str(input())))
    for ii in range(R):
        for jj in range(C):
            if migong[ii][jj]=='S':
                ans.append(fastest(migong,ii,jj,R,C,K))
                break
for i in ans:
    print(i)

