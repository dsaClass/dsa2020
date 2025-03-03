from collections import deque

def min_time_to_reach_sasuke(M, N, T, grid):
    """
    计算鸣人追上佐助的最短时间。
    
    参数:
    M (int): 网格的行数
    N (int): 网格的列数
    T (int): 鸣人初始的查克拉值
    grid (List[List[str]]): 网格地图，包含 '@' (鸣人), '+' (佐助), '*' (空地), '#' (障碍)
    
    返回:
    int: 到达佐助的最短时间，如果无法到达则返回 -1
    """
    # 找到鸣人的起始位置
    for i in range(M):
        for j in range(N):
            if grid[i][j] == '@':
                start_x, start_y = i, j
                break

    # 定义四个方向的移动：上、下、左、右
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS队列，存储状态：(x, y, t, time)
    # x, y: 当前位置坐标
    # t: 剩余查克拉
    # time: 已用时间
    queue = deque([(start_x, start_y, T, 0)])

    # 访问标记，防止重复访问相同状态 (x, y, t)
    visited = [[[False] * (T + 1) for _ in range(N)] for _ in range(M)]
    visited[start_x][start_y][T] = True

    while queue:
        x, y, t, time = queue.popleft()

        # 如果当前位置是佐助的位置 '+'
        if grid[x][y] == '+':
            return time

        # 尝试向四个方向移动
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 检查新位置是否在网格范围内
            if 0 <= nx < M and 0 <= ny < N:
                if grid[nx][ny] in ('*', '+'):
                    # 如果下一个位置是空地 '*' 或佐助 '+'
                    if not visited[nx][ny][t]:
                        visited[nx][ny][t] = True
                        queue.append((nx, ny, t, time + 1))
                elif grid[nx][ny] == '#':
                    # 如果下一个位置是障碍 '#'
                    if t > 0 and not visited[nx][ny][t - 1]:
                        visited[nx][ny][t - 1] = True
                        queue.append((nx, ny, t - 1, time + 1))

    # 如果无法到达佐助
    return -1

# 示例用法
# 样例输入1

 # 读取第一行：M, N, T
M, N, T = map(int, input().split())
    
    # 读取 M 行地图
grid = [list(input()) for _ in range(M)]
    
    # 计算并输出结果
result = min_time_to_reach_sasuke(M, N, T, grid)
print(result)