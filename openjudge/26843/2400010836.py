l=[]
count = 0

def heapify(i,k): #意味着对i处元素操作，并递归处理所有因此产生的问题
    global l
    left  = i*2+1 #两个子节点
    right = i*2+2
    if right < k:
        if l[left] > l[right]:
            larger = left
        else:
            larger = right
    elif right == k:
        larger = left
    else:
        larger = i
    if l[i] < l[larger]: #如果i小于两个子节点之最大值，则交换
        l[i],l[larger] = l[larger],l[i]
        heapify(larger,k) #处理子树，保证子树仍为堆

while True:
    n = int(input())
    if not n:
        break
    l = list(map(int,input().split()))
    k = n
    for i in range(k//2-1,-1,-1): #初始化，建立堆
        heapify(i,k)
    while k: #依次把最大值换到堆尾
        l[0],l[k-1] = l[k-1],l[0] #把堆顶的元素（最大元素）换到堆尾
        k -= 1
        heapify(0,k) #类似于行19内容，处理交换后可能产生的问题，保证余下的部分仍是最大堆
    if count:
        print()
    count += 1
    for i in range(n):
        print(l[i],end = ' ' if i != n else '')