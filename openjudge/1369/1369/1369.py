import heapq  # 用于实现字典序最小的拓扑排序

def topological_sort(n, children):
    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    for i in range(1, n + 1):
        for child in children[i]:
            graph[i].append(child)
            in_degree[child] += 1

    # 使用小根堆确保字典序最小（如果不需要则可以用 queue 替代）
    heap = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            heapq.heappush(heap, i)

    result = []
    while heap:
        u = heapq.heappop(heap)
        result.append(u)
        for v in sorted(graph[u]):  # 如果字典序不重要，可以不排序
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heapq.heappush(heap, v)

    return result

# 主函数部分
def main():
    n = int(input())
    children = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        line = list(map(int, input().split()))
        for x in line:
            if x == 0:
                break
            children[i].append(x)

    order = topological_sort(n, children)
    print(*order)

if __name__ == "__main__":
    main()