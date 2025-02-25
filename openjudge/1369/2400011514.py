from collections import defaultdict, deque

def topological_sort(n, children):
    # 构建图和计算入度
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for child in children[i]:
            graph[i].append(child)
            in_degree[child] += 1
    
    # 初始化队列，将所有入度为0的节点加入队列
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    # 进行拓扑排序
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for child in graph[node]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)
    
    return result

# 输入处理
n = int(input())
children = defaultdict(list)
for i in range(1, n + 1):
    children[i] = list(map(int, input().split()))[:-1]

# 执行拓扑排序
order = topological_sort(n, children)

# 输出结果
print(" ".join(map(str, order)))