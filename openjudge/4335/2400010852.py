import heapq
n=int(input())
heap=[]
for _ in range(n):
    l=int(input())
    heapq.heappush(heap,l)
cost=0
while len(heap)>1:
    a=heapq.heappop(heap)
    b=heapq.heappop(heap)
    merged=a+b
    cost+=merged
    heapq.heappush(heap,merged)
print(cost)
