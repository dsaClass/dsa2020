from collections import deque
def mintimetocatchcow(N,K):
    if N==K:
        return 0
    # 队列存储的是 (当前位置, 已经花费的时间)
    # 希望记录的是最早的可能到达时间，需要一个列表记录是否已经到达过
    queue = deque([(N, 0)])
    visited = [False] * 100001
    visited[N] = True
    while queue:
        current, time = queue.popleft()
        # 尝试3种移动方式
        for next_pos in [current - 1, current + 1, current * 2]:
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                if next_pos == K:
                    return time + 1
                visited[next_pos] = True
                queue.append((next_pos, time + 1))
N, K = map(int, input().split())
print(mintimetocatchcow(N, K))
