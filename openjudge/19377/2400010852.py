from collections import deque
def count_reachable(adj,start,n):
    visited=[False]*(n+1)
    q=deque([start])
    visited[start]=True
    count=0
    while q:
        u=q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v]=True
                count+=1
                q.append(v)
    return count
n,m=map(int,input().split())
adj_forward=[[] for _ in range(n+1)]
adj_backward=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    adj_forward[a].append(b)
    adj_backward[b].append(a)
result=0
for i in range(1,n+1):
    forward=count_reachable(adj_forward,i,n)
    backward=count_reachable(adj_backward,i,n)
    if forward+backward==n-1:
        result+=1
print(result)
