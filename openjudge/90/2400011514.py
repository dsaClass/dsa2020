import sys
sys.setrecursionlimit(1000000)

def main():
    R, C = map(int, sys.stdin.readline().split())
    h = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
    dp = [[0] * C for _ in range(R)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右
    
    def dfs(i, j):
        if dp[i][j] != 0:
            return dp[i][j]
        max_len = 1
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < R and 0 <= nj < C and h[ni][nj] < h[i][j]:
                current_len = dfs(ni, nj) + 1
                if current_len > max_len:
                    max_len = current_len
        dp[i][j] = max_len
        return max_len
    
    max_length = 0
    for i in range(R):
        for j in range(C):
            current = dfs(i, j)
            if current > max_length:
                max_length = current
    print(max_length)

if __name__ == "__main__":
    main()