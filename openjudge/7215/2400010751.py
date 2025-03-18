def integer_partitions(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for j in range(n + 1):
        dp[0][j] = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i < j:
                dp[i][j] = dp[i][i]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - j][j]

    return dp[n][n]
while True:
    try:
        n = int(input())
        if 0 < n <= 50:
            print(integer_partitions(n))
    except EOFError:
        break
