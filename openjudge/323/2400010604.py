def solve():
    while True:
        n, k = map(int, input().split())
        if n == -1 and k == -1:
            break
        board = []
        for _ in range(n):
            board.append(input().strip())
        
        count = 0
        cols = [False] * n
        
        def backtrack(row, placed):
            nonlocal count
            if placed == k:
                count += 1
                return
            if row == n:
                return
            # Option 1: 不在该行放置棋子
            backtrack(row + 1, placed)
            # Option 2: 尝试在该行放置棋子
            for col in range(n):
                if board[row][col] == '#' and not cols[col]:
                    cols[col] = True
                    backtrack(row + 1, placed + 1)
                    cols[col] = False
        
        backtrack(0, 0)
        print(count)

solve()