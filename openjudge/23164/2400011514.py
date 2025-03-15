def dfs(matrix, visited, r, c, x, y):
    # 定义四个方向的移动：上下左右
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [(x, y)]
    visited[x][y] = True
    area = 1  # 当前房间的面积，起始位置已经是空地

    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and matrix[nx][ny] == '.':
                visited[nx][ny] = True
                stack.append((nx, ny))
                area += 1

    return area

def count_rooms_and_max_area(r, c, matrix):
    visited = [[False] * c for _ in range(r)]
    room_count = 0
    max_area = 0

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == '.' and not visited[i][j]:
                room_count += 1
                area = dfs(matrix, visited, r, c, i, j)
                max_area = max(max_area, area)

    return room_count, max_area

# 输入处理
r, c = map(int, input().split())
matrix = [input().strip() for _ in range(r)]

# 计算房间数和最大房间面积
room_count, max_area = count_rooms_and_max_area(r, c, matrix)

# 输出结果
print(room_count)
print(max_area)
