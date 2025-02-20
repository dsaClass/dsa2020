result=[]
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    volumes = list(map(int, input().split()))
    # 创建dp数组，dp[i]表示容量为i的背包的取法数
    dp = [0] * (n + 1)
    dp[0] = 1  # 容量为0的背包，只有1种方式，什么也不放
    # 进行动态规划更新
    for volume in volumes:
        for i in range(volume, n + 1):#这个范围很关键
            dp[i] += dp[i - volume]
    result.append(dp[n])   # dp[n]即为恰好填满容量为n的背包的取法数
for i in result:
    print(i)


