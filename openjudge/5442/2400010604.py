class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
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
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    min_cost = 0
    for u, v, weight in edges:
        if uf.union(u, v):
            min_cost += weight
    return min_cost

def main():
    n = int(input())
    edges = []
    for _ in range(n-1):
        line = input().split()
        u = ord(line[0]) - ord('A')
        k = int(line[1])
        for i in range(k):
            v = ord(line[2 + 2*i]) - ord('A')
            weight = int(line[3 + 2*i])
            edges.append((u, v, weight))
    print(kruskal(n, edges))

if __name__ == "__main__":
    main()