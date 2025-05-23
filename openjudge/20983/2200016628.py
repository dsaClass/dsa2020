N = int(input())

dp = [[0] * (N+1) for _ in range(N+1)]

# 边界条件：0的划分数是1
for k in range(N+1):
    dp[0][k] = 1

for n in range(1, N+1):
    for k in range(1, N+1):
        if k > n:
            dp[n][k] = dp[n][n]  # 最大加数超过n时，等于最大加数为n的划分数
        else:
            dp[n][k] = dp[n][k-1] + dp[n-k][k]

print(dp[N][N])