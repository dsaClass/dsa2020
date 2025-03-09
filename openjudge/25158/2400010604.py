from collections import deque

def can_reach_exit(n, m, maze):
    # 定义四个方向的移动
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 创建队列用于BFS
    queue = deque()
    queue.append((0, 0))  # 从入口开始
    
    # 创建一个访问标记数组
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()
        
        # 如果到达出口，返回1
        if x == n - 1 and y == m - 1:
            return 1
        
        # 尝试向四个方向移动
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 检查新位置是否在迷宫内，且是空地，且未被访问过
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    # 如果队列为空且没有到达出口，返回0
    return 0

# 读取输入
n, m = map(int, input().split())
maze = [input().strip() for _ in range(n)]

# 判断是否可以从入口走到出口
print(can_reach_exit(n, m, maze))