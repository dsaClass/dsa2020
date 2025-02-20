def f(s):
    n = len(s)
    l = [[False]*n for i in range(n)]
    for i in range(n):
        l[i][i]=True
    for i in range(n - 1):
        l[i][i+1]=(s[i]==s[i+1])
    for length in range(3,n+1):
        for i in range(n-length+1):
            j=i+length-1
            l[i][j] =l[i+1][j-1] and (s[i]==s[j])
    dp = [0] * n
    for i in range(n):
        if l[0][i]:
            dp[i]=0
        else:
            dp[i]=i
            for j in range(i):
                if l[j+1][i]:
                    dp[i]=min(dp[i],dp[j]+1)
    return dp[n-1]
n=int(input())
for i in range(n):
    s=input()
    print(f(s))
