def apple(n):
    dp = [0] * (n + 1)
    dp[0] = 1  

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]

    return dp[n]


while True:
    try:
        m = int(input())
        print(apple(m))
    except EOFError:
        break