import sys
def pro1(n,k):
    dp1=[[0]*(n+1) for i in range(k+1)] #希望dp1[i][j]记录下把j分为i个数的分拆数
    dp1[0][0]=1
    for i in range(1,k+1):
       for j in range(1,n+1):
         if j<i:dp1[i][j]=0
         elif j==i:dp1[i][j]=1
         else:dp1[i][j]=dp1[i-1][j-1]+dp1[i][j-i] #根据分拆中有没有1分类
    return dp1[k][n]
def pro2(n):
    '''dp2=[[0]*n for i in range(n+1)] #希望dp2[i][j]记录下把j拆成若干个不同且最大数不超过i的分拆数
       dp2[0][0]=1
       for i in range(1,n+1):
         for j in range(n,i-1,-1):   #防止j-i已经被计算过含i的可能性了
            dp[i][j]=dp[i-1][j]+dp[i][j-i]  #分类讨论分拆数是否含i
       return dp2[n][n]'''
    #改进的Idea
    dp2=[0]*(n+1)
    dp2[0]=1
    for i in range(1,n+1):
        for j in range(n,i-1,-1):
            dp2[j]+=dp2[j-i] #相比改进之前不需引进二位序列
    return dp2[n]

def pro3(n):
    dp3=[0]*(n + 1)
    dp3[0]=1
    for i in range(1,n+1,2):
        for j in range(i,n+1):
            dp3[j]+=dp3[j - i]
    return dp3[n]

for line in sys.stdin:
    line = line.strip()
    n, k = map(int, line.split())
    print(pro1(n,k))
    print(pro2(n))
    print(pro3(n))