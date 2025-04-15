from collections import defaultdict

def main():
    N,R=map(int,input().split())
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(N-1):
        u,v=map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # DFS to compute depth and up table
    depth = [0] * (N + 1)
    up = [[0] * 20 for _ in range(N + 1)]
    
    def dfs(u, parent):
        up[u][0] = parent
        for i in range(1, 20):
            up[u][i] = up[up[u][i-1]][i-1]
        for v in adj[u]:
            if v != parent:
                depth[v] = depth[u] + 1
                dfs(v, u)
    
    dfs(R, R)
    
    # Function to find LCA
    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        # Bring u to the same depth as v
        for i in range(19, -1, -1):
            if depth[u] - (1 << i) >= depth[v]:
                u = up[u][i]
        if u == v:
            return u
        # Now u and v are at the same depth
        for i in range(19, -1, -1):
            if up[u][i] != up[v][i]:
                u = up[u][i]
                v = up[v][i]
        return up[u][0]
    
    Q = int(input())
    for _ in range(Q):
        x,y=map(int,input().split())
        print(lca(x, y))

if __name__ == "__main__":
    main()