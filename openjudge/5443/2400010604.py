import heapq

def solve():
    P = int(input())
    locations = []
    name_to_index = {}
    for i in range(P):
        name = input().strip()
        locations.append(name)
        name_to_index[name] = i

    Q = int(input())
    adj = [[] for _ in range(P)]
    for _ in range(Q):
        parts = input().split()
        u_name, v_name, distance = parts[0], parts[1], int(parts[2])
        u = name_to_index[u_name]
        v = name_to_index[v_name]
        adj[u].append((v, distance))
        adj[v].append((u, distance))

    R = int(input())
    queries = []
    for _ in range(R):
        parts = input().split()
        queries.append((parts[0], parts[1]))

    for start_name, end_name in queries:
        start = name_to_index[start_name]
        end = name_to_index[end_name]
        if start == end:
            print(start_name)
            continue

        # Dijkstra's algorithm
        INF = float('inf')
        dist = [INF] * P
        dist[start] = 0
        prev = [-1] * P
        heap = []
        heapq.heappush(heap, (0, start))

        while heap:
            current_dist, u = heapq.heappop(heap)
            if u == end:
                break
            if current_dist > dist[u]:
                continue
            for (v, distance) in adj[u]:
                if dist[v] > dist[u] + distance:
                    dist[v] = dist[u] + distance
                    prev[v] = u
                    heapq.heappush(heap, (dist[v], v))

        path = []
        current = end
        while current != -1:
            path.append(current)
            current = prev[current]
        path.reverse()

        output = []
        for i in range(len(path)-1):
            u = path[i]
            v = path[i+1]
            distance = None
            for (neighbor, d) in adj[u]:
                if neighbor == v:
                    distance = d
                    break
            output.append(f"{locations[u]}->({distance})")
        output.append(locations[path[-1]])

        print("->".join(output))

solve()