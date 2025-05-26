n = int(input())
left = n - 4  # 减去 '+' 和 '=' 两个符号火柴数

match_count = {'0':6, '1':2, '2':5, '3':5, '4':4,
               '5':5, '6':6, '7':3, '8':7, '9':6}

MAX = 1000  # 限制搜索范围（可根据实际情况调节）

# 预处理所有数字的火柴数
sticks = [0] * (MAX + 1)

def calc_sticks(num):
    return sum(match_count[d] for d in str(num))

for i in range(MAX + 1):
    sticks[i] = calc_sticks(i)

def is_valid(num):
    s = str(num)
    return s == "0" or s[0] != '0'

count = 0
for A in range(MAX + 1):
    if sticks[A] > left:
        continue
    for B in range(MAX + 1):
        total = sticks[A] + sticks[B]
        if total > left:
            continue
        C = A + B
        if C > MAX:
            continue
        total += sticks[C]
        if total == left and is_valid(A) and is_valid(B) and is_valid(C):
            count += 1

print(count)























