def shao(s):
    n=len(s)
    dp=[[0]*n for _ in range(n)] #dp[i][j]表示i-j变成回文
    for i in range(n):
        dp[i][i]=0
    for les in range(2,n+1):
        for qi in range(n-les+1):#start
            mo=qi+les-1#end
            if s[qi]==s[mo]:
                dp[qi][mo]=dp[qi+1][mo-1]
            else:
                dp[qi][mo]=min(dp[qi+1][mo],dp[qi][mo-1],dp[qi+1][mo-1])+1
    return dp[0][n-1]
s=input()
print(shao(s))