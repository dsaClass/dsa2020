from collections import deque
n, m = map(int, input().split())
maze = [input() for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
prev = [[None for _ in range(m)] for _ in range(n)]
q = deque()
start = (0, 0)
end = (n - 1, m - 1)
q.append(start)
found = False
while q:
    x, y = q.popleft()
    if (x, y) == end:
        found = True
        break
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if maze[nx][ny] == '.' and prev[nx][ny] is None:
                prev[nx][ny] = (x, y)
                q.append((nx, ny))
if not found:
    print(0)
else:
    path = []
    current = end
    while True:
        path.append(current)
        current = prev[current[0]][current[1]]
        if current==(0,0):
            break
    path.append((0,0))
    path.reverse()
    output = ''.join(f'({x},{y})' for x, y in path)
    print(output)
