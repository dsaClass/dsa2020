def f(m,n):
    dp=[[0 for  _ in range(n+1)] for _ in range(m+1)]
    for i in range(1,n+1):
        dp[0][i]=1
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j]=dp[i][j-1]
            if i>=j:
                dp[i][j]+=dp[i-j][j]
    return dp[m][n]
t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    print(f(m,n))
