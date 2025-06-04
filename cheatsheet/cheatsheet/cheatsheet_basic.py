'''
有关 sys 模块
'''
def main():
    import sys

    #单行单个数据
    n=int(sys.stdin.readline().strip())  #整数
    s=sys.stdin.readline().strip()  #字符串

    #单行多个数据
    arr=list(map(int,sys.stdin.readline().split()))

    #一次性读取所有数据
    all_input=sys.stdin.read().strip()
    lines=all_input.split("\n")

    #未知行数，可能包含空行，一次性读完所有数据，并储存进一个列表
    nums = []
    for line in sys.stdin:
        for i in line.split():
            nums.append(int(i))


'''
部分作业题
'''
'''
P1748 Josephus Problem
'''
def josephus(n,k):
    monkeys=[i for i in range(1,n+1)]
    tps=0
    while len(monkeys)>1:
        tps=(tps+k-1)%len(monkeys)
        monkeys.remove(monkeys[tps])
    return monkeys[0]

mission=[]
while True:
    lst=list(map(int,input().split()))
    if lst[0]==0:
        break
    mission.append(lst)

for i in range(len(mission)):
    print(josephus(mission[i][0],mission[i][1]))

'''
螺旋加密
'''
#5. 螺旋加密
def password(m,n,s):
    ans=""
    for i in s:
        if i==" ":
            ans+="00000"
        else:
            cache=ord(i)-ord("A")+1
            cache=(bin(cache))[2:]
            cache=f'{cache:0>5}'
            ans+=cache
    ans+="0"*(m*n-len(s)*5)
    return ans

def sprial_matrix(m,n,ans):
    matrix=[[0]*n for _ in range(m)]
    num=0
    left,right,top,bottom=0,n-1,0,m-1
    while left<=right and top<=bottom:
        #从左到右遍历上边界
        for i in range(left,right+1):
            matrix[top][i]=ans[num]
            num+=1
        top+=1

        #从上到下遍历右边界
        for i in range(top,bottom+1):
            matrix[i][right]=ans[num]
            num+=1
        right-=1

        #从右到左遍历下边界
        for i in range(right,left-1,-1):
            matrix[bottom][i]=ans[num]
            num+=1
        bottom-=1

        #从下到上遍历左边界
        for i in range(bottom,top-1,-1):
            matrix[i][left]=ans[num]
            num+=1
        left+=1
    return matrix

'''
7207 神奇的幻方
'''
from mpl_toolkits.mplot3d.art3d import poly_collection_2d_to_3d


def magic_square(n):
    matrix=[[0]*(2*n-1)for _ in range(2*n-1)]
    i=1
    j,k=0,n-1
    while i<=(2*n-1)**2:
        matrix[j][k]=i
        i+=1
        if j==0 and k==2*n-2:
            j,k=1,2*n-2
        elif j==0:
            j,k=2*n-2 , k+1
        elif k==2*n-2:
            j,k=j-1,0
        elif matrix[j-1][k+1]!=0:
            j+=1
        else:
            j,k=j-1,k+1
    return matrix
'''
n=int(input())
matrix=magic_square(n)
tps=0
while tps<2*n-1:
    print(" ".join(map(str,matrix[tps])))
    tps+=1
'''

'''
题目复盘：行列式的指标可以用row（行）,col（列）
中间判定的代码可以狠狠简化，row+1超限返回0，相当于对方阵行列数size取余
修改代码如下：
'''
def approved_magic_square(n):
    size=2*n-1
    matrix=[[0]*size for _ in range(size)]
    i=1
    row,col=0,n-1
    while i<=size**2:
        matrix[row][col]=i
        i+=1
        new_row,new_col=(row+1)%size,(col+1)%size
        if matrix[new_row][new_col]:
            row+=1
        else:
            row,col=new_row,new_col
    return matrix


""" 
21006 方苹果（盘子相同）
把M个同样的苹果放在N个同样的盘子里，允许有的盘子空着不放，
问共有多少种不同的分法？（用K表示）5，1，1和1，5，1 是同一种分法。
这是一道组合数学问题，可以用递归或动态规划实现
"""
#以下是一种用动态规划实现的方法
def count_ways_dp(n,m):
    dp=[[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][1]=1
    for j in range(1,m+1):
        dp[0][j]=1
    for i in range(1,n+1):
        for j in range(2,m+1):
            if i<j:
                dp[i][j]=dp[i][i]
            else:
                dp[i][j]=dp[i-j][j]+dp[i][j-1]
    return dp[n][m]

#以下是一种用递归实现的方法,不过这种递归超越了最大栈深度，很不建议
def count_ways_recursion(n,m):
    if n==1 or m==0:
        return 1
    elif m<n:
        return count_ways_recursion(m,m)
    else:
        return count_ways_recursion(n-m,m)+count_ways_recursion(n,m-1)

#n,m=map(int,input().split())
#print(count_ways_dp(n,m))

'''
27800 波兰表达式
波兰表达式是一种把运算符前置的算术表达式，例如普通的表达式2 + 3的波兰表示法为+ 2 3。
波兰表达式的优点是运算符之间不必有优先级关系，也不必用括号改变运算次序，例如(2 + 3) * 4的
波兰表示法为* + 2 3 4。本题求解波兰表达式的值，其中运算符包括+ - * /四个。
'''
def polish_notation(expression):
   stack=[]
   cal=["+","-","*","/"]
   for token in reversed(expression):
       if token not in cal:
           stack.append(float(token))
       else:
           a=stack.pop()
           b=stack.pop()
           if token=="+":
               stack.append(a+b)
           elif token=="-":
               stack.append(a-b)
           elif token=="*":
               stack.append(a*b)
           elif token=="/":
               stack.append(a/b)

   return stack.pop()

#expression=list(input().split())
#print("{:.1f}".format(polish_notation(expression)))

'''
5379 队列操作
'''
def is_queue(operation):
    queue=[]
    for i in operation:
        if i[0]=="+":
            queue.append(i[1:])
        elif queue==[] or i[1:]!=queue[0]:
            return "no"
        else:
            queue.pop(0)
    return "yes"
'''
n=int(input())
for i in range(n):
    m=int(input())
    operation=list(input().split(" "))
    print("Case {}: {}".format(i+1,is_queue(operation)))
'''


"""
5345 位查询
"""
def C(numbers,d):
    d=d%65536
    new_numbers=[]
    for number in numbers:
        new_numbers.append((number+d)%65536)
    return new_numbers

def Q(numbers,i):
    ans=0
    for number in numbers:
        number=bin(number)[2:]
        if len(number)>=i+1:
            if number[-i-1]=="1":
                ans+=1
    return ans

#以下是一个降低代码时间复杂度的方法，用到了掩码来判断二进制第i位是否为1
def better_Q(numbers,i):
    mask=1<<i
    return sum(1 for number in numbers if number&mask==1)

'''
n,m=map(int,input().split())
numbers=list(map(int,input().split()))
operate=[]
tps=0
while tps<m:
    operate.append(list(input().split()))
    tps+=1

for j in range(len(operate)):
    if operate[j][0]=="C":
        numbers=(C(numbers,int(operate[j][1])))
    else:c 
        print(better_Q(numbers,int(operate[j][1])))

'''

'''
利用本题总结掩码的用法：
掩码(mask)是一个二进制数，用于提取或检查目标数字的某一位
mask=1<<i 本身生成一个长度为8的二进制数，表示将1向左移动i位
可用逻辑判断来进行逐位比较，如number & mask 会自动比较两个数的二进制形式

以上的做法依然会超过时限，下面利用前缀和优化方法
'''
'''
n,m=map(int,input().split())
numbers=list(map(int,input().split()))
operate=[]
tps=0
while tps<m:
    operate.append(list(input().split()))
    tps+=1

prefix=[[0]*(n+1) for _ in range(16)]
for i in range(16):
    for j in range(1,n+1):
        prefix[i][j]=prefix[i][j-1]+((numbers[j-1]>>i&1))

shift=0
output=[]
for k in range(len(operate)):
    if operate[k][0]=="C":
        d=int(operate[k][1])
        shift=(shift+d)%65536
    else:
        i=int(operate[k][1])
        mask=1<<i
        ans=sum(1 for number in numbers if number&mask==1)
        output.append(ans)
print("\n".join(map(str,output)))

'''
"""
5467 多项式加法
"""
def summation(numbers1,numbers2):
    numbers1.sort(key=lambda x:x[1],reverse=False)
    numbers2.sort(key=lambda x:x[1],reverse=False)
    ans=[]
    while numbers1 or numbers2:
        if not numbers1:
            while numbers2:
                tps=numbers2.pop()
                if ans and ans[-1][1]==tps[1]:
                    ans[-1][0]+=tps[0]
                    if ans[-1][0]==0:
                        ans.pop()
                else:
                    ans.append(tps)
            break
        elif not numbers2:
            while numbers1:
                tps = numbers1.pop()
                if ans and ans[-1][1] == tps[1]:
                    ans[-1][0] += tps[0]
                    if ans[-1][0] == 0:
                        ans.pop()
                else:
                    ans.append(tps)
            break
        else:
            if numbers1[-1][1]>numbers2[-1][1]:
                item=numbers1.pop()
            elif numbers2[-1][1]>numbers1[-1][1]:
                item=numbers2.pop()
            else:
                coeff=numbers1[-1][0]-numbers2[-1][0]
                exp=numbers1[-1][1]
                numbers1.pop()
                numbers2.pop()
                if coeff!=0:
                    item=[coeff,exp]
                else:
                    continue
        #处理item项
        if item[0]==0:
            continue
        if ans and ans[-1][1]==item[1]:   #这里得确保ans有元素，否则会越界
            ans[-1][0]+=item[0]
            if ans[-1][0]==0:   #每次进行加和操作后，都要注意检查系数是否为0
                ans.pop()
        else:
            ans.append(item)
    return ans

def format_polynomial(poly):
    terms = []
    for power in poly:
        terms.append("[ {} {} ]".format(power[0], power[1]))
    return " ".join(terms)

n=int(input())
for i in range(n):
    poly_1=[]
    poly_2=[]
    numbers_1=list(map(int,input().split()))
    for i in range(0,len(numbers_1)-2,2):
       poly_1.append([numbers_1[i],numbers_1[i+1]])
    numbers_2=list(map(int,input().split()))
    for i in range(0,len(numbers_2)-2,2):
        poly_2.append([numbers_2[i],numbers_2[i+1]])
    result=summation(poly_1,poly_2)
    print(format_polynomial(result))





'''
        elif numbers1[-1][1]==numbers2[-1][1]:
            if numbers1[-1][0] + numbers2[-1][0] != 0:
                ans.append([numbers1[-1][0]+numbers2[-1][0],numbers1[-1][1]])
            numbers1.pop()
            numbers2.pop()
        elif numbers1[-1][1]>numbers2[-1][1] and numbers1[-1][0]!=0:
            if ans and numbers1[-1][1]==ans[-1][1]:
                ans[-1][0]+=numbers1[-1][0]
                if ans[-1][0]==0:
                    ans.pop()
                numbers1.pop()
            else:
                ans.append(numbers1.pop())
        elif numbers1[-1][1]<numbers2[-1][1]:
            if ans and numbers2[-1][1]==ans[-1][1]:
                ans[-1][0]+=numbers2[-1][0]
                if ans[-1][0]==0:
                    ans.pop()
                numbers2.pop()
            else:
                ans.append(numbers2.pop())

    return ans
'''

