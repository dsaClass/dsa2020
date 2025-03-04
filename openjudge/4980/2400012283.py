from collections import deque


def shorttime(map1, rn, rm, an, am):
    n = len(map1)
    m = len(map1[0])
    dp = [[float('inf')] * m for _ in range(n)]
    dp[rn][rm] = 0
    queue = deque([(rn, rm)])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        i, j = queue.popleft()
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < n and 0 <= nj < m and map1[ni][nj]!= '#':
                cost = 1 if map1[ni][nj] == '@' else 2
                if dp[ni][nj] > dp[i][j] + cost:
                    dp[ni][nj] = dp[i][j] + cost
                    queue.append((ni, nj))
    return dp[an][am]


u = int(input())
for _ in range(u):
    n, m = map(int, input().split())
    map1 = []
    rn = 0
    rm = 0
    an = 0
    am = 0
    for i in range(n):
        li1 = list(input())
        map1.append(li1)
        for j in range(m):
            if li1[j] == 'r':
                rn = i
                rm = j
            elif li1[j] == 'a':
                an = i
                am = j
    result = shorttime(map1, rn, rm, an, am)
    if result == float('inf'):
        print('Impossible')
    else:
        print(result-1)