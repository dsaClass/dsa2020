from collections import deque


def topological_sort(n, children):
    # 构建邻接表和入度数组
    graph = [[] for _ in range(n + 1)]  # graph[i] 存储i的子节点列表
    in_degree = [0] * (n + 1)  # in_degree[j] 表示j的入度（有多少父节点指向j）

    for i in range(1, n + 1):
        for child in children[i]:
            graph[i].append(child)
            in_degree[child] += 1

    # 初始化队列：入度为0的节点先发言
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    result = []
    while queue:
        parent = queue.popleft()  # 取出当前发言的节点（父节点）
        result.append(parent)
        # 处理父节点的所有子节点，更新入度
        for child in graph[parent]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)  # 子节点入度为0时，可加入队列

    return result


def main():
    n = int(input())
    children = [[] for _ in range(n + 1)]  # children[i] 存储i的子女列表（不含0）

    for i in range(1, n + 1):
        line = list(map(int, input().split()))
        for x in line:
            if x == 0:
                break  # 遇到0终止，不加入子女列表
            children[i].append(x)

    order = topological_sort(n, children)
    print(*order)  # 输出结果，自动用空格分隔


if __name__ == "__main__":
    main()