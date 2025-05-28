import sys

def comb(n, m):
    # 组合数 C(n, m)
    if m < n - m:
        m = n - m
    ans = 1
    for i in range(m + 1, n + 1):
        ans *= i
    for i in range(1, n - m + 1):
        ans //= i
    return ans

def possible(preord, postord, n, preleft, preright, postleft, postright):
    cnt = 0
    root = preleft + 1
    total = 1
    while root <= preright:
        i = postleft
        while i <= postright and postord[i] != preord[root]:
            i += 1
        size = i - postleft + 1
        subtree_count = possible(preord, postord, n, root, root + size - 1, postleft, i)
        total *= subtree_count
        cnt += 1
        root += size
        postleft = i + 1
    total *= comb(n, cnt)
    return total

def solve(n, preord, postord):
    return possible(preord, postord, n, 0, len(preord) - 1, 0, len(postord) - 1)

# 处理输入
for line in sys.stdin:
    line = line.strip()
    if line == '0':
        break
    parts = line.split()
    n = int(parts[0])
    preord = parts[1]
    postord = parts[2]
    print(solve(n, preord, postord))