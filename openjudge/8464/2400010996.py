def max_profit(prices):
    n = len(prices)
    if n == 0:
        return 0

    # 第一次买卖的最大利润
    profit1 = [0] * n
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        profit1[i] = max(profit1[i - 1], prices[i] - min_price)

    # 第二次买卖的最大利润
    profit2 = [0] * n
    max_price = prices[-1]
    for i in range(n - 2, -1, -1):
        max_price = max(max_price, prices[i])
        profit2[i] = max(profit2[i + 1], max_price - prices[i])

    # 合并结果
    max_total = 0
    for i in range(n):
        max_total = max(max_total, profit1[i] + profit2[i])

    return max_total


T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    print(max_profit(prices))