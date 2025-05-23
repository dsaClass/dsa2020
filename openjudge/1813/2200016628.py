import copy

# 输入
start = [input().split() for _ in range(5)]


# 翻转函数
def flip(grid, r, c):
    for dr, dc in [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 5 and 0 <= nc < 6:
            grid[nr][nc] = '0' if grid[nr][nc] == '1' else '1'

# 解决函数
def solve(start):
    for mask in range(2**6):  # 枚举第一行的按法
        state = copy.deepcopy(start)
        press = [['0'] * 6 for _ in range(5)]

        # 按第一行
        for j in range(6):
            if (mask >> j) & 1: #第一行j列按了
                press[0][j] = '1'
                flip(state, 0, j)

        # 从第二行开始逐行决定按法
        for i in range(1, 5):
            for j in range(6):
                if state[i - 1][j] == '1':  # 如果上一行灯亮，必须按
                    press[i][j] = '1'
                    flip(state, i, j)

        # 检查最后一行是否全灭
        if all(state[4][j] == '0' for j in range(6)):
            return press

    return "impossible"

# 输出
ans = solve(start)
if ans == "impossible":
    print(ans)
else:
    for row in ans:
        print(" ".join(row))