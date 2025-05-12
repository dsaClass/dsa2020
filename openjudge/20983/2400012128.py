n = int(input().strip())
board = [[0]*(n+1) for _ in range(n+1)]
board[1][1] = 1
for i in range(2,n+1):
    board[i][1] = 1
for m in range(2,n+1):
    for k in range(2,n+1):
        if m-k>=0:
            board[m][k] = board[m-k][k] + board[m-1][k-1]
        else:
            board[m][k] = 0

ans = 0
for i in range(1,n+1):
    ans += board[n][i]

print(ans)