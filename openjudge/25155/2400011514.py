n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# 对每个顶点的邻接列表进行升序排序，以确保访问顺序
for neighbors in adj:
    neighbors.sort()

visited = [False] * n
result = []

def dfs(u):
    visited[u] = True
    result.append(u)
    for v in adj[u]:
        if not visited[v]:
            dfs(v)

# 确保处理所有顶点，包括非连通分量
for i in range(n):
    if not visited[i]:
        dfs(i)

print(' '.join(map(str, result)))