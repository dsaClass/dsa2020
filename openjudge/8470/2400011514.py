def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        n = int(input[idx])
        idx += 1
        original = []
        for _ in range(n):
            original.append(input[idx].strip())
            idx += 1
        
        # 去重
        seen = set()
        unique_list = []
        for s in original:
            if s not in seen:
                seen.add(s)
                unique_list.append(s)
        original = unique_list
        
        # 过滤被其他不同片段包含的片段
        nodes = []
        for s in original:
            redundant = False
            for t in original:
                if s != t and s in t:
                    redundant = True
                    break
            if not redundant:
                nodes.append(s)
        M = len(nodes)
        if M == 0:
            print(0)
            continue
        
        # 计算重叠矩阵
        def compute_overlap(a, b):
            max_k = min(len(a), len(b))
            for k in range(max_k, 0, -1):
                if a.endswith(b[:k]):
                    return k
            return 0
        
        overlap = [[0] * M for _ in range(M)]
        for i in range(M):
            for j in range(M):
                if i != j:
                    overlap[i][j] = compute_overlap(nodes[i], nodes[j])
        
        # 初始化动态规划表
        INF = float('-inf')
        dp = [[INF] * M for _ in range(1 << M)]
        for i in range(M):
            mask = 1 << i
            dp[mask][i] = 0
        
        # 动态规划转移
        for mask in range(1 << M):
            for i in range(M):
                if not (mask & (1 << i)):
                    continue
                current = dp[mask][i]
                if current == INF:
                    continue
                for j in range(M):
                    if j == i:
                        continue
                    if not (mask & (1 << j)):
                        new_mask = mask | (1 << j)
                        new_saving = current + overlap[i][j]
                        if new_saving > dp[new_mask][j]:
                            dp[new_mask][j] = new_saving
        
        # 计算最大节省量
        full_mask = (1 << M) - 1
        max_saving = max(dp[full_mask][i] for i in range(M))
        sum_length = sum(len(node) for node in nodes)
        shortest = sum_length - max_saving
        print(shortest)

if __name__ == "__main__":
    main()