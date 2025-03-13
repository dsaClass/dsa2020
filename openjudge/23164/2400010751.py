from collections import deque


def bfs(matrix, visited, r, c, x, y):
    area = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        area += 1
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and matrix[nx][ny] == '.':
                visited[nx][ny] = True
                queue.append((nx, ny))

    return area


def count_rooms(r, c, matrix):
    visited = [[False] * c for _ in range(r)]
    room_count = 0
    max_area = 0

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == '.' and not visited[i][j]:
                room_count += 1
                area = bfs(matrix, visited, r, c, i, j)
                max_area = max(max_area, area)

    return room_count, max_area


r, c = map(int, input().split())
matrix = [list(input().strip()) for _ in range(r)]

room_count, max_area = count_rooms(r, c, matrix)

print(room_count)
print(max_area)
