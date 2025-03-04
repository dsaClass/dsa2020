#二分查找，注意到M小N大，我们对M二分枚举（类似于aggressive cows）

def min_max_expense(N, M, expenses):
    # 前缀和数组
    prefix_sum = [0] * (N + 1)
    for i in range(N):
        prefix_sum[i + 1] = prefix_sum[i] + expenses[i]

    # 二分查找的范围
    left, right = max(expenses), prefix_sum[-1]

    def can_split(max_expense):
        count = 1  # 当前财政周期数
        current_sum = 0  # 当前财政周期的开销
        for i in range(1, N + 1):
            current_sum += expenses[i - 1]
            if current_sum > max_expense:
                count += 1
                current_sum = expenses[i - 1]
                if count > M:
                    return False
            if i == N:
                return True
        

    # 二分查找
    while left < right:
        mid = (left + right) // 2
        if can_split(mid):
            right = mid
        else:
            left = mid + 1

    return left

# 读取输入
N, M = map(int, input().split())
expenses = [int(input()) for _ in range(N)]

# 输出结果
print(min_max_expense(N, M, expenses))