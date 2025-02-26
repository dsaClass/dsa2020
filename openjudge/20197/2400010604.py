def count_squares(N, M):
    count = 0
    while N > 0 and M > 0:
        min_side = min(N, M)
        count += 1
        if N > M:
            N -= min_side
        else:
            M -= min_side
    return count

l=list(map(int,input().split()))
n,m=l[0],l[1]
print(count_squares(n,m))