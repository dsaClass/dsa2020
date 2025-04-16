import sys
import math

def main():
    sys.setrecursionlimit(1 << 25)
    k, n = map(int, sys.stdin.readline().split())
    max_node = (1 << k) - 1
    L = [0] * (max_node + 1)
    R = [0] * (max_node + 1)
    size = [0] * (max_node + 1)
    
    current_pre = [1]  # 使用列表来传递可变值
    
    def dfs(x):
        L[x] = current_pre[0]
        current_pre[0] += 1
        s = 1
        left = 2 * x
        right = 2 * x + 1
        if left <= max_node:
            dfs(left)
            s += size[left]
        if right <= max_node:
            dfs(right)
            s += size[right]
        size[x] = s
        R[x] = L[x] + s - 1
    
    dfs(1)
    
    class BIT:
        def __init__(self, n_size):
            self.n = n_size
            self.tree = [0] * (self.n + 2)
        
        def update(self, idx, delta):
            while idx <= self.n:
                self.tree[idx] += delta
                idx += idx & -idx
        
        def query(self, idx):
            res = 0
            while idx > 0:
                res += self.tree[idx]
                idx -= idx & -idx
            return res
    
    bit = BIT(max_node)
    sum_ops = [0] * (max_node + 1)
    
    for _ in range(n):
        parts = sys.stdin.readline().split()
        if parts[0] == '1':
            x = int(parts[1])
            y = int(parts[2])
            sum_ops[x] += y
            bit.update(L[x], y * size[x])
        else:
            x = int(parts[1])
            current = x
            sum_ancestors = 0
            while current >= 1:
                sum_ancestors += sum_ops[current]
                current = current // 2
            part1 = sum_ancestors * size[x]
            part2 = bit.query(R[x]) - bit.query(L[x] - 1)
            part2 -= sum_ops[x] * size[x]
            print(part1 + part2)

if __name__ == '__main__':
    main()