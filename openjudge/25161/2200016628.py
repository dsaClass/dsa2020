def min_nodes(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = 1 + dp[i - 1] + dp[i - 2]

    return dp[n]

# 输入
n = int(input())
print(min_nodes(n))