def Maze(M,start):
    stack = [start]#利用栈来存储走过的路线
    m = len(M)
    n = len(M[0])
    while stack:
        now = stack[-1]
        i,j = now
        if i==m-1 and j==n-1:
            return'1'

        M[i][j] = "#"#标记走过了!!!不走回头路
        back = True
        for x,y in (i-1,j),(i+1,j),(i,j+1),(i,j-1):
            if 0 <= x <= m-1 and 0 <= y <= n-1:
                if M[x][y] != '#':
                    stack.append((x,y))
                    back = False
                    break
        if back:
            stack.pop()#一直回到上一个可选节点
            continue
    else:
        return '0'
m,n = tuple(map(int,input().split()))
M = [list(input()) for i in range(m)]
print(Maze(M,(0,0)))