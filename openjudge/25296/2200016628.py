import sys

# 定义每个移动操作影响的时钟
moves = [
    [0, 1, 3, 4],  # 移动1: ABDE
    [0, 1, 2],  # 移动2: ABC
    [1, 2, 4, 5],  # 移动3: BCEF
    [0, 3, 6],  # 移动4: ADG
    [1, 3, 4, 5, 7],  # 移动5: BDEFH
    [2, 5, 8],  # 移动6: CFI
    [3, 4, 6, 7],  # 移动7: DEGH
    [6, 7, 8],  # 移动8: GHI
    [4, 5, 7, 8]  # 移动9: EFHI
]



# 读取输入
clocks = list(map(int, sys.stdin.read().split()))

min_moves = None
min_count = float('inf')

# 遍历所有可能的移动组合
for mask in range(4 ** 9): #遍历每一种可能
    # 把 mask 拆成 9 个 0~3 的数，放到 move_counts 里
    current_mask = mask
    # 记录每种可能下，每个操作的次数
    move_counts = [0] * 9
    for i in range(9):
        move_counts[i] = current_mask % 4 #取余
        current_mask //= 4 #整除
    # 例如 mask = 123  => move_counts = [3, 2, 1, 1, 0, 0, 0, 0, 0] 即操作1执行3次、操作2执行2次……

    # 计算当前组合下的最终时钟状态
    final_clocks = clocks.copy()
    for move_idx in range(9):
        count = move_counts[move_idx] #看每个操作进行了几次
        if count == 0:
            continue
        for clock_idx in moves[move_idx]: #对每个操作下的时钟进行拨动
            final_clocks[clock_idx] = (final_clocks[clock_idx] + count) % 4

    # 检查是否所有时钟都指向12点
    if all(c == 0 for c in final_clocks):
        # 计算总操作次数
        total = sum(move_counts)
        # 选择移动次数最少的组合
        if total < min_count:
            min_count = total
            min_moves = move_counts.copy()
        # 如果移动次数相同，选择字典序更小的组合
        elif total == min_count:
            # 比较字典序 列表之间的比较是按字典序进行的
            if move_counts < min_moves:
                min_moves = move_counts.copy()

# 生成结果
result = []
for move_idx in range(9):
    count = min_moves[move_idx] #每个操作的次数
    for _ in range(count): #要是这个操作的次数count>1 要连续输出这个操作
        result.append(move_idx + 1)  # 移动编号从1开始

# 输出结果
print(' '.join(map(str, result)))