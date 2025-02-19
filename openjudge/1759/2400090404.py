n = int(input())
nums = list(map(int,input().split()))
#solution1:直接使用递归+记忆化搜索
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
print(LIS(nums))
#solution2：递推
def LIS_d(nums):
    n = len(nums)
    f = [0]*n
    for i,x in enumerate(nums):
        res = 0
        for j in range(i):
            if nums[j] < x:
                res = max(f[j],res)
        f[i] = res + 1
    return f[n-1]
print(LIS_d(nums))

#solution3 联系最长公共子序列
#求最长上升子序列可以转换为求该数组与自然数组的最长公共子序列
#因此 求nums的最大上升子序列也可以转换为 求它和numbers【1，2，3，4，5，6....】的最大公共子序列
#先给出最长公共子序列（LCS）的代码：
#递归+记忆化搜索：
def LCS(s,t):
    n = len(s)
    m = len(t)
    def dfs(i,j):
        if i < 0 or j < 0:
            return 0
        if s[i] == t[j]:
            return dfs(i-1,j-1)+1
        return max(dfs(i-1,j),dfs(i,j-1))
    return dfs(n-1,m-1)
#改递推：
def LCS_d(s,t):
    n = len(s)
    m = len(t)
    f = [[0 for i in range(m+1)]for j in range(n+1)]
    for i,x in enumerate(s):
        for j,y in enumerate(t):
            f[i+1][j+1] = f[i][j] +1 if x ==y else max(f[i+1][j],f[i][j+1])
    return f[n][m]


mx = max(nums)
lst = [i for i in range(mx+1)]
print(LCS_d(nums,lst))

#solution4:
#贪心法 交换状态函数的状态与状态值结合二分查找
#这个算法的时间复杂度可以达到nlogn
import bisect
def LIS_nlogn(nums):
    g = []
    for i, x in enumerate(nums):
        j = bisect.bisect_left(g,x)
        if j == len(g):
            g.append(x)
        else:
            g[j] = x
    return len(g)
print(LIS_nlogn(nums))

