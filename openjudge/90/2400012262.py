row, col = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(row)]
# 将所有点按高度从小到大排序
points = sorted([(matrix[i][j], i, j) for i in range(row) for j in range(col)])
# 初始化每个点的值为1，因为每条路径至少包含自己
dp = [[1] * col for _ in range(row)]
# 定义方向数组，用于遍历上下左右
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# 记录最长递增路径长度
ans = 1
# 从低到高进行遍历，低点不会对高点产生影响
for height, x, y in points:
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < row and 0 <= ny < col and matrix[nx][ny] < height:
            dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
    ans = max(ans, dp[x][y])

print(ans)
