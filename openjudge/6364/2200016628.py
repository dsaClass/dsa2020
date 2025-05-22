n, k = map(int, input().split())

cows = []  # 存储 (编号, A, B)
for i in range(1, n + 1):
    a, b = map(int, input().split())
    cows.append((i, a, b))

# 按照 A 值排序，选出前 K 头牛（第一轮晋级者）
cows.sort(key=lambda x: -x[1])
top_k = cows[:k]

# 在 top_k 中找 B 值最大的牛
winner = max(top_k, key=lambda x: x[2])

print(winner[0])  # 输出编号