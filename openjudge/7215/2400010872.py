n_max = 50
dp = [[0] * (n_max + 1) for _ in range(n_max + 1)]

# 处理j=0的情况
for i in range(n_max + 1):
    dp[i][0] = 1 if i == 0 else 0

# 填充其他情况
for i in range(n_max + 1):
    for j in range(1, n_max + 1):
        if i == 0:
            dp[i][j] = 1
        else:
            if j > i:
                dp[i][j] = dp[i][i]
            else:
                a = dp[i - j][j]
                b = dp[i][j - 1]
                dp[i][j] = a + b

import sys
for line in sys.stdin:
    N = int(line.strip())
    print(dp[N][N])
