def get_candidates(board, row, col):
    candidates = set(range(1, 10))
    # 移除所在行已有的数字
    for i in range(9):
        if board[row][i] in candidates:
            candidates.remove(board[row][i])
    # 移除所在列已有的数字
    for i in range(9):
        if board[i][col] in candidates:
            candidates.remove(board[i][col])
    # 移除所在 3x3 子方格已有的数字
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] in candidates:
                candidates.remove(board[i][j])
    return candidates

def find_empty_cell(board):
    min_candidates = 10
    best_row, best_col = -1, -1
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                candidates = get_candidates(board, row, col)
                if len(candidates) < min_candidates:
                    min_candidates = len(candidates)
                    best_row, best_col = row, col
    return best_row, best_col

def solve_sudoku(board):
    row, col = find_empty_cell(board)
    if row == -1:  # 没有空白位置，说明数独已解
        return True
    candidates = get_candidates(board, row, col)
    for num in candidates:
        board[row][col] = num
        if solve_sudoku(board):
            return True
        board[row][col] = 0
    return False

T = int(input())
for _ in range(T):
    board = []
    for _ in range(9):
        row = list(map(int, input()))
        board.append(row)
    if solve_sudoku(board):
        for row in board:
            print(''.join(map(str, row)))
    else:
        print("No solution exists.")