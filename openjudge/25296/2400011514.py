import itertools

# 读取输入
s = []
for _ in range(3):
    s += list(map(int, input().split()))

required = [(4 - s[i]) % 4 for i in range(9)]

min_total = float('inf')
best_sequence = None

for k in itertools.product(range(4), repeat=9):
    # 检查所有条件是否满足
    # 时钟A的条件
    a = (k[0] + k[1] + k[3]) % 4
    if a != required[0]:
        continue
    # 时钟B的条件
    b = (k[0] + k[1] + k[2] + k[4]) % 4
    if b != required[1]:
        continue
    # 时钟C的条件
    c = (k[1] + k[2] + k[5]) % 4
    if c != required[2]:
        continue
    # 时钟D的条件
    d = (k[0] + k[3] + k[4] + k[6]) % 4
    if d != required[3]:
        continue
    # 时钟E的条件
    e = (k[0] + k[2] + k[4] + k[6] + k[8]) % 4
    if e != required[4]:
        continue
    # 时钟F的条件
    f = (k[2] + k[4] + k[5] + k[8]) % 4
    if f != required[5]:
        continue
    # 时钟G的条件
    g = (k[3] + k[6] + k[7]) % 4
    if g != required[6]:
        continue
    # 时钟H的条件
    h = (k[4] + k[6] + k[7] + k[8]) % 4
    if h != required[7]:
        continue
    # 时钟I的条件
    i_ = (k[5] + k[7] + k[8]) % 4
    if i_ != required[8]:
        continue

    total = sum(k)
    # 生成移动序列
    sequence = []
    for move_idx in range(9):
        move = move_idx + 1
        count = k[move_idx]
        sequence.extend([move] * count)
    # 更新最优解
    if total < min_total:
        min_total = total
        best_sequence = sequence.copy()
    elif total == min_total:
        # 比较字典序
        if tuple(sequence) < tuple(best_sequence):
            best_sequence = sequence.copy()

print(' '.join(map(str, best_sequence)))