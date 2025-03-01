import heapq

N = int(input())  # 牛的数量
cows = []
    
# 读取每头牛的挤奶时间区间
for i in range(N):
    A, B = map(int, input().split())
    cows.append((A, B, i))
    
# 按照开始时间排序，如果开始时间相同，按结束时间排序
cows.sort()

# 记录每个牛分配的畜栏编号
result = [0] * N
# 最小堆，存储的是(结束时间, 畜栏编号)
heap = []
# 当前的畜栏编号
next_bar = 1
    
for A, B, idx in cows:
    if heap and heap[0][0] < A:  # 如果有畜栏可以使用
        # 弹出堆顶元素，表示这个畜栏可以被复用
        end_time, bar = heapq.heappop(heap)
        result[idx] = bar  # 分配畜栏
        # 把新的结束时间推入堆中
        heapq.heappush(heap, (B, bar))
    else:
        # 否则，需要新的畜栏
        result[idx] = next_bar
        heapq.heappush(heap, (B, next_bar))
        next_bar += 1  # 新的畜栏编号
    
# 输出最小畜栏数
print(len(heap))
# 输出每头牛分配的畜栏编号
for r in result:
    print(r)
