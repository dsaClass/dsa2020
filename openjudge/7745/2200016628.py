nums=list(map(int,input().split()))
nums.sort()
ans=nums
for i in range(len(nums)):
    num=nums[i]
    if  num %2 ==1:
        del ans[i]
        ans.insert(0,num)
print(" ".join(map(str,ans)))