def ways(apples, plates):
    dp = [[0 for i in range(plates + 1)] for j in range(apples + 1)]
    for plate in range(plates + 1):
        dp[0][plate] = 1
    for apple in range(apples + 1):
        dp[apple][0] = 0
    for i in range(1, apples + 1):
        for j in range(1, plates + 1):
            if i >= j:
                dp[i][j] = dp[i][j-1] + dp[i-j][j]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[apples][plates]
m, n = map(int, input().split())
print(ways(m, n))