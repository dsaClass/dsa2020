import heapq

n = int(input())
cows = []
for i in range(n):
    a, b = map(int, input().split())
    cows.append((a, b, i))  # 记录原始索引以便输出

# 按开始时间排序
cows.sort()

# 优先队列，存储 (结束时间, 畜栏编号)
heap = []
# 记录每头牛被分配的畜栏编号
assigned = [0] * n
# 畜栏编号从1开始
pen_number = 1

for cow in cows:
    a, b, idx = cow
    if heap and heap[0][0] < a:
        # 可以复用畜栏
        earliest_end, pen = heapq.heappop(heap)
        assigned[idx] = pen
        heapq.heappush(heap, (b, pen))
    else:
        # 需要新增畜栏
        assigned[idx] = pen_number
        heapq.heappush(heap, (b, pen_number))
        pen_number += 1

# 输出最少的畜栏数量
print(pen_number - 1)
# 输出每头牛被分配的畜栏编号
for i in range(n):
    print(assigned[i])