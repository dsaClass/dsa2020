from collections import deque
def min_prize(n, m, matches):
    graph = [[] for _ in range(n)]
    indegree = [0] * n
    for a, b in matches:
        graph[b].append(a)
        indegree[a] += 1
    prize = [100] * n
    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        team = queue.popleft()
        for oppo in graph[team]:
            # 根据胜负关系调整奖金
            prize[oppo] = max(prize[oppo], prize[team] + 1)
            indegree[oppo]-=1
            if indegree[oppo]==0:
                queue.append(oppo)
    return sum(prize)
n,m=map(int,input().split())
matches=[tuple(map(int,input().split()))for _ in range(m)]
print(min_prize(n, m, matches))
