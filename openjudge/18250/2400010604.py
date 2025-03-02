class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # 路径压缩
            x = self.parent[x]
        return x

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx == fy:
            return False  # 已经在同一个集合
        if self.size[fx] < self.size[fy]:
            fx, fy = fy, fx  # 确保 fx 是更大的集合
        self.parent[fy] = fx
        self.size[fx] += self.size[fy]
        return True


def process_test_case(n, m, operations):
    dsu = DSU(n)
    for x, y in operations:
        if dsu.find(x) == dsu.find(y):
            print("Yes")
        else:
            dsu.union(x, y)
            print("No")
    # 统计有阔落的杯子
    result = set()
    for i in range(1, n + 1):
        result.add(dsu.find(i))
    print(len(result))
    print(" ".join(map(str, sorted(result))))


def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    while idx < len(data):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        operations = []
        for _ in range(m):
            x = int(data[idx])
            y = int(data[idx + 1])
            operations.append((x, y))
            idx += 2
        process_test_case(n, m, operations)


if __name__ == "__main__":
    main()