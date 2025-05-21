def put(mmap, legal_c, r, n, k):
    if k == 0:
        return 1
    if n - r < k:
        return 0
    ans = 0
    for c in range(n):
        if legal_c[c] and mmap[r][c] == '#':
            legal_c[c] = 0
            ans += put(mmap, legal_c, r + 1, n, k - 1)
            legal_c[c] = 1
    # 下面讨论r行不放的时候
    ans += put(mmap, legal_c, r + 1, n, k)
    return ans
    

# 图的深搜
n, k = map(int, input().split())
while (n, k) != (-1, -1):
    mmap = []
    legal_c = [1] * n
    for _ in range(n):
        mmap.append(list(input()))
    print(put(mmap, legal_c, 0, n, k))
    n, k = map(int, input().split())
