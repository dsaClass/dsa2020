dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x,y) :
    global sign
    global step
    for i in range(4) :
        nx=x+dx[i]
        ny=y+dy[i]
        if maze[nx][ny]=='e' :
            sign=1
            step+=1
            continue 
        if maze[nx][ny]=='.' :
            maze[x][y]='#'
            dfs(nx,ny)
            maze[x][y]='.'
    return
    
n,m=map(int,input().split())
maze=[]
maze.append(['#']*(m+2))
for _ in range(n) :
    maze.append(['#']+list(input())+['#'])
maze.append(['#']*(m+2))
maze[1][1]='s'
maze[n][m]='e'
sign=0
step=0
dfs(1,1)
if sign==1 :
    print(step)
else :
    print('0')