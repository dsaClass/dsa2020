import sys

def count_subtree_nodes(m, n):
    if m == 0:
        return 0
    sum_nodes = 0
    level = 0
    while True:
        start = m * (2 ** level)
        if start > n:
            break
        end = start + (2 ** level - 1)
        if end <= n:
            count = 2 ** level
        else:
            count = n - start + 1
        sum_nodes += count
        level += 1
    return sum_nodes

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    m, n = map(int, line.split())
    if m == 0 and n == 0:
        break
    print(count_subtree_nodes(m, n))