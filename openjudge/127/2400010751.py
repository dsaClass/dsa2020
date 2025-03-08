import sys, heapq
data = sys.stdin.read().split()
idx = 0
while True:
    n = int(data[idx])
    idx += 1
    if n == 0:
        break
    # 构造图：节点编号 1..n
    graph = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        contacts = int(data[idx])
        idx += 1
        for _ in range(contacts):
            j = int(data[idx])
            t = int(data[idx + 1])
            idx += 2
            graph[i].append((j, t))

    best_person, best_time = 0, float('inf')
    for start in range(1, n + 1):
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        heap = [(0, start)]
        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))
        max_time = max(dist[1:])
        if max_time < best_time:
            best_time = max_time
            best_person = start
    print("disjoint" if best_time == float('inf') else f"{best_person} {best_time}")
