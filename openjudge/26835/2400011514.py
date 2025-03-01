class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return False
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        else:
            self.parent[yroot] = xroot
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1
        return True

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # 按权重排序
    dsu = DSU(n)
    mst = []
    total_cost = 0.0

    for s, e, w in edges:
        if dsu.union(s, e):
            mst.append((s, e, w))
            total_cost += w
            if len(mst) == n - 1:
                break

    if len(mst) != n - 1:
        return "NOT CONNECTED", []

    return total_cost, mst

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        s, e, w = input().split()
        edges.append((int(s), int(e), float(w)))

    total_cost, mst = kruskal(n, edges)

    if total_cost == "NOT CONNECTED":
        print("NOT CONNECTED")
    else:
        print("{:.2f}".format(total_cost))
        for s, e, _ in sorted(mst, key=lambda x: x[2]):
            print(min(s, e), max(s, e))

if __name__ == "__main__":
    main()