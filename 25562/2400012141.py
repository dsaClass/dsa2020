def catalan_number(n):
    dp = [0] * (n + 1)    #dp[i] 表示第 i 个卡特兰数
    dp[0] = 1
    for i in range(1, n + 1):    #递推计算卡特兰数
        dp[i] = 0
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
    return dp[n]
n = int(input())
print(catalan_number(n))










