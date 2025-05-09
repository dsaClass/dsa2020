import math
n,f = map(int,input().strip().split())
def trans(s):
    return (int(s)**2)*100000

cakes = list(map(trans,input().strip().split()))
def check(x):
    count = 0
    for cake in cakes:
        count += cake // x
    return count >= (f+1)
cakes.sort()

l,r = 1,max(cakes)
best = 0
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        best = mid
        l = mid + 1
    else:
        r = mid - 1
ans = best*math.pi /100000
print(f"{ans:.3f}")