#哈夫曼树算法
#每次合并最小，并求最后的和
n=int(input())
nums=[int(input()) for i in range(n)]
ans=0
while len(nums)>1:
    n1=min(nums)
    nums.remove(n1)
    n2=min(nums)
    nums.remove(n2)
    ans+=n1+n2
    nums.append(n1+n2)
print(ans)

#二分查找(找最小)
def check(n):
    pass
left=None #设置left 和 right
right=None
while left<right:
    mid=(left+right)//2
    if check(mid):
        right=mid
    else:
        left=mid+1
print(left)

#二分查找（找最大）
def check(n):
    pass
left=None #设置left 和 right
right=None
while left<right:
    mid=(left+right+1)//2  
    if check(mid):
        left=mid 
    else:
        right=mid-1 
print(left)


#求二分后的逆序对
def count(l1,l2):
    l1.sort()
    l2.sort()
    n=len(l2)
    l2.append(-1)
    j=0
    num=0
    for i in l1:
        while j<n and l2[j]<i:
            j+=1
        num+=(n-j)
    return num


#并查集模板
parent = list(range(n + 1))
rank   = [0] * (n + 1)
cnt = n 
                              # 初始每人一块
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])   # 路径压缩
    return parent[x]

def union(x, y):
    rx, ry = find(x), find(y)
    if rx == ry:
        return
    if rank[rx] < rank[ry]:
        rx, ry = ry, rx
    parent[ry] = rx            # 按秩合并，便于查找 如果已经制定了合并顺序，则无需比较rank
    if rank[rx] == rank[ry]:
        rank[rx] += 1
    global cnt
    cnt -= 1 


#字符串KMP
def compute_prefix_function(P):
    m = len(P)
    next = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and P[i] != P[j]:
            j = next[j - 1]
        if P[i] == P[j]:
            j += 1
        next[i] = j
    return next

def kmp_search(T, P):
    n, m = len(T), len(P)
    next = compute_prefix_function(P)
    j = 0
    result = []
    for i in range(n):
        while j > 0 and T[i] != P[j]:
            j = next[j - 1]
        if T[i] == P[j]:
            j += 1
        if j == m:
            result.append(i - m + 1)
            j = next[j - 1]
    return result

print("匹配位置：", kmp_search('abcabcabcabc', 'abcab'))  # 输出 [0, 3, 6]


#解同余线性方程组 A x ≡ b (mod mod) 返回: 是否有解，特解，自由变量下标，齐次解基
import math

def gauss_mod(A, b, mod):
    n, m = len(A), len(A[0])
    A = [row[:] for row in A]
    b = b[:]
    where = [-1] * m
    row = 0

    # 消元
    for col in range(m):
        piv = next((i for i in range(row, n)
                    if A[i][col] % mod and math.gcd(A[i][col], mod) == 1), None)
        if piv is None: continue
        A[row], A[piv] = A[piv], A[row]
        b[row], b[piv] = b[piv], b[row]
        where[col] = row
        inv = pow(A[row][col], -1, mod)
        for j in range(col, m): A[row][j] = A[row][j] * inv % mod
        b[row] = b[row] * inv % mod
        for i in range(n):
            if i != row and A[i][col]:
                f = A[i][col]
                for j in range(col, m): A[i][j] = (A[i][j] - f * A[row][j]) % mod
                b[i] = (b[i] - f * b[row]) % mod
        row += 1
        if row == n: break

    # 无解判定
    for i in range(row, n):
        if all(A[i][j] % mod == 0 for j in range(m)) and b[i] % mod:
            return False, [], [], []

    # 构造特解
    x = [0] * m
    for j in range(m):
        if where[j] != -1:
            x[j] = b[where[j]] % mod

    # 构造齐次解基
    free_vars = [j for j in range(m) if where[j] == -1]
    basis = []
    for k in free_vars:
        v = [0] * m
        v[k] = 1
        for j in range(m):
            i = where[j]
            if i != -1:
                s = sum(A[i][ℓ] * v[ℓ] for ℓ in free_vars) % mod
                v[j] = (-s) % mod
        basis.append(v)

    return True, x, free_vars, basis

#测试样例，需调整输入输出
A=[]
b=[]
mod=3
ok, sol, free_vars, basis = gauss_mod(A, b, mod)
if not ok:
    print("无解")
else:
        print("有解")
        print("一个特解：", sol)
        print("自由变量下标：", free_vars)
        print("齐次解基：")
        for v in basis:
            print("  ", v)
