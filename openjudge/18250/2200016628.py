import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return True  # 已经在同一个集合
        self.parent[rootY] = rootX  # 把y集合并到x集合
        return False


while True:
    try:
        line = sys.stdin.readline()
        if not line:
            break
        n, m = map(int, line.strip().split())
        uf = UnionFind(n)
        for _ in range(m):
            x, y = map(int, sys.stdin.readline().strip().split())
            if uf.union(x, y):
                print("Yes")
            else:
                print("No")
        # 最后统计有哪些集合代表仍然是自己的（即这些位置有“饮料”）
        result = set()
        for i in range(1, n + 1):
            result.add(uf.find(i))
        print(len(result))
        print(' '.join(map(str, sorted(result))))
    except:
        break