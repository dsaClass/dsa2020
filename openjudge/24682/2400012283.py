from collections import deque
n,r=map(int,input().split())
parent=[0]*(n+1)
depth=[0]*(n+1)
adj=[[]for _ in range(n+1)]#构建邻列表
for _ in range(n-1):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
q=deque([r])
depth[r]=0
parent[r]=r
while q:
    u=q.popleft()
    for v in adj[u]:
        if parent[v]==0 and v!=parent[u]:
            parent[v]=u
            depth[v]=depth[u]+1
            q.append(v)
def lca(x,y):
    if depth[x]<depth[y]:
        x,y=y,x
    while depth[x]>depth[y]:
        x=parent[x]
    while x!=y:
        x=parent[x]
        y=parent[y]
    return x
q=int(input())
for _ in range(q):
    x,y =map(int,input().split())
    print(lca(x,y))