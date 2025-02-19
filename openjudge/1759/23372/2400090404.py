def Bag(nums,amount):
    k = len(nums)
    f = [[-1 for i in range(k+1)] for j in range(amount+1)]
    def dfs(i,c):
        if f[c][i] != -1:
            return f[c][i]
        if c == 0:
            return 1
        if i == 0 and c != 0:
            return 0
        if c < nums[i-1]:
            return dfs(i-1,c)
        f[c][i] = dfs(i-1,c)+dfs(i,c-nums[i-1])
        return f[c][i]
    return dfs(k,amount)

def Bag_d(nums,amount):
    k = len(nums)
    f =  [[0 for i in range(amount +1)] for j in range(k+1)]
    for j in range(k+1):
        f[j][0] = 1#初始条件

    for i ,x in enumerate(nums):
        for c in range(amount+1):
            if c < x:
                f[i+1][c] = f[i][c]
            else:
                f[i+1][c] = f[i][c] + f[i+1][c-x]
    return f[k][amount]
ans = []
while True:
    n,m = map(int,input().split())
    if m == 0 or n == 0:
        break
    nums = list(map(int,input().split()))
    ans.append(Bag_d(nums,n))
for i in ans:
    print(i)