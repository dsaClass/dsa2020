n = int(input())
tickets = []
for i in range(n):
    tickets.append(list(map(int, input().split())))
if n ==2:
    print(min(tickets[0][1], tickets[1][0]))
else:
    dp = [[[float('inf'),[0]] for _ in range(n)] for _ in range(n-1)]
    for k in range(1,n-1):
        dp[0][k][0] = tickets[0][k]
        dp[0][k][1].append(k)
    for i in range(0,n-2):
        for j in range(1,n-1):
            out = dp[i][j][1][:]
            for k in [x for x in range(n-1) if x not in out] :
                if tickets[j][k] + dp[i][j][0] < dp[i+1][k][0]:
                    dp[i+1][k][0] = tickets[j][k] + dp[i][j][0]
                    dp[i+1][k][1] = out[:]
                    dp[i+1][k][1].append(k)
    for j in range(0,n):
        dp[n-2][n-1][0] =min(dp[n-2][n-1][0], dp[n-3][j][0]+tickets[j][n-1])

    print(dp[n-2][n-1][0])