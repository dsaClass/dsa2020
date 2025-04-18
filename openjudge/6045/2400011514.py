T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    m = list(map(int, input().split()))
    p = list(map(int, input().split()))
    if n == 0:
        print(0)
        continue
    dp = [0] * n
    dp[0] = p[0]
    for i in range(1, n):
        current_max = p[i]  # 初始化为只选当前餐馆的情况
        for j in range(i):
            if m[i] - m[j] > k:
                if dp[j] + p[i] > current_max:
                    current_max = dp[j] + p[i]
        dp[i] = max(dp[i-1], current_max)
    print(dp[-1])