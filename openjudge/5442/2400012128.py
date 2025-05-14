import sys

# 读取输入
n = int(input())
# 初始化邻接矩阵
graph = [[sys.maxsize] * n for _ in range(n)]

for _ in range(n - 1):
    line = input().split()
    start = ord(line[0]) - ord('A')
    edge_count = int(line[1])
    for i in range(edge_count):
        end = ord(line[2 + 2 * i]) - ord('A')
        weight = int(line[3 + 2 * i])
        graph[start][end] = weight
        graph[end][start] = weight

# Prim 算法实现
def prim(graph, n):
    # 记录顶点是否已加入最小生成树
    visited = [False] * n
    # 记录每个顶点到最小生成树的最小权值
    key = [sys.maxsize] * n
    # 从顶点 0 开始
    key[0] = 0
    result = 0

    for _ in range(n):
        # 选择距离最小生成树最近的顶点
        min_key = sys.maxsize
        min_index = -1
        for v in range(n):
            if not visited[v] and key[v] < min_key:
                min_key = key[v]
                min_index = v

        # 将该顶点加入最小生成树
        visited[min_index] = True
        result += min_key

        # 更新与该顶点相邻的顶点的最小权值
        for v in range(n):
            if not visited[v] and graph[min_index][v] < key[v]:
                key[v] = graph[min_index][v]

    return result

# 计算最小权值和
min_weight_sum = prim(graph, n)
print(min_weight_sum)