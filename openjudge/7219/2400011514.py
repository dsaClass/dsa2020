def count_k_partitions(n, k):
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = 1
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            if j >= i:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - i]
    return dp[k][n]

def count_distinct_partitions(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(n, i - 1, -1):
            dp[j] += dp[j - i]
    return dp[n]

def count_odd_partitions(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1, 2):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
    return dp[n]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    while idx < len(data):
        N = int(data[idx])
        K = int(data[idx + 1])
        idx += 2
        
        # 第一行: N划分成K个正整数之和的划分数目
        k_partitions = count_k_partitions(N, K)
        
        # 第二行: N划分成若干个不同正整数之和的划分数目
        distinct_partitions = count_distinct_partitions(N)
        
        # 第三行: N划分成若干个奇正整数之和的划分数目
        odd_partitions = count_odd_partitions(N)
        
        print(k_partitions)
        print(distinct_partitions)
        print(odd_partitions)

if __name__ == "__main__":
    main()