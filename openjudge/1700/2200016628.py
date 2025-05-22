class Solution:
    def solveNQueens(self, n):
        result = []
        chessboard = ['.' * n for _ in range(n)]
        self.backtracking(n, 0, chessboard, result)
        return result

    def backtracking(self, n, col, chessboard, result):
        if col == n:
            result.append(chessboard[:])
            return

        for row in range(n):
            if self.isValid(row, col, chessboard):
                chessboard[row] = chessboard[row][:col] + 'Q' + chessboard[row][col+1:]
                self.backtracking(n, col + 1, chessboard, result)
                chessboard[row] = chessboard[row][:col] + '.' + chessboard[row][col+1:]

    def isValid(self, row, col, chessboard):
        # 检查该行是否已有皇后
        for j in range(col):
            if chessboard[row][j] == 'Q':
                return False
        # 检查左上对角线
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # 检查左下对角线
        i, j = row + 1, col - 1
        while i < len(chessboard) and j >= 0:
            if chessboard[i][j] == 'Q':
                return False
            i += 1
            j -= 1
        return True

# 执行并格式化输出
s = Solution()
solutions = s.solveNQueens(8)

for idx, solution in enumerate(solutions, 1):
    print(f"No. {idx}")
    for row in solution:
        print(' '.join(['1' if ch == 'Q' else '0' for ch in row]))
