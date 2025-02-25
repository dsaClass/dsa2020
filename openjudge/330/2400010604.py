import math

def minimal_radar_installations(n, d, islands):
    # 判断是否有解
    for island in islands:
        x, y = island
        if y > d:
            return -1

    # 计算每个岛屿的可覆盖区间
    intervals = []
    for island in islands:
        x, y = island
        delta = math.sqrt(d ** 2 - y ** 2)
        li = x - delta
        ri = x + delta
        intervals.append((li, ri))

    # 按照区间的右端点进行排序
    intervals.sort(key=lambda x: x[1])

    # 贪心选择雷达位置
    radar_count = 0
    last_radar = -float('inf')
    for interval in intervals:
        li, ri = interval
        if li > last_radar:
            radar_count += 1
            last_radar = ri

    return radar_count

case_number = 1
while True:
    l = list(map(int, input().split()))
    n, d = l[0], l[1]
    if n == 0 and d == 0:
        break
    islands = []
    for _ in range(n):
        x, y = map(int, input().split())
        islands.append((x, y))
    # 处理每个测试案例
    result = minimal_radar_installations(n, d, islands)
    print(f"Case {case_number}: {result}")
    case_number += 1
    input()