def max_profit(prices,n):
    dp=[[0]*5 for _ in range(n)]
    dp[0][1] = -prices[0]
    dp[0][3] = -prices[0]
    for i in range(1,n):
        dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])#第一次持有
        dp[i][2] = max(dp[i-1][2],dp[i-1][1]+prices[i])#第一次卖出
        dp[i][3] = max(dp[i-1][3],dp[i-1][2]-prices[i])#第二次持有
        dp[i][4] = max(dp[i-1][4],dp[i-1][3]+prices[i])#第二次卖出
    return dp[n-1][4]
T=int(input())
for _ in range(T):
    n = int(input())
    prices = list(map(int,input().split()))
    print(max_profit(prices,n))

