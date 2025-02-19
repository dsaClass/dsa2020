import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # 路径压缩
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # 按边权值排序
    uf = UnionFind(n)
    mst_weight = 0
    for u, v, w in edges:
        if uf.union(u, v):
            mst_weight += w
    return mst_weight

def main():
    n = int(sys.stdin.readline().strip())
    edges = []
    
    for _ in range(n - 1):
        line = sys.stdin.readline().strip().split()
        u = ord(line[0]) - ord('A')  # 将字母映射到索引
        k = int(line[1])
        for i in range(k):
            v = ord(line[2 + 2 * i]) - ord('A')
            w = int(line[3 + 2 * i])
            edges.append((u, v, w))
    
    print(kruskal(n, edges))

if __name__ == "__main__":
    main()
