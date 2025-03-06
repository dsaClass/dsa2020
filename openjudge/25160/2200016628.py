from collections import deque

def bfs(maze, n, m):
    # 初始化队列和访问记录
    queue = deque([(0, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    prev = [[None] * m for _ in range(n)]
    
    # 方向向量
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        x, y = queue.popleft()
        if (x, y) == (n-1, m-1):
            break
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == '.' and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                prev[nx][ny] = (x, y)
    
    # 回溯路径
    if prev[n-1][m-1] is not None:
        path = []
        x, y = n-1, m-1
        while (x, y) != (0, 0):
            path.append((x, y))
            x, y = prev[x][y]
        path.append((0, 0))
        path.reverse()
        return path
    else:
        return []

def main():
    n, m = map(int, input().split())
    maze = [input() for _ in range(n)]
    path = bfs(maze, n, m)
    if path:
        print(''.join(f'({x},{y})' for x, y in path))
    else:
        print(0)

if __name__ == "__main__":
    main()