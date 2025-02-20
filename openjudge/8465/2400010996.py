##事先设定好方向数组directions，然后用dfs函数进行搜索，如果走到即记录为一条新路
directions=[[-1,2],[-1,-2],[1,2],[1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]
ans=[]
jieshu=[]
def dfs(x,y,n,m,path,field):
    global ans
    if len(path)==n*m:
        ans.append(path)
        return
    else:
        for i in directions:
            dx,dy=x+i[0],y+i[1]
            if 0<=dx<n and 0<=dy<m and field[dx][dy]==0:
                field[dx][dy]=1
                path.append([dx,dy])
                dfs(dx,dy,n,m,path,field)
                field[dx][dy]=0
                path.pop()

t = int(input())
for k in range(t):
    N,M,a,b=map(int,input().split())
    field1=[[0]*M for _ in range(N)]
    field1[a][b]=1
    ans=[]
    dfs(a,b,N,M,[[a,b]],field1)
    jieshu.append(len(ans))
for i in jieshu:
    print(i)



