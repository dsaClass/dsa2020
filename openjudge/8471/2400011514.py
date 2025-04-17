def min_cut(s):
    n = len(s)
    if n == 0:
        return 0
    # 预处理回文子串
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if i == j:
                is_pal[i][j] = True
            elif s[i] == s[j]:
                if j == i + 1:
                    is_pal[i][j] = True
                else:
                    is_pal[i][j] = is_pal[i+1][j-1]
            else:
                is_pal[i][j] = False
    # 动态规划
    dp = [0] * (n + 1)
    dp[0] = -1  # 初始条件，表示空串不需要切割
    for i in range(1, n + 1):
        dp[i] = i - 1  # 初始化为最大可能切割次数
        for j in range(i):
            if is_pal[j][i-1]:
                if dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1
    return dp[n]

t = int(input())
for _ in range(t):
    s = input().strip()
    print(min_cut(s))