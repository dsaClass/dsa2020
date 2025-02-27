def count_squares(matrix):
    m=len(matrix)
    n=len(matrix[0])
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]


    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    #通过相邻前面几个的dp值推断此处dp
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    return sum([sum([dp[i][j] for j in range(n)]) for i in range(m)])

m,n=map(int,input().split())
matrix=[]
for _ in range(m):
    matrix.append(list(str(input())))



result = count_squares(matrix)
print(result)
