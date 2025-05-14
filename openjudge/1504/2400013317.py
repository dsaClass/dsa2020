import math
import heapq

def solve():
    home_x, home_y, school_x, school_y = map(int, input().split())
    subway_lines = []
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
    
    subway_stops = []
    for line in subway_lines:
        subway_stops.extend(line)
    all_stops = [(home_x, home_y), (school_x, school_y)] + subway_stops
    stop_indices = {stop: idx for idx, stop in enumerate(all_stops)}
    num_stops = len(all_stops)
    
    adj = [[] for _ in range(num_stops)]
    walk_speed = 10000 / 60
    subway_speed = 40000 / 60
    
    for i in range(num_stops):
        for j in range(i + 1, num_stops):
            x1, y1 = all_stops[i]
            x2, y2 = all_stops[j]
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            time = distance / walk_speed
            adj[i].append((j, time))
            adj[j].append((i, time))
    
    for line in subway_lines:
        for i in range(len(line) - 1):
            stop1 = line[i]
            stop2 = line[i+1]
            idx1 = stop_indices[stop1]
            idx2 = stop_indices[stop2]
            x1, y1 = stop1
            x2, y2 = stop2
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            time = distance / subway_speed
            adj[idx1].append((idx2, time))
            adj[idx2].append((idx1, time))
    
    home_idx = stop_indices[(home_x, home_y)]
    school_idx = stop_indices[(school_x, school_y)]
    min_time = [float('inf')] * num_stops
    min_time[home_idx] = 0
    heap = []
    heapq.heappush(heap, (0, home_idx))
    
    while heap:
        current_time, u = heapq.heappop(heap)
        if u == school_idx:
            break
        if current_time > min_time[u]:
            continue
        for v, time in adj[u]:
            if min_time[v] > current_time + time:
                min_time[v] = current_time + time
                heapq.heappush(heap, (min_time[v], v))
    
    total_time = min_time[school_idx]
    print(round(total_time))

solve()
