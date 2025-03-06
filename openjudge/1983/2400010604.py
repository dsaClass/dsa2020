def solve_sudoku():
    def is_valid(row, col, num):
        return not (rows[row] & (1 << num)) and not (cols[col] & (1 << num)) and not (boxes[box_index(row, col)] & (1 << num))

    def place_number(row, col, num):
        rows[row] |= (1 << num)
        cols[col] |= (1 << num)
        boxes[box_index(row, col)] |= (1 << num)
        board[row][col] = num

    def remove_number(row, col, num):
        rows[row] ^= (1 << num)
        cols[col] ^= (1 << num)
        boxes[box_index(row, col)] ^= (1 << num)
        board[row][col] = 0

    def box_index(row, col):
        return (row // 3) * 3 + col // 3

    def find_empty():
        min_choices = float('inf')
        best_pos = None
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    choices = 0
                    for num in range(1, 10):
                        if is_valid(i, j, num):
                            choices += 1
                    if choices < min_choices:
                        min_choices = choices
                        best_pos = (i, j)
        return best_pos

    def backtrack():
        pos = find_empty()
        if not pos:
            return True  # 所有格子都填满
        row, col = pos

        for num in range(1, 10):
            if is_valid(row, col, num):
                place_number(row, col, num)
                if backtrack():
                    return True
                remove_number(row, col, num)
        return False

    # 初始化全局变量
    global rows, cols, boxes, board
    rows = [0] * 9
    cols = [0] * 9
    boxes = [0] * 9
    board = [[0] * 9 for _ in range(9)]

    # 读取输入并初始化
    for i in range(9):
        for j in range(9):
            num = int(input_data[i][j])
            if num != 0:
                place_number(i, j, num)

    # 开始回溯求解
    backtrack()

    # 输出结果
    for row in board:
        print(''.join(map(str, row)))


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])  # 测试用例数量
    index = 1

    for _ in range(t):
        global input_data
        input_data = [data[index + i] for i in range(9)]
        index += 9
        solve_sudoku()


if __name__ == "__main__":
    main()