from collections import deque
import sys
input = sys.stdin.read().splitlines()
ptr = 0
n = int(input[ptr])
ptr += 1
for _ in range(n):
    r, c = map(int, input[ptr].split())
    ptr += 1
    start = None
    end = None
    grid = []
    for i in range(r):
        line = input[ptr].strip()
        grid.append(line)
        if not start or not end:
            for j in range(c):
                if line[j] == 'S':
                    start = (i, j)
                elif line[j] == 'E':
                    end = (i, j)
        ptr += 1
        
    visited = [[False] * c for _ in range(r)]
    q = deque([(start[0], start[1])])
    visited[start[0]][start[1]] = True
    steps = 0
    found = False
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q and not found:
        for _ in range(len(q)):
            x, y = q.popleft()
            if (x, y) == end:
                found = True
                break
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and grid[nx][ny] != '#':
                    visited[nx][ny] = True
                    q.append((nx, ny))
        if found:
            print(steps)
            break
        steps += 1
    else:
        print("oop!")