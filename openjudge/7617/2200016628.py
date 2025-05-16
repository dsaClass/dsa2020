import heapq

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

# 建立一个大小为 k 的最小堆
min_heap = []

for num in arr:
    if len(min_heap) < k:
        heapq.heappush(min_heap, num)
    else:
        if num > min_heap[0]:
            heapq.heappushpop(min_heap, num)

# 输出从大到小
for num in sorted(min_heap, reverse=True):
    print(num)
