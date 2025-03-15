import sys

def main():
    while True:
        line = sys.stdin.readline()
        while line.strip() == '':
            line = sys.stdin.readline()
        nk = line.strip().split()
        n, k = map(int, nk)
        if n == -1 and k == -1:
            break
        
        rows = []
        for _ in range(n):
            s = sys.stdin.readline().strip()
            row_cols = [i for i, c in enumerate(s) if c == '#']
            rows.append(row_cols)
        
        max_mask = 1 << n
        dp = [[0] * (k + 1) for _ in range(max_mask)]
        dp[0][0] = 1
        
        for i in range(n):
            new_dp = [[0] * (k + 1) for _ in range(max_mask)]
            for mask in range(max_mask):
                for cnt in range(k + 1):
                    if dp[mask][cnt] == 0:
                        continue
                    new_dp[mask][cnt] += dp[mask][cnt]
                    if cnt < k:
                        for col in rows[i]:
                            if not (mask & (1 << col)):
                                new_mask = mask | (1 << col)
                                new_cnt = cnt + 1
                                new_dp[new_mask][new_cnt] += dp[mask][cnt]
            dp = new_dp
        
        total = 0
        for mask in range(max_mask):
            total += dp[mask][k]
        print(total)

if __name__ == '__main__':
    main()
