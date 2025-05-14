def dfs(row, count, n, k, board, col_used):
    if count == k:
        return 1  # 成功放置了 k 个棋子
    if row >= n:
        return 0  # 行数越界，回溯
    total = 0
    for j in range(n):
        if board[row][j] == '#' and not col_used[j]:
            col_used[j] = True
            total += dfs(row + 1, count + 1, n, k, board, col_used)
            col_used[j] = False  # 回溯
    # 也可以不在当前行放棋子，直接跳到下一行
    total += dfs(row + 1, count, n, k, board, col_used)
    return total

def main():
    while True:
        line = input()
        if not line:
            continue
        n_k = line.strip()
        if n_k == "-1 -1":
            break
        n, k = map(int, n_k.split())
        board = [input().strip() for _ in range(n)]
        col_used = [False] * n
        result = dfs(0, 0, n, k, board, col_used)
        print(result)

if __name__ == "__main__":
    main()