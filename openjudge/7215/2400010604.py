def count_partitions(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # 初始化
    for j in range(n + 1):
        dp[0][j] = 1  # 0的划分只有一种方式

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j > i:
                dp[i][j] = dp[i][i]
            else:
                dp[i][j] = dp[i - j][j] + dp[i][j - 1]

    return dp[n][n]

#输入
import sys

for item in sys.stdin:
    print(count_partitions(int(item.strip())))