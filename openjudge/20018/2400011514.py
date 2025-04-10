import bisect

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (self.size + 1)  # 1-based indexing
    
    def update(self, index, delta=1):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index
    
    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    v = list(map(int, data[1:n+1]))
    
    # 离散化处理
    sorted_v = sorted(v)
    sorted_unique = []
    prev = None
    for num in sorted_v:
        if num != prev:
            sorted_unique.append(num)
            prev = num
    
    max_rank = len(sorted_unique)
    ranks = [bisect.bisect_left(sorted_unique, x) + 1 for x in v]
    
    fenwick = FenwickTree(max_rank)
    ans = 0
    k = 0  # 已处理元素的数量
    
    for r in reversed(ranks):
        sum_r = fenwick.query(r)
        ans += (k - sum_r)
        fenwick.update(r)
        k += 1
    
    print(ans)

if __name__ == "__main__":
    main()