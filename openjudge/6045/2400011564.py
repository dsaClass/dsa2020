T = int(input())
for _ in range(T):
	n, k = map(int,input().split())
	pos = list(map(int, input().split()))
	prof = list(map(int,input().split())) # 读入数据。
	dp = [0] * (n) # 动态规划问题泛化：在前i个地点可以获得的最大利润。
	dp[0] = prof[0]
	for i in range(1, n):
		if pos[i] - pos[0] <= k: # 若第i个位置与第一个地点距离小于k
			dp[i] = max([prof[_] for _ in range(0, i + 1)]) # 那么只考虑前i个地点的最大利润，由于只能开一个餐馆，就是前n个地点的餐馆利润的最大值。
		else: # 否则，可以选择在第i个地方开店或者不开店。如果不开店，那么利润等于只考虑前i-1个地点的最大利润；如果开店，那么利润等于第i-1个位置的餐馆利润加上只考虑前j个地点的餐馆的最大利润，其中j满足，第j个地点和第i个地点相隔超过k，且j最大。
			for j in range(i - 1, -1, -1): # 通过从后向前枚举来找到符合要求的j。
				if pos[i] - pos[j] > k:
					can = j
					break
			dp[i] = max(dp[i - 1], dp[can] + prof[i]) # 只考虑前i个地点所能获得的最大利润是两种选择中的较大者。
	print(dp[-1]) # 输出。
