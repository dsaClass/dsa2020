n, m = map(int, input().split())

parent = list(range(n))
rank = [1] * n
has_loop = False

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

for _ in range(m):
    u, v = map(int, input().split())
    root_u = find(u)
    root_v = find(v)
    if root_u == root_v:
        has_loop = True
    else:
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_u] = root_v
            if rank[root_u] == rank[root_v]:
                rank[root_v] += 1

# 判断是否连通
connected = True
if n <= 0:
    connected = False
else:
    root = find(0)
    for i in range(1, n):
        if find(i) != root:
            connected = False
            break

print(f"connected:yes" if connected else "connected:no")
print(f"loop:yes" if has_loop else "loop:no")