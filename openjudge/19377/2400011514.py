n, m = map(int, input().split())

# 初始化可达性矩阵，牛的编号从1到n
reachable = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    reachable[a][b] = True

# Floyd-Warshall算法计算传递闭包
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if reachable[i][k] and reachable[k][j]:
                if not reachable[i][j]:
                    reachable[i][j] = True

count = 0
for i in range(1, n + 1):
    stronger = 0
    weaker = 0
    for j in range(1, n + 1):
        if i == j:
            continue
        if reachable[j][i]:
            stronger += 1
        if reachable[i][j]:
            weaker += 1
    if stronger + weaker == n - 1:
        count += 1

print(count)