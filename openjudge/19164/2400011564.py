t, m = map(int, input().split())
incomelist = []
for _ in range(t):
    incomelist.append(list(map(int, input().split()))) # 读入两地营业额数据
dp = [[0] * (t) for _ in range(2)] # 准备动态规划数据表格
dp[0][0] = incomelist[0][0] # 第一个月可以选择在任意一地开始。
dp[1][0] = incomelist[0][1]
for col in range(1, t): # 问题泛化：前n个月在两地分别最多可以获得多少净收益？
    dp[0][col] = max(dp[0][col - 1], dp[1][col - 1] - m) + incomelist[col][0]
    dp[1][col] = max(dp[1][col - 1], dp[0][col - 1] - m) + incomelist[col][1]
# 关系：本地第n个月最大营业额 = 最大值（本地第n-1个月最大营业额，异地第n-1个月最大营业额 - 交通费） + 本地第n个月的营业额。
print(max(dp[0][-1], dp[1][-1]))
