import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n)]
indegree = [0] * n

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    indegree[v] += 1

queue = deque()
for i in range(n):
    if indegree[i] == 0:
        queue.append(i)

count = 0
while queue:
    u = queue.popleft()
    count += 1
    for v in adj[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)

print("yes" if count != n else "no")