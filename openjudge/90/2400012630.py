def main() :
    R,C=map(int,input().split())
    matrix=[]
    for _ in range(R) :
        row=list(map(int,input().split()))
        matrix.append(row)

    dx=[1,0,-1,0]
    dy=[0,1,0,-1]

    points=[]
    for i in range(R) :
        for j in range(C) :
            points.append((matrix[i][j],i,j))
    points.sort()

    dp=[[1]*C for _ in range(R)]
    max_len=1

    for h,x,y in points :
        for i in range(4) :
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<R and 0<=ny<C and matrix[nx][ny]<h :
                dp[x][y]=max(dp[x][y],dp[nx][ny]+1)
                max_len=max(max_len,dp[x][y])

    print(max_len)

if __name__=="__main__" :
    main()