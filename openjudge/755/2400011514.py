from collections import deque

# 定义棋盘的初始状态
def read_input():
    board = []
    for _ in range(4):
        row = input().strip()
        board.append(list(row))
    return board

# 将棋盘状态转换为一个整数表示，方便存储和比较
def board_to_int(board):
    res = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] == 'b':
                res |= 1 << (i * 4 + j)
    return res

# 翻转棋子
def flip(board, x, y):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            board[nx][ny] = 'w' if board[nx][ny] == 'b' else 'b'

# BFS搜索最小步数
def bfs(start):
    target1 = 0  # 全白
    target2 = 0xFFFF  # 全黑
    if start == target1 or start == target2:
        return 0

    visited = set()
    queue = deque()
    queue.append((start, 0))
    visited.add(start)

    while queue:
        current, steps = queue.popleft()
        for i in range(4):
            for j in range(4):
                # 复制当前状态
                new_board = [[None for _ in range(4)] for _ in range(4)]
                for x in range(4):
                    for y in range(4):
                        new_board[x][y] = 'b' if (current >> (x * 4 + y)) & 1 else 'w'
                # 翻转棋子
                flip(new_board, i, j)
                # 转换为整数表示
                new_state = board_to_int(new_board)
                if new_state == target1 or new_state == target2:
                    return steps + 1
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))
    return "Impossible"

# 主函数
def main():
    board = read_input()
    start = board_to_int(board)
    result = bfs(start)
    print(result)

if __name__ == "__main__":
    main()