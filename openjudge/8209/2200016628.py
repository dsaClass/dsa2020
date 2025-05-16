N,M = map(int,input().split())
costs =[int(input()) for _ in range(N)]
low = max(costs)
high = sum(costs)
ans = high
while low<=high:
    mid = (low+high)//2
    period = 1
    this_p_cost = 0
    for c in costs:
        this_p_cost += c
        if this_p_cost > mid:
            period += 1
            this_p_cost = c
        else:
            continue

    if period <= M:
        ans = mid
        high = mid -1
    else:
        low=mid+1

print(ans)

