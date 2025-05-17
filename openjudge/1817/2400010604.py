def solve():
    import sys
    sys.setrecursionlimit(1000000)
    
    m = int(input())
    n = int(input())
    grid = []
    for _ in range(m):
        row = list(map(int, input().split()))
        grid.append(row)
    
    visited = [[False for _ in range(n)] for _ in range(m)]
    directions = [ (0, -1), (-1, 0), (0, 1), (1, 0) ]  # West, North, East, South
    wall = [1, 2, 4, 8]  # Corresponding to West, North, East, South
    
    def dfs(x, y):
        stack = [(x, y)]
        visited[x][y] = True
        size = 0
        while stack:
            cx, cy = stack.pop()
            size += 1
            for i in range(4):
                dx, dy = directions[i]
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and not (grid[cx][cy] & wall[i]):
                    visited[nx][ny] = True
                    stack.append((nx, ny))
        return size
    
    room_count = 0
    max_room_size = 0
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                room_size = dfs(i, j)
                room_count += 1
                if room_size > max_room_size:
                    max_room_size = room_size
    
    print(room_count)
    print(max_room_size)

solve()