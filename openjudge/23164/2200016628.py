from collections import deque

# 读取输入
r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]

room_count = 0
max_area = 0

# 遍历每个点
for i in range(1,r-1):
    for j in range(1,c-1):
        if grid[i][j] == '.' and not visited[i][j]:
            # 开始BFS
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            area = 1

            while queue:
                x, y = queue.popleft()
                # 四个方向
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx = x + dx
                    ny = y + dy
                    # 检查是否在合法范围内，并且是否是未访问的'.'
                    if 0 <= nx < r and 0 <= ny < c:
                        if grid[nx][ny] == '.' and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            area += 1
            # 更新房间数和最大面积
            room_count += 1
            if area > max_area:
                max_area = area

print(room_count)
print(max_area)