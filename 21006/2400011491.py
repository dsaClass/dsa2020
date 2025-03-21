m,n =map(int,input().split())
dp = [[0 for i in range(n)] for j in range(m)]

for j in range(n):
    for i in range(m):
        if i==0 or j==0:
            dp[i][j] = 1
        elif i < j:
            dp[i][j] = dp[i][j-1]
        elif i ==j:
            dp[i][j] = dp[i][j - 1] + 1
        else:
            dp[i][j] = dp[i][j-1]+ dp[i-j-1][j] #i,j的都是0对应1，在相减时要额外减1

print(dp[m-1][n-1])