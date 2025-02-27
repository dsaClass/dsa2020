import heapq
def dijkstra(adj, start, n):
    dist=[float('inf')]*(n+1)
    dist[start]=0
    heap=[(0,start)]
    while heap:
        current_dist,u=heapq.heappop(heap)
        if current_dist > dist[u]:
            continue
        for v,time in adj[u]:
            if dist[v]>current_dist+time:
                dist[v]=current_dist+time
                heapq.heappush(heap, (dist[v], v))
    return dist
while True:
    n=int(input())
    if n==0:
        break
    adj=[[] for _ in range(n+1)]
    for i in range(1,n+1):
        adj = [[] for _ in range(n+1)]
    for i in range(1,n+1):
        parts=list(map(int, input().split()))
        cnt=parts[0]
        rest=parts[1:]
        contacts=rest[::2]
        times=rest[1::2]
        for contact,time in zip(contacts,times):
            adj[i].append((contact,time))
    best_start=None
    min_max_time=float('inf')
    for start in range(1,n+1):
        dist=dijkstra(adj,start,n)
        max_time=max(dist[1:])
        if max_time < min_max_time:
            min_max_time=max_time
            best_start=start
    print(f"{best_start} {min_max_time}")
