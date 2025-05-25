class DLXNode:
    def __init__(self):
        self.L = self.R = self.U = self.D = self.C = None
        self.rowID = -1
        self.colID = -1
        self.size = 0

class DLX:
    def __init__(self, m):
        self.header = DLXNode()
        self.m = m  # 列数
        self.columns = [DLXNode() for _ in range(m)]
        # 初始化列头节点环形链表
        last = self.header
        for i, col in enumerate(self.columns):
            col.C = col
            col.colID = i
            col.U = col.D = col
            col.size = 0
            last.R = col
            col.L = last
            last = col
        last.R = self.header
        self.header.L = last
        self.nodes = []
        self.ans = []
        self.row_nodes = []

    def add_row(self, row_id, cols):
        first = None
        last = None
        for c in cols:
            node = DLXNode()
            node.rowID = row_id
            node.colID = c
            col = self.columns[c]

            # 垂直插入节点
            node.U = col.U
            node.D = col
            col.U.D = node
            col.U = node
            node.C = col
            col.size += 1

            # 水平连接
            if first is None:
                first = node
            else:
                last.R = node
                node.L = last
            last = node

        # 形成环形水平链
        if first and last:
            first.L = last
            last.R = first
        self.nodes.append(first)
        self.row_nodes.append(first)

    def cover(self, col):
        col.R.L = col.L
        col.L.R = col.R
        i = col.D
        while i != col:
            j = i.R
            while j != i:
                j.D.U = j.U
                j.U.D = j.D
                j.C.size -= 1
                j = j.R
            i = i.D

    def uncover(self, col):
        i = col.U
        while i != col:
            j = i.L
            while j != i:
                j.C.size += 1
                j.D.U = j
                j.U.D = j
                j = j.L
            i = i.U
        col.R.L = col
        col.L.R = col

    def search(self, k=0):
        if self.header.R == self.header:
            return True
        # 选最小列（启发式）
        c = self.header.R
        min_size = c.size
        col = c
        while c != self.header:
            if c.size < min_size:
                min_size = c.size
                col = c
            c = c.R
        if col.size == 0:
            return False

        self.cover(col)
        r = col.D
        while r != col:
            self.ans.append(r)
            j = r.R
            while j != r:
                self.cover(j.C)
                j = j.R
            if self.search(k+1):
                return True
            j = r.L
            while j != r:
                self.uncover(j.C)
                j = j.L
            self.ans.pop()
            r = r.D
        self.uncover(col)
        return False

def sudoku_exact_cover(board):
    def get_box_num(r, c):
        return (r // 3) * 3 + (c // 3)

    # 324列：
    # 0~80: cell constraints (cell)
    # 81~161: row constraints (row+num)
    # 162~242: col constraints (col+num)
    # 243~323: box constraints (box+num)

    dlx = DLX(324)
    row_mapping = []

    for r in range(9):
        for c in range(9):
            for num in range(1, 10):
                if board[r][c] != 0 and board[r][c] != num:
                    continue
                row_id = len(row_mapping)
                row_mapping.append((r, c, num))
                cols = [
                    r * 9 + c,                            # cell constraint
                    81 + r * 9 + (num - 1),              # row constraint
                    162 + c * 9 + (num - 1),             # col constraint
                    243 + get_box_num(r, c) * 9 + (num - 1)  # box constraint
                ]
                dlx.add_row(row_id, cols)

    dlx.search()

    result = [[0]*9 for _ in range(9)]
    for node in dlx.ans:
        r, c, num = row_mapping[node.rowID]
        result[r][c] = num
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    t = int(data[0])
    idx = 1
    for _ in range(t):
        board = [list(map(int, list(data[idx + i]))) for i in range(9)]
        idx += 9
        ans = sudoku_exact_cover(board)
        for row in ans:
            print(''.join(map(str, row)))

if __name__ == "__main__":
    main()