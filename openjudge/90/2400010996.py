#dp与dfs相结合
#通过dfs的操作来实现dp法中项之间的关系处理
R,C=map(int,input().split())
place=[]
directions=[[-1,0],[1,0],[0,1],[0,-1]]
for i in range(R):
    place.append(list(map(int,input().split())))
dp=[[0]*(C) for i in range(R)]
def dfs(x,y):
    global dp
    if dp[x][y]>0:
        return dp[x][y]
    ans=1
    for i in directions:
        dx,dy=x+i[0],y+i[1]
        if 0<=dx<R and 0<=dy<C and place[dx][dy]<place[x][y]:
            ans=max(ans,dfs(dx,dy)+1)
    dp[x][y]=ans
    return ans
answer=1
for i in range(R):
    for j in range(C):
        answer=max(dfs(i,j),answer)
print(answer)


