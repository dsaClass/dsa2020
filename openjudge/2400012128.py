n,m=[int(i) for i in input().strip().split()]
lst0=[]
for i in range(n):
    lst0.append(int(input().strip()))
# 二分查找
left = max(lst0)
right = sum(lst0)
# 检查函数，判断是否可以将 N 天划分为不超过 M 个 fajo 月，使得每个 fajo 月的开销不超过 limit
def check(limit):
    months = 1
    current_cost = 0
    for cost in lst0:
        if current_cost + cost > limit:
            months += 1
            current_cost = cost
        else:
            current_cost += cost
    return months <= m

# 二分查找
while left < right:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid + 1

# 输出结果
print(left)