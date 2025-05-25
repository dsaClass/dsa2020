from collections import deque
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
walls = [1, 2, 4, 8]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    room_size = 1
    while q:
        cx, cy = q.popleft()
        for direction in range(4):
            nx = cx + dx[direction]
            ny = cy + dy[direction]
            if not (castle[cx][cy] & walls[direction]) and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                room_size += 1
    return room_size

n = int(input())
m = int(input())
castle = []
for _ in range(n):
    castle.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]
room_count = 0
max_room_size = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            room_size = bfs(i, j)
            room_count += 1
            max_room_size = max(max_room_size, room_size)
print(room_count)
print(max_room_size)







