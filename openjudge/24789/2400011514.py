import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    ptr = 0
    n = data[ptr]
    ptr += 1
    m = data[ptr]
    ptr += 1
    edges = []
    sum_v = 0
    for _ in range(m):
        x = data[ptr]
        ptr += 1
        y = data[ptr]
        ptr += 1
        v = data[ptr]
        ptr += 1
        edges.append((v, x, y))
        sum_v += v
    
    edges.sort()
    
    parent = list(range(n))
    rank = [1] * n
    
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    
    count = 0
    min_span_sum = 0
    for edge in edges:
        v, x, y = edge
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
            count += 1
            if count == n - 1:
                break
    
    print(sum_v - min_span_sum)

if __name__ == "__main__":
    main()