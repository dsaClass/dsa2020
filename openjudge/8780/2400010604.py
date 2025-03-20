def max_intercept_missiles(N, heights):
    dp = [1] * N
    for i in range(1, N):
        for j in range(i):
            if heights[j] >= heights[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# 输入处理
N = int(input())
heights = list(map(int, input().split()))

# 输出结果
print(max_intercept_missiles(N, heights))