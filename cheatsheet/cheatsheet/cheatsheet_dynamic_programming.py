'''
问题引入：爬楼梯问题
'''
#解法一：回溯穷举可能性
#从地面出发，每轮上1或2阶，每当到达楼梯顶部，方案数+1；超过楼梯顶则剪枝

'''
简单的整数划分问题
'''
max_n = 50
dp = [[0] * (max_n + 1) for _ in range(max_n + 1)]

# 初始化i=0的情况
for j in range(max_n + 1):
    dp[0][j] = 1

for i in range(1, max_n + 1):
    dp[i][0] = 0  # 当无法选取任何正整数时，无法组成i>0的情况
    for j in range(1, i + 1):
        dp[i][j] = dp[i][j - 1] + dp[i - j][j]
    # 对于j超过i的情况，直接取j=i的值
    for j in range(i + 1, max_n + 1):
        dp[i][j] = dp[i][i]

import sys
for line in sys.stdin:
    n = int(line.strip())
    print(dp[n][n])

'''
8780 最长单调递减子序列(LDS)
'''
#找到一段数组中长度最长的单调不增序列
#经典问题：求最长非递增子序列长度
#n=int(input())
#height=tuple(map(int,input().split()))
def intercept_missiles(height,n):
    dp=[1]*(n+1)   #dp[i]表示第i个位置索引的元素是当前子序列中可能得最小子序列
    for i in range(n):
        for j in range(i):   #时间复杂度为O(N^2)
            if height[i]<=height[j]:   #只有后者高度小于前者才需要判断
                dp[i]=max(dp[j]+1,dp[i])
                #此时，前面第j个位置dp[j]已能反映出它之前可拦截的导弹数
    return max(dp[i] for i in range(n))

#print(intercept_missiles(height))

'''
20650 最长的公共子序列(LCS)
'''
#思路：在序列前加一个空格，来确定边界条件
#定义一个二维数组lcs(i,j)，表示字符串a中第i个字符和字符串b中第j个字符的LCS长度
#if a[i]=b[j]: lcs[i][j]=lcs[i-1][j-1]+1
#else: lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1] 两个删去任意一个都可以，要比较两种情况
def lps(str1,str2):
    n=len(str1)
    m=len(str2)
    if n==0:
        return 0
    else:
        dp=[[0]*(n+1) for _ in range(m+1)]
        #dp[i][j]表示str1[:i]与str[:j]的最长共子序列
        for i in range(1,n+1):
            for j in range(1,m+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[n][m]


'''
0-1背包问题
问题描述：给定一组物品，每个物品有重量weight[i]与价值value[i]，以及背包最大容量w
要求选择物品放入背包使总重量不超过w，且总价值最大
'''
#dp[i][w]表示前i个物品中，选择重量不超过w的物品时能获得的最大价值
#状态转移方程：dp[i][w]=max(dp[i-1][w],dp[i-1][w-weight[i-1]]+value[i-1])
#初始化条件：dp[0][w]=0,dp[i][0]=0

def knapsack(weights,values,w):
    n=len(weights)
    dp=[[0]*(w+1) for _ in range(n+1)]
    #初始化列表
    for i in range(1,n+1):
        for w in range(w+1):
            if weights[i-1]>w:
                dp[i][w]=dp[i-1][w]
            else:
                 #在选择与不选择当前物品之间做出选择，注意这里列表weights和values的指标都要-1
                dp[i][w]=max(dp[i-1][w],dp[i-1][w-weights[i-1]]+values[i-1])
    return dp[n][w]


'''
最长公共前后缀问题(LPS Longest Prefix Suffix)
问题描述：给定一个字符串，在该字符串中，找到最长的既是前缀又是后缀的真子串，并返回该子串
'''
#模式值：代表当前字符串的最长公共前后缀长度
#模式串：str[:i] for i in range(1,len(str)+1)构成的字符串
#称str[:n]为str[:n+1]的基础串，s[j]为s[i:j]的后继字符
#算法思路：考虑字符串s的基础串，t是它的lps，若s的末字符与t的后继字符相等，则t拼接上后继字符便是s的lps，
#否则t变成s短一点的公共前后缀
def lps(str):
    ret=[0]*len(str)    #定义其模式串
    for i in range(1,len(str)):
        j=ret[i-1]    #意味着继承了基础串的公共子序列
        while True:
            if str[j]==str[i]:  #如果相等，基础串公共子序列+1
                ret[i]=j+1
                break
            elif j==0:   #该字符不相等且此前也没有公共前后缀，在该位置仍然没有前后缀
                ret[i]=0
                break
            else:     #该处不匹配，但前面已有公共前后缀，则向前考察一位，缩短子缀长度以提高其适配性
                j-=1
    return ret

#print(lps(input()))

'''
计算一维数组最大子数组和（全负范围）
使用算法：Kadane算法
'''
def max_subarray(nums):
    n=len(nums)
    if n==0:
        return 0
    max_end_here=nums[0]
    max_so_far=nums[0]
    for i in range(1,n):
        max_end_here=max(nums[i],nums[i]+max_end_here)  #比较：是此前所有项还是仅有当前项
        max_so_far=max(max_so_far,max_end_here)  #比较：是上一个最优值还是这个最优值
    return max_so_far

'''
这道题的背景是输出矩阵的最大子矩阵
二维矩阵的最大子矩阵问题，可以通过生成双指针，遍历起终行的方式转换为一维数组的最大子数组
'''
matrix=[[0,-2,-8,0],[9,2,-6,2],[-4,1,-4,1],[-1,8,0,2]]
for _ in range(1):
    n=4
    max_num=-float("inf")
    for i in range(n):  #遍历起始行
        nums = [0] * n
        for j in range(i,n):  #遍历终止行
            for k in range(n):
                nums[k]+=matrix[j][k]   #遍历终止行
            so_far=max_subarray(nums)
            if so_far>max_num:
                max_num=so_far
    print(max_num)


'''
作业题目
'''

'''
7215 简单的整数划分问题
'''
# 递归方法
def integer_partition(n,max_num):
    if n==0:
        return 1
    if n<0 or max_num==0:
        return 0
    return integer_partition(n,max_num-1)+integer_partition(n-max_num,max_num)

#动态规划方法
def count_partition_dp(n):
    dp=[[0]*(51) for _ in range(51)]
    for i in range(n+1):
        dp[0][i]=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j<=i:
                dp[i][j]=dp[i-j][j]+dp[i][j-1]
            else:
                dp[i][j]=dp[i][i]
    return dp[n][n]

#n=int(input())
#print(integer_partition(n,n))

#？？？这个程序错在哪里？为什么wrong answer


'''
1775 采药
'''

#经典背包问题
T,M=map(int,input().split())
matrix=[tuple(map(int,input().split())) for _ in range(M)]
dp=[0]*(T+1)   #初始化动归列表

for t,v in matrix:    #从耗时最长的开始遍历：我能把它放进背包里吗？
    for j in range(T,t-1,-1):   #这一行判定我是否有足够时间
        dp[j]=max(dp[j],dp[j-t]+v)    #这一行判定我花费时间摘草药是否值得

print(dp[T])



'''
8780 拦截导弹(LDS)
'''
#找到一段数组中长度最长的单调不增序列
#经典问题：求最长非递增子序列长度
#n=int(input())
#height=tuple(map(int,input().split()))
def intercept_missiles(height,n):
    dp=[1]*(n+1)   #dp[i]表示第i个位置索引的导弹是可拦截的最后一个导弹
    for i in range(n):
        for j in range(i):   #时间复杂度为O(N^2)
            if height[i]<=height[j]:   #只有后者高度小于前者才需要判断
                dp[i]=max(dp[j]+1,dp[i])
                #此时，前面第j个位置dp[j]已能反映出它之前可拦截的导弹数
    return max(dp[i] for i in range(n))

#print(intercept_missiles(height))

'''
24375 小木棍
'''
import math


def find_min_original_length(n, sticks):
    if n == 0:
        return 0
    total = sum(sticks)
    max_len = max(sticks)
    sticks.sort(reverse=True)

    # 收集所有因数，并筛选出>=max_len的候选
    factors = set()
    for i in range(1, int(math.isqrt(total)) + 1):
        if total % i == 0:
            factors.add(i)
            factors.add(total // i)
    candidates = [x for x in factors if x >= max_len]
    candidates.sort()

    for L in candidates:
        if total % L != 0:
            continue
        k = total // L
        if any(stick > L for stick in sticks):
            continue

        # 预处理sum_from数组
        m = len(sticks)
        sum_from = [0] * m
        sum_from[-1] = sticks[-1]
        for i in range(m - 2, -1, -1):
            sum_from[i] = sum_from[i + 1] + sticks[i]

        used = [False] * m

        def backtrack(start, remain, count):
            if count == 0:
                return True
            if remain == 0:
                return backtrack(0, L, count - 1)

            # 找到第一个未使用的起始位置
            start_pos = start
            while start_pos < m and used[start_pos]:
                start_pos += 1
            if start_pos >= m:
                return False
            if sum_from[start_pos] < remain:
                return False

            prev = -1
            for i in range(start_pos, m):
                if used[i]:
                    continue
                if sticks[i] > remain:
                    continue
                if sticks[i] == prev:
                    continue
                if i > 0 and sticks[i] == sticks[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                prev = sticks[i]
                success = backtrack(i + 1, remain - sticks[i], count)
                used[i] = False

                if success:
                    return True
                if remain == L:
                    return False

            return False

        if backtrack(0, L, k):
            return L

    return total


import sys

for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        break
    sticks = list(map(int, sys.stdin.readline().split()))
    print(find_min_original_length(n, sticks))


'''
23997 奇数划分
'''

#回溯-递归解法
ans=[]
def backtrack(start,remain,path):
    if remain==0:
        ans.append(path.copy())
        return
    for i in range(start,remain+1,2):
        if i>remain:
            break
        else:
            path.append(i)
            backtrack(i+2,remain-i,path)
            path.pop()

#n=int(input())
#backtrack(1,n,[])
#for i in ans:
#    print(" ".join(map(str,i)))
#print(len(ans))

#动态规划算法
#可以视作0-1背包问题的变种，不过从values最大值变成和为给定值
#dp[i][j]表示前i个奇数是可以选择用或不用的，j是要凑出来的数值

def dp_backtrack(n):
    odds=[i for i in range(1,n+1) if i%2==1]
    m=len(odds)
    dp=[[0]*(n+1) for _ in range(m+1)]
    dp[0][0]=1
    for k in range(1,m+1):
        j=odds[k-1]
        for i in range(n+1):
            dp[k][i]=dp[k-1][i]  #如果不用当前第k个奇数
            if i>=j:   #当前判定的奇数比需要表示的值更大，此时i-j>0，才有讨论用i的可能，
                       #否则我们在凑j时是不可能用i的
                dp[k][i]+=dp[k-1][i-j]
    return dp[m][n]

#n=int(input())
#print(dp_backtrack(n))

'''
25815 回文字符串
这里注意区分，如果只有增删两种操作，相当于最长回文子序列(LPS)
如果有增删改三种，显然改的效率大于增删，应该正向考虑这个问题
'''
#类比最长公子序列
def lps(str):
    n=len(str)
    if n==0:
        return 0
    else:
        dp=[[0]*(n) for _ in range(n)]
        #dp[i][i]表示str[i……j]之间的最长回文子序列长度
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if str[i]==str[j]:
                    dp[i][j]=dp[i+1][j-1]
                else:
                    dp[i][j]=min(1+dp[i+1][j],1+dp[i][j-1],1+dp[i+1][j-1])
    return dp[0][n-1]

str=input().strip()
print(lps(str))



