def flip(state, i): #在 state（当前状态）中按下第 i 个按钮
    n = len(state)
    for j in [i - 1, i, i + 1]:
        if 0 <= j < n:
            state[j] = '0' if state[j] == '1' else '1' #'0' 变 '1'，'1' 变 '0'

def solve(start_str, target_str):
    n = len(start_str)
    res = float('inf')

    for first_press in [False, True]:  # 枚举第0个是否按
        count = 0
        state = list(start_str)

        if first_press: #如果按了第0个按钮，就调用 flip()，操作次数+1。
            flip(state, 0)
            count += 1

        # 贪心地决定接下来的按钮
        #每次看前一个位置 i-1 是否已经变成目标状态,如果没有，就必须按下当前这个按钮 i，以改变它左边那个（也会改变自己和右边）。
        for i in range(1, n):
            if state[i - 1] != target_str[i - 1]:
                flip(state, i)
                count += 1

        if ''.join(state) == target_str:
            res = min(res, count)

    return res if res != float('inf') else "impossible"

# 示例输入
start = input().strip()
target = input().strip()
print(solve(start, target))
