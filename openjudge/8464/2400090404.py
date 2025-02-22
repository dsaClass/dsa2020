def maxProfit(prices):
    n = len(prices)
    if n == 0:
        return 0

    # 从左到右计算最大利润
    left_profit = [0] * n
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        left_profit[i] = max(left_profit[i - 1], prices[i] - min_price)

    # 从右到左计算最大利润
    right_profit = [0] * n
    max_price = prices[-1]
    for i in range(n - 2, -1, -1):
        max_price = max(max_price, prices[i])
        right_profit[i] = max(right_profit[i + 1], max_price - prices[i])

    # 找到最大的总利润
    max_total_profit = 0
    for i in range(n):
        max_total_profit = max(max_total_profit, left_profit[i] + right_profit[i])

    return max_total_profit

ans=[]
# 读取输入
T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    ans.append(maxProfit(prices))
for i in ans:
    print(i)
