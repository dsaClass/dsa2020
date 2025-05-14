import heapq
import math

def readints():
    import sys
    return list(map(int, sys.stdin.readline().split()))

def main():
    # Read home and school coordinates
    home_x, home_y, school_x, school_y = map(int, input().split())
    
    subway_lines = []
    # Read subway lines until EOF
    while True:
        try:
            line = list(map(int, input().split()))
            stops = []
            for i in range(0, len(line), 2):
                x, y = line[i], line[i+1]
                if x == -1 and y == -1:
                    break
                stops.append((x, y))
            if stops:
                subway_lines.append(stops)
        except EOFError:
            break
    
    # All points: home, school, and all subway stops
    points = [(home_x, home_y), (school_x, school_y)]
    for line in subway_lines:
        for stop in line:
            points.append(stop)
    # Remove duplicates by converting to a set then back to list
    unique_points = list(dict.fromkeys(points))
    points = unique_points
    n = len(points)
    
    # Create a mapping from point to index
    point_to_index = {point: i for i, point in enumerate(points)}
    
    # Initialize adjacency list
    adj = [[] for _ in range(n)]
    
    # Add edges for subway lines (adjacent stops only)
    for line in subway_lines:
        for i in range(len(line) - 1):
            a = line[i]
            b = line[i+1]
            idx_a = point_to_index[a]
            idx_b = point_to_index[b]
            dx = a[0] - b[0]
            dy = a[1] - b[1]
            distance = math.sqrt(dx*dx + dy*dy)
            time = distance / (40000.0 / 60.0)  # 40 km/h -> m/min (40000 m per hour, 60 min)
            adj[idx_a].append((idx_b, time))
            adj[idx_b].append((idx_a, time))
    
    # Add walking edges between all pairs of points
    for i in range(n):
        for j in range(i+1, n):
            a = points[i]
            b = points[j]
            dx = a[0] - b[0]
            dy = a[1] - b[1]
            distance = math.sqrt(dx*dx + dy*dy)
            time = distance / (10000.0 / 60.0)  # 10 km/h -> m/min (10000 m per hour, 60 min)
            adj[i].append((j, time))
            adj[j].append((i, time))
    
    # Dijkstra's algorithm
    start = point_to_index[(home_x, home_y)]
    end = point_to_index[(school_x, school_y)]
    
    INF = float('inf')
    dist = [INF] * n
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    
    while heap:
        current_dist, u = heapq.heappop(heap)
        if u == end:
            break
        if current_dist > dist[u]:
            continue
        for (v, time) in adj[u]:
            if dist[v] > dist[u] + time:
                dist[v] = dist[u] + time
                heapq.heappush(heap, (dist[v], v))
    
    print(round(dist[end]))

if __name__ == '__main__':
    main()