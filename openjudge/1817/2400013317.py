def solve():
    rows = int(input())
    cols = int(input())
    grid = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        grid.append(row)
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    room_count = 0
    max_room_size = 0
    
    directions = [(-1, 0, 2), (1, 0, 8), (0, -1, 1), (0, 1, 4)]
    
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                current_room_size = 0
                while stack:
                    x, y = stack.pop()
                    current_room_size += 1
                    for dx, dy, wall in directions:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < rows and 0 <= ny < cols:
                            if not visited[nx][ny] and (grid[x][y] & wall) == 0:
                                visited[nx][ny] = True
                                stack.append((nx, ny))
                room_count += 1
                if current_room_size > max_room_size:
                    max_room_size = current_room_size
    
    print(room_count)
    print(max_room_size)

solve()
