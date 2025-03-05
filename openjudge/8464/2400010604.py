def maxProfit(prices):
    if not prices:
        return 0
    
    n = len(prices)
    
    # 记录从左到右的最大利润
    left_profit = [0] * n
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        left_profit[i] = max(left_profit[i - 1], prices[i] - min_price)
    
    # 记录从右到左的最大利润
    right_profit = [0] * n
    max_price = prices[-1]
    for i in range(n - 2, -1, -1):
        max_price = max(max_price, prices[i])
        right_profit[i] = max(right_profit[i + 1], max_price - prices[i])
    
    # 计算最大总利润
    max_total_profit = 0
    for i in range(n):
        max_total_profit = max(max_total_profit, left_profit[i] + right_profit[i])
    
    return max_total_profit

# 读取输入
T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    print(maxProfit(prices))