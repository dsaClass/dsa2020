n = int(input())

nums = []
for j in range(n):
    nums.append(int(input()))

dp = [0 for _ in range(n)]

for i in range(-1,-n,-1):
    if nums[i-1] > nums[i]:
        k = i
        while k < 0 and nums[i-1] > nums[k]:
            dp[i-1] += dp[k]+1
            k += dp[k] + 1
        
    else:
        dp[i-1] = 0

print(sum(dp))

