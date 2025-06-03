from collections import deque

def bfs(plat,n,k):
    q=deque([(0,0,0)])
    ans = 0
    while q:#确定当前位置
        for _ in range(len(q)):
            l,m,placed=q.popleft()
            if placed==k:
                ans+=1
                continue
            if n - m < k - placed:
                continue
            for i in range(n):
                if not l & 1<<i and plat[m][i]=="#":
                    q.append((l | (1<<i),m+1,placed+1))
            q.append((l,m+1,placed))
    return ans

while True:
    n,k = map(int,input().split())
    if n==k==-1:
        break
    plat = [input() for _ in range(n)]
    print(bfs(plat,n,k))