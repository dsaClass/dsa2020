n=int(input())
tree={}
for i in range(n) :
    left,right=map(int,input().split())
    tree[i+1]=(left,right)

max_depth=0

def dfs(node,depth) :
    if node==-1 :
        return
    global max_depth

    left,right=tree[node]
    max_depth=max(depth,max_depth)

    dfs(left,depth+1)
    dfs(right,depth+1)

dfs(1,1)
print(max_depth)