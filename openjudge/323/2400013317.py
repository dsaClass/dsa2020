def f(n,k,matrix):
    colused=0
    def g(row,colused,placed):
    #一行一行遍历，row用来标记遍历到哪一行了，colused用来标记哪些列用过了，placed用来计放置的棋子数
        count=0
        if placed==k: #如果放完棋子了，就返回1个方案
            return 1
        if row>=n: #如果所有行都遍历完，棋子还没放完，那就说明当前状况已经不成立了
            return 0
        count+=g(row+1,colused,placed) #如果这一行不放棋子，有多少种方案
        for col in range(n): #遍历这一行，枚举出棋子放在每个位置的方案数
            if matrix[row][col]=='#' and not colused & (1<<col):
            #如果矩阵这个位置是棋盘区域，并且这一行还没放过
            #colused是一个二进制数，共n位，从个位开始第i位是0表示这一行没放过，是1表示放过棋子了
            #(1<<col)就是把1左移col位，刚好移到标记第col行的位置
                count+=g(row+1,colused | (1<<col),placed+1)
        return count
    return g(0,0,0)
while True:
    n,k=map(int,input().split())
    if n==-1 and k==-1:
        break
    matrix=[]
    for _ in range(n):
        matrix.append(input())
    print(f(n,k,matrix))
