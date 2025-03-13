import sys
import math

# 读取输入
def read_int():
    return map(int, sys.stdin.readline().split())

# 计算两点之间的欧几里得距离
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# 并查集（Disjoint Set）
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            return True
        return False

# Kruskal 算法求最小生成树（MST）
def kruskal_mst(points, P, S):
    edges = []
    
    # 计算所有两点间的距离
    for i in range(P):
        for j in range(i + 1, P):
            edges.append((distance(points[i], points[j]), i, j))
    
    # 按照边权从小到大排序
    edges.sort()
    
    uf = UnionFind(P)
    mst_edges = []  # 存储最小生成树的边
    
    # 遍历所有边，按照 Kruskal 算法选择边构造最小生成树
    for dist, u, v in edges:
        if uf.union(u, v):
            mst_edges.append(dist)
        if len(mst_edges) == P - 1:
            break
    
    # 砍掉 `S-1` 条最长的边，剩下的最大边权即为答案
    mst_edges.sort(reverse=True)  # 降序排序
    return mst_edges[S - 1] if S <= len(mst_edges) else 0

# 主函数
def main():
    T = int(sys.stdin.readline().strip())  # 测试用例个数
    for _ in range(T):
        S, P = read_int()
        points = [tuple(read_int()) for _ in range(P)]  # 读取前哨站坐标
        result = kruskal_mst(points, P, S)
        print(f"{result:.2f}")  # 保留两位小数输出

# 运行主程序
if __name__ == "__main__":
    main()
