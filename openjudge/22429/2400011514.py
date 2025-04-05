import sys
from collections import deque

def main():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    adj = [[] for _ in range(n+1)]
    reverse_adj = [[] for _ in range(n+1)]
    in_degree = [0] * (n + 1)
    
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        edges.append((a, b, c))
        adj[a].append((b, c))
        reverse_adj[b].append((a, c))
        in_degree[b] += 1
    
    # 拓扑排序
    order = []
    q = deque()
    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)
    
    while q:
        u = q.popleft()
        order.append(u)
        for (v, c) in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
    
    # 计算最早时间
    earliest = [0] * (n + 1)
    for u in order:
        for (v, c) in adj[u]:
            if earliest[u] + c > earliest[v]:
                earliest[v] = earliest[u] + c
    
    max_earliest = max(earliest[1:n+1])
    
    # 计算最晚时间
    latest = [max_earliest] * (n + 1)
    for v in reversed(order):
        for (u, c) in reverse_adj[v]:
            if latest[v] - c < latest[u]:
                latest[u] = latest[v] - c
    
    # 收集关键边
    critical_edges = []
    for a, b, c in edges:
        if latest[b] - c == earliest[a]:
            critical_edges.append((a, b))
    
    # 按字典序排序
    critical_edges.sort()
    
    print(max_earliest)
    for a, b in critical_edges:
        print(a, b)

if __name__ == "__main__":
    main()