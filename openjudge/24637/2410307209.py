n=int(input())
values=list(map(int, input().split()))
dp=[[0,0] for i in range(n+2)]

for i in range(n,0,-1):
    left,right=2*i,2*i+1
    #防止子树下面没有了
    left_0=dp[left][0] if left <= n else 0
    left_1=dp[left][1] if left <= n else 0
    right_0=dp[right][0] if right <= n else 0
    right_1=dp[right][1] if right <= n else 0

    max_son=max(left_0,left_1)+max(right_0,right_1)#以i为根的子树最大的value
    dp[i][0]=max_son#如果不选i，那么左右子树都可以选
    dp[i][1]=values[i-1]+left_0+right_0#如果选i，那么左右子树都不能选

print(max(dp[1][0],dp[1][1]))