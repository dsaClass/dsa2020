l = list(map(int,input().split()))
L,N,M = l[0],l[1],l[2]
ll = [0]
for i in range(N):
    ll.append(int(input()))
ll.append(L)

def check(ans):
    global ll
    keep = 0
    sum = 0
    flag = 0
    for i in range(1,N+1):
        sum = ll[i]-ll[flag]
        if sum >= ans:
            keep += 1
            sum = 0
            flag = i
    if ll[N+1]-ll[flag] < ans:
        keep -= 1
    if N-keep <= M:
        return 1
    return 0

low, high = 0, L
result = 0
mid = L
while low <= high:
    if check(mid):
        result = mid
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2
print(result)
