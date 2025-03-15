m,n=map(int,input().split())
ans=0
def dfs(apple,plant,mx):
    global ans
    if plant==1:
        if apple>=mx:
            ans+=1
        return
    for i in range(mx, apple+1):
        dfs(apple-i,plant-1,i)

dfs(m,n,0)
print (ans)