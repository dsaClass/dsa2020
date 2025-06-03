'''
基础知识
'''
#谢尔排序
def shellSort(nums):
    gap = len(nums) // 2
    while gap>0:
        for i in range(gap,len(nums)):
            temp=nums[i]
            j=i
            while j>=gap and nums[j-gap]>=temp: #类似于插入排序
                nums[j]=nums[j-gap]
                j-=gap
            nums[j]=temp
        gap//=2
    return nums

#快速排序
def partition(nums, left, right):
    pivot = nums[left]  # 步骤1：选择最左侧元素作为基准
    i, j = left + 1, right  # 步骤2：初始化指针（i从left+1开始）

    while True:
        # 步骤3：从左找>pivot的元素
        while i <= j and nums[i] <= pivot:
            i += 1

        # 步骤4：从右找<pivot的元素
        while i <= j and nums[j] >= pivot:
            j -= 1

        # 步骤5：检查指针位置
        if i > j:
            break  # 指针交叉，分区结束

        # 步骤6：交换错位元素
        nums[i], nums[j] = nums[j], nums[i]

    # 步骤7：将基准放到正确位置
    nums[left], nums[j] = nums[j], nums[left]
    return j  # 返回基准位置


def quickSorting(nums, left, right):
    # 递归终止条件：子数组长度<=1
    if left >= right:
        return

    # 分区操作并获取基准位置
    pivot_index = partition(nums, left, right)

    # 递归排序左子数组（基准左侧）
    quickSorting(nums, left, pivot_index - 1)

    # 递归排序右子数组（基准右侧）
    quickSorting(nums, pivot_index + 1, right)


#归并排序（分治+拉链排序）
def mergeSort(nums):
    if len(nums)<=1:
        return nums
    left=nums[:len(nums)//2]
    right=nums[len(nums)//2:]
    mergeSort(left)
    mergeSort(right)
    i,j=0,0
    nums.clear()   #避免再建一个列表导致浪费更多空间&递归过程的nums不一样
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            nums.append(left[i])
            i+=1
        else:
            nums.append(right[j])
            j+=1
    else:
        nums.extend(left[i:] if i<j else right[j:])
    return nums

nums=[21,1,26,45,29,28,2]
print(mergeSort(nums))
print(shellSort(nums))
quickSorting(nums,0,len(nums)-1)
print(nums)
#顺序查找：很傻的一种算法
def sequentialSearch(nums,target):
    for num in nums:
        if num==target:
            return nums.index(num)
        elif num>target:
            return None
    else:
        return None


#二分查找的while函数双指针表示法

n,k=map(int,input().split())
woods=[]
for _ in range(n):
    woods.append(int(input()))
max=sum(woods)//k

if max==0:
    print(0)
    exit(0)
#如此可以找到满足题意的最大值
low,high=1,max   #这里代表的范围应该是闭区间
while low<=high:  #注意判定条件，break的条件是 low>high
    mid=(low+high)//2
    tps=0
    for wood in woods:
        tps+=wood//mid
    if tps<k:
        high=mid-1  #不-1的话会陷入无限循环
    elif tps>=k:  #这一步同时也为了找到满足题意的最大值
        low=mid+1
print(high)


#二分查找的列表表示法
def binarySearch(nums,target):
    i,j=0,len(nums)-1
    found=False
    while i<=j and not found:
        mid=(i+j)//2
        if nums[mid]==target:
            found=True
            return mid
        elif nums[mid]>target:
            return binarySearch(nums[:mid],target)
        else:
            return binarySearch(nums[mid+1:],target)

#二分查找的经典运用场景：最小值最大化&最大值最小化

'''
实战题目
'''
#切木材（去年机考题）（二分查找）
def binary_search(low,high):
    tps=0
    mid=(low+high)//2
    if low==high:
        return mid
    for wood in woods:
        tps+=wood//mid
    if tps>k:
        return binary_search(mid+1,high)
    elif tps<k:
        return binary_search(low,mid)
    else:
        return mid
mid=binary_search(0,2*max)
if mid==0:
    print(0)
else:
    while True:
        mid+=1
        new_tps=0
        for wood in woods:
            new_tps+=wood//mid
        if new_tps<k:
            print(mid-1)
            break

#越野跑超过人数（归并排序）
n=int(input())
nums=[]
for _ in range(n):
    nums.append(int(input()))
ans=0
def sorting(nums):
    global ans
    if len(nums)<=1:
        return nums
    a=len(nums)//2
    left=sorting(nums[:a])
    right=sorting(nums[a:])
    new_nums=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            new_nums.append(left[i])
            ans+=len(right)-j
            i+=1
        elif left[i]>=right[j]:
            new_nums.append(right[j])
            j+=1
    new_nums.extend(left[i:] if i<len(left) else right[j:])
    return new_nums
new_nums=sorting(nums)
print(ans)

#8209 月度开销（二分查找）
n,m=map(int,input().split())
payment=[]
for _ in range(n):
    payment.append(int(input()))

def kaixiao(target):
    count=1
    current_sum=0
    for i in payment:
        if current_sum+i<=mid:
            current_sum+=i
        else:
            count+=1
            current_sum=i
    return count


low,high=max(payment),sum(payment)
while low<high:
    mid=(low+high)//2
    if kaixiao(mid)<=m:  #可能正确的情况，但我们希望得到更小的m
        high=mid
    elif kaixiao(mid)>m:  #一定错误的情况，要修改边界值将原low规避掉
        low=mid+1

print(low)

#7613 白细胞计数
'''
n=int(input())
sample=[]
for i in range(n):
    sample.append(float(input()))
sample.sort()
average=sum(sample[1:-1])/(n-2)
max=max(sample[-2]-average,average-sample[1])
print("{:.2f}".format(average),"{:.2f}".format(max))
'''


#7745 整数奇偶排序
'''
nums=list(map(int,input().split()))
odd=[]
even=[]
for i in nums:
    odd.append(i) if i%2==1 else even.append(i)
odd.sort(reverse=True)
even.sort()
if odd:
    print(" ".join(str(x) for x in odd)+" "+" ".join(str(x) for x in even))
else:
    print(" ".join(str(x) for x in even))
'''

#8207 和为给定数
'''
n=int(input())
nums=list(map(int,input().split()))
target=int(input())

nums1=[num for num in nums if num<=target]
nums1.sort()

left,right=0,len(nums1)-1
found=False

while left<right:
    a=nums1[left]+nums1[right]
    if a==target:
        print(nums1[left],nums1[right])
        found=True
        break
    elif a<target:
        left+=1
    else:
        right-=1
if not found:
    print("No")

'''

#月度开销
def fajo(arr,m,Min,Max):
    def is_feasible(arr,m,limit):
        count=1
        sum=0

        for i in range(len(arr)):
            if arr[i]>limit:
                return False
            if sum+arr[i]<=limit:
                sum+=arr[i]
            else:
                count+=1
                sum=arr[i]
        if count<=m:
            return True
        else:
            return False

    result=Max

    while Min<=Max:
        Mid=Min+(Max-Min)//2
        if is_feasible(arr,m,Mid):
            result=min(result,Mid)
            Max=Mid-1
        else:
            Min=Mid+1
    return result

'''
n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))
Min=max(arr)
Max=sum(arr)

print(fajo(arr,m,Min,Max))
'''

#5472 求逆序对数
def merge(arr,left,mid,right):
    i=left
    j=mid+1
    temp=[]
    count=0
    while i<= mid and j <=right:
        if arr[i]<=arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            count+=(mid-i+1)
            j+=1
        for k in range(len(temp)):
            arr[left+k]=temp[k]
        return count

def merge_sort(arr,left,right):
    if left>=right:
        return 0
    mid=(left+right)//2
    count=merge_sort(arr,left,mid)+merge_sort(arr,mid+1,right)
    count+=merge(arr,left,mid,right)
    return count

def bubble_sort(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count += 1
    return swap_count


#9201 Freda越野跑（逆序对数）
#n=int(input())
#arr=list(map(int,input().split()))
#ans=0

def merge_sort(arr):
    global ans
    if len(arr)==1:
        return arr
    k=len(arr)//2
    a=merge_sort(arr[:k])
    b=merge_sort(arr[k:])
    a.append(-1)
    b.append(-1)
    inda,indb=0,0
    for i in range(len(arr)):
        if a[inda]<b[indb]:
            arr[i] = b[indb]
            ans+=k+indb-i
            indb+=1
        else:
            arr[i]=a[inda]
            inda+=1
    return arr

#merge_sort(arr)
#print(ans)

#20741 两座孤岛最短距离
from collections import deque

#n=int(input())
#matrix=[]
#for _ in range(n):
#    matrix.append(list(input()))

def dfs(matrix,i,j,island_num):
    if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or matrix[i][j]!="1":
        return
    matrix[i][j]=island_num
    dfs(matrix,i+1,j,island_num)
    dfs(matrix,i-1,j,island_num)
    dfs(matrix,i,j+1,island_num)
    dfs(matrix,i,j-1,island_num)

def bfs(matrix,island_num):
    directions=[(0,1),(0,-1),(-1,0),(1,0)]
    queue=deque()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==island_num:
                queue.append((i,j,0))
    while queue:
        x,y,steps=queue.popleft()
        for dx,dy in directions:
            newx,newy=x+dx,y+dy
            if 0<=newx<len(matrix) and 0<=newy<len(matrix[0]):
                if matrix[newx][newy]==-island_num:
                    return steps
                elif matrix[newx][newy]=="0":
                    matrix[newx][newy]=island_num
                    queue.append((newx,newy,steps+1))

'''
island_num=2
for i in range(n):
    for j in range(len(matrix[0])):
        if matrix[i][j]=="1":
            dfs(matrix,i,j,island_num)
            island_num=-2

result=bfs(matrix,island_num)
print(result)

'''

#8208 矩形分割
R=int(input())
n=int(input())
square=[]
for _ in range(n):
    square.append(list(map(int,input().split())))
total_size=0

for i in range(n):
    total_size+=square[i][2]*square[i][3]

def size(x):
    size=0
    for i in range(len(square)):
        if square[i][0]+square[i][2]<=x:
            size+=square[i][2]*square[i][3]
        elif square[i][0]<x:
            size+=(x-square[i][0])*square[i][3]
    return size

def check(x):
    left=size(x)
    right=total_size-size(x)
    return left>=right

l,r=0,R
while l<r:
    mid=(l+r)//2
    if check(mid):
        r=mid
    else:
        l=mid+1

ans=l
while size(ans)==size(ans+1) and ans+1<=R:
    ans+=1
print(ans)



'''
其他补充知识
'''
'''
选择排序
原理：开启一轮循环，从未排序空间中选出最小元素放到排序空间末尾
评价：时间复杂度O(N^2)，非自适应、非稳定排序、指针需要额外空间
'''
def selection_sort(nums):
    for i in range(len(nums)-1):  #外循环，未排序区间[i,n-1]
        for j in range(i,len(nums)):  #内循环，找到未排序区间最小元素
            if nums[j]<nums[i]:
                nums[j],nums[i]=nums[i],nums[j]    #将最小元素与内循环首个元素交换
    return nums

nums=list(map(int,input().split()))
print(selection_sort(nums))

'''
冒泡排序
原理：连续比较与交换相邻元素实现排序
评价：最差时间复杂度O(N^2)，最佳时间复杂度O(N)，对应输入数组完全有序时
'''
def bubble_sort(nums):
    for i in range(len(nums)-1,0,-1):  #外循环从尾部开始
        flag=False
        for j in range(i):
            if nums[j]>nums[j+1]:  #内循环，与自己相邻的元素对比
                nums[j],nums[j+1]=nums[j+1],nums[j]
                flag=True
        if not flag:
            break
    return nums
'''
插入排序
原理：数组左侧是已排好序的子数组，子数组右侧是要排序的元素base，从右往左地与左侧元素比较
    如果更小，左侧元素索引右移；否则放在这个位置
评价：最差时间复杂度O(N^2)，最佳时间复杂度O(N)，对应输入数组完全有序时
     自适应排序、原地排序、稳定排序
     在数据量较小时，插入排序比快速排序更快
'''
def insertion_sort(nums):
    for i in range(1,len(nums)):
        base=nums[i]
        j=i-1
        while j>=0 and nums[j]>base:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=base
    return nums
