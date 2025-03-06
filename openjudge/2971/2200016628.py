from collections import deque

def minTimeToCatchTheCow(N, K):
    queue = deque([(N, 0)])  # (位置, 时间)
    visited = set([N])

    while queue:
        x, time = queue.popleft()
        if x == K:
            return time
        for next_x in [x - 1, x + 1, 2 * x]:
            if 0 <= next_x <= 100000 and next_x not in visited:
                visited.add(next_x)
                queue.append((next_x, time + 1))

N, K = map(int,input().split())
print(minTimeToCatchTheCow(N, K))