# 2400010833 闵诗珈
import math

def solve(n, d, islands):
    if d < 0:
        return -1

    ranges = []
    for x, y in islands:
        if y > d:
            return -1
        delta = math.sqrt(d * d - y * y)
        ranges.append((x - delta, x + delta))

    ranges.sort(key=lambda r: r[0])
    cnt = 0
    last_covered = float('-inf')
    for start, end in ranges:
        if start > last_covered:
            cnt += 1
            last_covered = end
        else:
            last_covered = min(last_covered, end)
    return cnt

case= 1
while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break

    islands = []
    for _ in range(n):
        islands.append(list(map(int, input().split())))

    result = solve(n, d, islands)
    print(f'Case {case}: {result}')
    case += 1
    input() # 读取空行，分隔案例。