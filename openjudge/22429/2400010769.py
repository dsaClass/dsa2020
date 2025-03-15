def main():
    # 输入处理
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]  # 邻接表
    in_degree = [0] * (n + 1)  # 入度数组
    earliest = [0] * (n + 1)  # 最早开始时间
    critical_tasks=[]#关键事件
    tasks=[]#所有事件
    # 建图
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        tasks.append((a,b,c))
        in_degree[b] += 1
    #初始化
    queue = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        u = queue.pop(0)
        for v, c in graph[u]:
            earliest[v] = max(earliest[v], earliest[u] + c)
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    min_time=max(earliest)
    for i in range(1,n+1):
        if earliest[i]==min_time:
            queue.append(i)
    #从取到min_time的点回推
    reverse_graph = [[] for _ in range(n + 1)]  # 反向图
    for a, b, c in tasks:
        reverse_graph[b].append((a, c))  # b -> (a, c) 表示从b到a需要c时间
    while queue:
        b=queue.pop(0)
        for a,c in reverse_graph[b]:
                if earliest[b]==earliest[a]+c:
                    queue.append(a)
                    if (a,b) not in critical_tasks:
                        critical_tasks.append((a,b))
    print(min_time)
    # 按字典序输出
    critical_tasks.sort()
    for task in critical_tasks:
        print(task[0], task[1])

if __name__ == "__main__":
    main()
