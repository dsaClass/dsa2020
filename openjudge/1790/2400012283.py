def count_nodes(m, n):
    count = 0
    level = 0
    while m <= n:
        nodes_in_level = min(2**level, n - m + 1)
        count += nodes_in_level
        m *= 2
        level += 1
    return count

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    print(count_nodes(m, n))