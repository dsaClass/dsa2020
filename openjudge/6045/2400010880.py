T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    m = list(map(int, input().split()))
    p = list(map(int, input().split()))
    dp = p.copy()
    for i in range(n):
        max_prev = 0
        for j in range(i):
            if m[i] - m[j] > k:
                if dp[j] > max_prev:
                    max_prev = dp[j]
        dp[i] += max_prev
    print(max(dp))