import heapq

def minimal_steps(n, m):
    if n == m:
        return 0, ""
    
    visited = {n: ""}  # 记录到达每个位置的最小字典序路径
    heap = []
    heapq.heappush(heap, (0, n, ""))  # (步数, 当前位置, 路径)
    
    while heap:
        steps, pos, path = heapq.heappop(heap)
        
        if pos == m:
            return steps, path
        
        # 优先尝试H（乘法），因为H字典序更小
        next_h = pos * 3
        new_path_h = path + 'H'
        if next_h not in visited or len(new_path_h) < len(visited[next_h]) or (len(new_path_h) == len(visited[next_h]) and new_path_h < visited[next_h]):
            visited[next_h] = new_path_h
            heapq.heappush(heap, (steps + 1, next_h, new_path_h))
        
        # 尝试O（除法）
        next_o = pos // 2
        new_path_o = path + 'O'
        if next_o not in visited or len(new_path_o) < len(visited[next_o]) or (len(new_path_o) == len(visited[next_o]) and new_path_o < visited[next_o]):
            visited[next_o] = new_path_o
            heapq.heappush(heap, (steps + 1, next_o, new_path_o))
    
    return -1, ""  # 题目保证有解，不会执行到这行

# 处理输入输出
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n, m = map(int, line.split())
    if n == 0 and m == 0:
        break
    steps, path = minimal_steps(n, m)
    print(steps)
    print(path)