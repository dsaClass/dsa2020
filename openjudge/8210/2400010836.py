l = list(map(int,input().split()))
L,N,M = l[0],l[1],l[2]
ll = [0]
for i in range(N):
    ll.append(int(input()))
ll.append(L)  #第三行与本行用于加入开头结尾两块石头

def check(ans):
    global ll
    keep = 0  #记录可以留下的石头个数，我们希望留下的越多越好
    sum = 0
    flag = 0
    for i in range(1,N+1):
        sum = ll[i]-ll[flag]  #sum从ll[flag]开始记录累计长度
        if sum >= ans:
            keep += 1
            sum = 0
            flag = i
    if ll[N+1]-ll[flag] < ans:  #最重要的一步，判断末尾边界情况，考虑是否要移除终点前的石头
        keep -= 1
    if N-keep <= M:  #check ans是否合规，即是否存在合法拿取使得石头最小间隔小于等于ans
        return 1
    return 0

low,high = 0,L  #以下为标准整数二分过程
ans = 0
mid = L
while low <= high:
    if check(mid):
        ans = mid
        low = mid+1
    else:
        high = mid-1
    mid = (low+high)//2
print(ans)