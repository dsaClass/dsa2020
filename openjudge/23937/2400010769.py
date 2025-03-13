def can_escape_maze():

    N = int(input())
    maze = []


    for _ in range(N):
        maze.append(list(map(int, input().split())))


    def dfs(x, y):
        # 如果到达出口，返回True
        if x == N - 1 and y == N - 1:
            return True

        # 尝试向右走
        if y + 1 < N and maze[x][y + 1] == 0:
            maze[x][y + 1] = 1  # 标记为已访问
            if dfs(x, y + 1):  # 递归调用
                return True
            maze[x][y + 1] = 0  # 回溯，恢复状态

        # 尝试向下走
        if x + 1 < N and maze[x + 1][y] == 0:
            maze[x + 1][y] = 1  # 标记为已访问
            if dfs(x + 1, y):  # 递归调用
                return True
            maze[x + 1][y] = 0  # 回溯，恢复状态

        return False  # 如果两个方向都无法到达出口，返回False


    if dfs(0, 0):
        return "Yes"
    else:
        return "No"


print(can_escape_maze())