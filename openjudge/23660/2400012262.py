t = int(input())
for _ in range(t):
    data = list(map(int, input().split()))
    n = data[0]
    nums = data[1:]
    dp = [0] * 7
    dp[0] = 1  # 初始状态，空集
    for num in nums:
        mod = num % 7
        new_dp = [0] * 7
        for k in range(7):
            new_dp[k] = dp[k] + dp[(k - mod) % 7]
        dp = new_dp
    print(dp[0])
