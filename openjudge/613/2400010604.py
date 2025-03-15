class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # 路径压缩
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        if self.size[xroot] < self.size[yroot]:
            xroot, yroot = yroot, xroot
        self.parent[yroot] = xroot
        self.size[xroot] += self.size[yroot]

def find_suspects(n, m, groups):
    dsu = DSU(n)
    for group in groups:
        for i in range(1, len(group)):
            dsu.union(group[0], group[i])
    suspect_root = dsu.find(0)
    return dsu.size[suspect_root]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    while True:
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        if n == 0 and m == 0:
            break
        groups = []
        for _ in range(m):
            k = int(data[idx])
            group = list(map(int, data[idx+1:idx+1+k]))
            groups.append(group)
            idx += 1 + k
        print(find_suspects(n, m, groups))

if __name__ == "__main__":
    main()