def LIS(nums):
    n = len(nums)
    mem = [-1]*n
    def dfs(i):#以i结尾的子序列长度
        res = 0
        if mem[i] != -1:
            return mem[i]
        for j in range(i):
            if nums[j] < nums[i]:
               res = max(res, dfs(j))
        mem[i] =  res + 1
        return mem[i]

    return max(dfs(i) for i in range(n))
n = int(input())
nums = list(map(int,input().split()))
print(LIS(nums))
