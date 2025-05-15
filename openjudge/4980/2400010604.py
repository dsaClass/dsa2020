import heapq

def solve():
    S = int(input())
    for _ in range(S):
        N, M = map(int, input().split())
        grid = []
        start = None
        end = None
        for i in range(N):
            line = input().strip()
            grid.append(line)
            if 'r' in line:
                start = (i, line.index('r'))
            if 'a' in line:
                end = (i, line.index('a'))
        
        if not start or not end:
            print("Impossible")
            continue
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[float('inf')] * M for _ in range(N)]
        heap = []
        heapq.heappush(heap, (0, start[0], start[1]))
        visited[start[0]][start[1]] = 0
        found = False
        result = 0
        
        while heap:
            time, x, y = heapq.heappop(heap)
            if (x, y) == end:
                found = True
                result = time
                break
            if time > visited[x][y]:
                continue
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if grid[nx][ny] == '#':
                        continue
                    new_time = time + 1
                    if grid[nx][ny] == 'x':
                        new_time += 1
                    if new_time < visited[nx][ny]:
                        visited[nx][ny] = new_time
                        heapq.heappush(heap, (new_time, nx, ny))
        
        print(result if found else "Impossible")

solve()