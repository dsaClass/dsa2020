def count(nums) :
    dp=[0]*7  
    dp[0]=1  

    for num in nums :
        new_dp=dp[:]  
        for r in range(7):
            new_r=(r+num)%7
            new_dp[new_r]+=dp[r]  
        dp=new_dp  
    return dp[0]  

t=int(input())
for _ in range(t) :
    data=list(map(int,input().split()))
    print(count(data[1:]))