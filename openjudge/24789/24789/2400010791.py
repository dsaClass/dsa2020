import sys
from sys import stdin


def main():
    n, m = map(int, stdin.readline().split())
    sum_v = 0
    edges = []

    for _ in range(m):
        x, y, v = map(int, stdin.readline().split())
        sum_v += v
        edges.append((v, x, y))

    edges.sort()

    parent = list(range(n))
    rank = [1] * n

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    min_span_sum = 0
    for v, x, y in edges:
        rx = find(x)
        ry = find(y)
        if rx != ry:
            if rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[rx] = ry
                if rank[rx] == rank[ry]:
                    rank[ry] += 1
            min_span_sum += v

    print(sum_v - min_span_sum)


if __name__ == "__main__":
    main()