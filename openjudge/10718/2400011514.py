from collections import deque
import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    t = int(input_data[0])
    index = 1
    results = []
    
    for _ in range(t):
        # 解析每组数据
        if index >= len(input_data):
            break
        parts = input_data[index].split()
        R = int(parts[0])
        C = int(parts[1])
        K = int(parts[2])
        index += 1

        maze = []
        start = None
        end = None
        for i in range(R):
            row = input_data[index].rstrip()
            index += 1
            maze.append(row)
            for j, ch in enumerate(row):
                if ch == 'S':
                    start = (i, j)
                elif ch == 'E':
                    end = (i, j)
        
        # 方向：上，下，左，右
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # 状态：(r, c, t_mod) t_mod为当前时间对K取余
        visited = [[[False] * K for _ in range(C)] for _ in range(R)]
        queue = deque()
        # 初始位置，时间 0
        sr, sc = start
        visited[sr][sc][0] = True
        queue.append((sr, sc, 0, 0))  # (row, col, time, steps)

        found = False
        ans = -1
        
        while queue:
            r, c, t, steps = queue.popleft()
            # 如果当前位置是出口，返回步数
            if (r, c) == end:
                found = True
                ans = steps
                break

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                nt = t + 1
                mod = nt % K
                # 边界判断
                if nr < 0 or nr >= R or nc < 0 or nc >= C:
                    continue
                # 判断该点是否可通行：
                # 当前步到达的时间nt如果是K的倍数，那么可以走石头所在的位置，否则不能走石头
                cell = maze[nr][nc]
                if nt % K != 0 and cell == '#':
                    continue
                # 其他任意情况（'.','S','E','#'）在可以的时刻都可以走
                if not visited[nr][nc][mod]:
                    visited[nr][nc][mod] = True
                    queue.append((nr, nc, nt, steps + 1))
                    
        results.append(str(ans) if found else "Oop!")
    
    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    solve()
