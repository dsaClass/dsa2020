class Solution:
    def solveQueens(self, N):
        result = []
        self.backtrack(N, 0, [], set(), set(), set(), result)
        return result

    def backtrack(self, N, row, state, cols, diag1, diag2, result):
        if row == N:
            result.append(state[:])  
            return
        for col in range(N):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            # 放置皇后
            state.append(col)
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            self.backtrack(N, row + 1, state, cols, diag1, diag2, result)

            # 撤销
            state.pop()
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

S = Solution()
N = int(input())
result = S.solveQueens(N)
if result:
    result.sort()  # 排序
    for solution in result:
        print(" ".join(map(str, solution)))
else:
    print("NO ANSWER")