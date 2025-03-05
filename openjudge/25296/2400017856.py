# 最短路径，bfs问题
from collections import deque
import sys
# 9 种操作影响的索引
MOVES = [
    [0, 1, 3, 4],  # 1号移动
    [0, 1, 2],     # 2号移动
    [1, 2, 4, 5],  # 3号移动
    [0, 3, 6],     # 4号移动
    [1, 3, 4, 5, 7],  # 5号移动
    [2, 5, 8],     # 6号移动
    [3, 4, 6, 7],  # 7号移动
    [6, 7, 8],     # 8号移动
    [4, 5, 7, 8]   # 9号移动
]

def rotate(state, move_idx):
    """对当前时钟状态执行 move_idx 号操作（顺时针拨动 90°)"""
    new_state = list(state)
    for index in MOVES[move_idx]:
        new_state[index] = (new_state[index] + 1) % 4  # 顺时针转 90°，取模 4
    return tuple(new_state)

def bfs(start):
    """BFS 搜索最短路径"""
    queue = deque([(start, [])])  # (当前状态, 操作序列)
    visited = set()  # 记录访问过的状态
    visited.add(start)

    while queue:
        state, path = queue.popleft()

        # 目标状态：所有时钟都指向 12 点（即 0）
        if state == (0, 0, 0, 0, 0, 0, 0, 0, 0):
            return path  # 返回操作序列
        
        # 遍历所有 9 种操作
        for move_idx in range(9):
            new_state = rotate(state, move_idx)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [move_idx + 1]))  # 记录操作

# 读取输入
input=sys.stdin.read().split()
initial_state = tuple(map(int, input))
result = bfs(initial_state)

# 按照题目要求格式输出
print(" ".join(map(str, result)))