n=int(input())
is_child=[False]*n
tree={}

for i in range(n) :
    left,right=map(int,input().split())
    tree[i]=(left,right)
    if left!=-1 :
        is_child[left]=True
    if right!=-1 :
        is_child[right]=True
        

max_depth=0
leaves=0

def dfs(node,depth) :
    global max_depth,leaves
    if node==-1 :
        return
    max_depth=max(depth,max_depth)
    left,right=tree[node]
    if left==-1 and right==-1 :
        leaves+=1
    
    dfs(left,depth+1)
    dfs(right,depth+1)

for i in range(n) :
    if not is_child[i] :
        root=i
        break

dfs(root,0)
print(max_depth,leaves)