def max_profit(prices):
    n = len(prices)
    if n < 2:
        return 0    #不足两天没有买卖的机会
    profit1 = [0] * n  #第一次买卖的最大利润
    profit2 = [0] * n  # 第二次买卖的最大利润
    min_price = prices[0]  #计算 profit1：表示到第 i 天，最多进行一次买卖能获得的最大利润
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        profit1[i] = max(profit1[i - 1], prices[i] - min_price)
    max_price = prices[n - 1]   #计算 profit2：表示从第 i 天到最后，最多进行一次买卖能获得的最大利润
    for i in range(n-2, -1, -1):
        max_price = max(max_price, prices[i])
        profit2[i] = max(profit2[i+1], max_price - prices[i])
    # 找到两次买卖的最大利润
    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, profit1[i] + profit2[i])
    return max_profit
t = int(input())
for _ in range(t):
    N = int(input())
    prices = list(map(int, input().split()))
    print(max_profit(prices))
