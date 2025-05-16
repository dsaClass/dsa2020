l, n, m = map(int, input().split())
rocks = [int(input()) for _ in range(n)]
rocks = [0] + rocks + [l]  # 加上起点和终点并排序

low = 1
high = l
ans = 0

while low <= high:
    mid = (low + high) // 2
    cur_pos = 0
    move_num = 0
    for i in range(1, len(rocks)):
        if rocks[i] - cur_pos < mid:
            # 岩石太近，跳不过去，移除rocks[i]
            move_num += 1
        else:
            cur_pos = rocks[i]
    if move_num > m:
        high = mid - 1
    else:
        ans = mid
        low = mid + 1

print(ans)