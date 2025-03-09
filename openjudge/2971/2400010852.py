k,n=map(int,input().split())
if k>=n:
    print(k-n)
else:
    dp=[0]*(2*n)
    flag=[False]*(2*n)
    curr=[k]
    flag[k]=True
    while not flag[n]:
        i=curr.pop(0)
        if  i+1<2*n and (not flag[i + 1]):
            flag[i + 1] = True
            dp[i + 1] = dp[i] + 1
            curr.append(i + 1)
        if i - 1 >= 0 and (not flag[i - 1]):
            flag[i - 1] = True
            dp[i - 1] = dp[i] + 1
            curr.append(i - 1)
        if i < n and (not flag[2 * i]):
            flag[2 * i] = True
            dp[2 * i] = dp[i] + 1
            curr.append(2 * i)
    print(dp[n])
