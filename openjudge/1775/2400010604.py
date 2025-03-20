def max_value(T, M, herbs):
    dp = [0] * (T + 1)
    
    for time, value in herbs:
        for j in range(T, time - 1, -1):
            dp[j] = max(dp[j], dp[j - time] + value)
    
    return dp[T]

T, M = map(int, input().split())
herbs = [tuple(map(int, input().split())) for _ in range(M)]

print(max_value(T, M, herbs))