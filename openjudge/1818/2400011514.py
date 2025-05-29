import sys
from collections import deque

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        W, H = map(int, line.strip().split())
        if W == 0 and H == 0:
            break
        grid = []
        start = None
        for y in range(H):
            row = sys.stdin.readline().strip()
            grid.append(list(row))
            for x in range(W):
                if grid[y][x] == '@':
                    start = (y, x)
        visited = [[False for _ in range(W)] for _ in range(H)]
        q = deque()
        q.append(start)
        visited[start[0]][start[1]] = True
        count = 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            y, x = q.popleft()
            for dy, dx in directions:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < H and 0 <= nx < W:
                    if (grid[ny][nx] == '.' or grid[ny][nx] == '@') and not visited[ny][nx]:
                        visited[ny][nx] = True
                        count += 1
                        q.append((ny, nx))
        print(count)

if __name__ == "__main__":
    main()