import heapq

n = int(input())
fruits = list(map(int, input().split()))

heapq.heapify(fruits)
total_energy = 0

while len(fruits) > 1:
    a = heapq.heappop(fruits)
    b = heapq.heappop(fruits)
    energy = a + b
    total_energy += energy
    heapq.heappush(fruits, energy)

print(total_energy)
