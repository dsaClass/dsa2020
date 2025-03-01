import sys
import heapq


def main():
    N, M = map(int, sys.stdin.readline().split())
    defeat_time = [0] * (N + 2)  # 0和1不需要击败时间
    for i in range(2, N + 2):
        defeat_time[i] = int(sys.stdin.readline())

    # 构建图
    graph = [[] for _ in range(N + 2)]
    for _ in range(M):
        u, v, t = map(int, sys.stdin.readline().split())
        graph[u].append((v, t))
        graph[v].append((u, t))

    # Dijkstra算法
    dist = [float('inf')] * (N + 2)
    dist[0] = 0
    heap = [(0, 0)]
    visited = set()

    while heap:
        current_dist, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)

        for v, t in graph[u]:
            if v not in visited:
                # 通过这条路的时间 + 通过隘口的击败时间（如果还未击败）
                new_dist = current_dist + t + (defeat_time[v] if v not in visited else 0)
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))

    print(dist[1])


if __name__ == "__main__":
    main()