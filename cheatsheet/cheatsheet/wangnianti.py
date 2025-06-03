
#切木材（去年机考题）（二分查找）
def binary_search(low,high):
    tps=0
    mid=(low+high)//2
    if low==high:
        return mid
    for wood in woods:
        tps+=wood//mid
    if tps>k:
        return binary_search(mid+1,high)
    elif tps<k:
        return binary_search(low,mid)
    else:
        return mid
mid=binary_search(0,2*max)
if mid==0:
    print(0)
else:
    while True:
        mid+=1
        new_tps=0
        for wood in woods:
            new_tps+=wood//mid
        if new_tps<k:
            print(mid-1)
            break


#越野跑超过人数（归并排序）
n=int(input())
nums=[]
for _ in range(n):
    nums.append(int(input()))
ans=0
def sorting(nums):
    global ans
    if len(nums)<=1:
        return nums
    a=len(nums)//2
    left=sorting(nums[:a])
    right=sorting(nums[a:])
    new_nums=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            new_nums.append(left[i])
            ans+=len(right)-j
            i+=1
        elif left[i]>=right[j]:
            new_nums.append(right[j])
            j+=1
    new_nums.extend(left[i:] if i<len(left) else right[j:])
    return new_nums
new_nums=sorting(nums)
print(ans)

'''

'''
#厚道的调分方法 （二分查找）
grade=list(map(float,input().split()))
n=len(grade)
if n%5!=0:
    good_n=int(n*0.6)+1
else:
    good_n=n//5*3

grade.sort(reverse=True)
standard=grade[good_n-1]
def tiaofen(b):
    a=b/1000000000
    new_grade=a*standard+1.1**(a*standard)
    return new_grade

low,high=399511173,998777935
while low<high:
    mid=low+(high-low)//2
    if tiaofen(mid)<85:
        low=mid+1
    elif tiaofen(mid)>=85:
        high=mid

print(low)
'''

#8209 月度开销（二分查找）
'''
n,m=map(int,input().split())
payment=[]
for _ in range(n):
    payment.append(int(input()))

def kaixiao(target):
    count=1
    current_sum=0
    for i in payment:
        if current_sum+i<=mid:
            current_sum+=i
        else:
            count+=1
            current_sum=i
    return count


low,high=max(payment),sum(payment)
while low<high:
    mid=(low+high)//2
    if kaixiao(mid)<=m:  #可能正确的情况，但我们希望得到更小的m
        high=mid
    elif kaixiao(mid)>m:  #一定错误的情况，要修改边界值将原low规避掉
        low=mid+1

print(low)

'''



#1818 红与黑(DFS)
'''
def dfs(x,y):
    count=1
    row=len(mapp)
    col=len(mapp[0])
    visited[y][x]=True
    direction=[(0,1),(1,0),(0,-1),(-1,0)]
    for dx,dy in direction:
        new_x=x+dx
        new_y=y+dy
        if 0<=new_x<=col-1 and 0<=new_y<=row-1 and not visited[new_y][new_x] and mapp[new_y][new_x]==0:
            count+=dfs(new_x,new_y)
    return count

while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    mapp=[[0 for _ in range(n)] for _ in range(m)]
    current_x=current_y=0
    for i in range(m):
        a=input()
        a=list(str(a))
        for j in range(n):
            if a[j]=="#":
                mapp[i][j]=1
            elif a[j]==".":
                mapp[i][j]=0
            else:
                current_x = j
                current_y = i
                mapp[i][j] = 0

    visited=[[False for _ in range(n)]for _ in range(m)]
    visited[current_y][current_x]=True
    print(dfs(current_x,current_y))

'''

#无向图的深度优先搜索
'''
n,m=map(int,input().split())
edges=[[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    edges[a][b]=1
    edges[b][a]=1
visited=[0 for _ in range(n)]
ans=[]
def dfs(i):
    global ans
    visited[i]=1
    ans.append(i)
    for e in range(n):
        if edges[i][e]==1 and visited[e]==0:
            visited[e]=1
            dfs(e)
for i in range(n):
    if visited[i]==0:
        dfs(i)


print(" ".join(map(str,ans)))

'''

#23163 判断无向图是否联通有无回路
'''
n,m=map(int,input().split())
graph=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[0 for _ in range(n)]
want_visited=[1 for _ in range(n)]

connected=True
loop=False
def dfs(i,parent):  #回溯这一步不能算作构成环
    global loop
    visited[i]=1
    for e in graph[i]:
        if e==parent:
            continue
        elif visited[e]==1:
            loop=True
        else:
            dfs(e,i)

for i in range(n):
    if visited[i]==0:
        dfs(i,-1)
        if visited!=want_visited:
            connected=False

print("connected:yes" if connected else "connected:no")

print("loop:yes" if loop else "loop:no")


#2721 文本二叉树
class NodeTree():
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.parent=None
        self.child_count=0

#前序遍历
def preorder(node):
    if not node:
        return ""
    else:
        return node.key + preorder(node.left) + preorder(node.right)

#中序遍历
def inorder(node):
    if not node:
        return ""
    else:
        return inorder(node.left)+node.key+inorder(node.right)

#后序遍历
def postorder(node):
    if not node:
        return ""
    else:
        return postorder(node.left) + postorder(node.right)+node.key

n=int(input())
for _ in range(n):
    #读入数据
    node_dict={}
    nodes=[]
    last_node=[False]*100 #储存的是树结点

    #建树
    while True:
        a=list(input())
        if a==["0"]:
            break
        nodes.append(a)
    for key in nodes:
        if len(key)==1:
            root=key[0]
            node_dict[key[0]]=NodeTree(key[0])
            last_node[0]=node_dict[key[0]]
        else:
            depth=len(key)-1
            parent=last_node[depth-1]
            if key[-1]=="*":
                parent.child_count=1
            else:
                new_node=key[-1]
                node_dict[new_node]=NodeTree(new_node)
                last_node[depth]=node_dict[new_node]
                if parent.child_count==0:
                    parent.left=node_dict[new_node]
                    parent.child_count += 1
                elif parent.child_count==1:
                    parent.right=node_dict[new_node]
    for key,node in node_dict.items():
        node.key=key
    print(preorder(node_dict[root]))
    print(postorder(node_dict[root]))
    print(inorder(node_dict[root]))
    if _<n-1:
        print(" ")


#5907 二叉树的操作
#树的结点交换与前驱访问
'''
本题的重点在于如何建树，并反映每个结点的父亲与左右子关系
可以建立一个字典node_dist，方便地从key返回树的结点
'''

class TreeNode:
    def __init__(self,key,left=None,right=None,parent=None):
        self.key=key
        self.left=None
        self.right=None
        self.parent=None

t=int(input())
for _ in range(t):
    #建树
    n,m=map(int,input().split())
    node_dict={}
    for _ in range(n):
        x,y,z=map(int,input().split())
        if x not in node_dict:
            node_dict[x]=TreeNode(x)
        node=node_dict[x]
        if y!=-1:
            if y not in node_dict:
                node_dict[y]=TreeNode(y)
            l_node=node_dict[y]
            node.left=l_node
            l_node.parent=node
        if z!=-1:
            if z not in node_dict:
                node_dict[z]=TreeNode(z)
            r_node=node_dict[z]
            node.right = r_node
            r_node.parent = node
    for x,x_node in node_dict.items():
        x_node.key=x

    #进行操作
    for _ in range(m):
        a=list(map(int,input().split()))
        if a[0]==1:
            x,y=node_dict[a[1]],node_dict[a[2]]
            px=x.parent
            py=y.parent
            if px.left==x:
                pos_x="left"
            else:
                pos_x="right"
            if py.left==y:
                pos_y="left"
            else:
                pos_y="right"
            if pos_x=="left":
                px.left=y
            else:
                px.right=y
            if pos_y == "left":
                py.left = x
            else:
                py.right = x
            y.parent=px
            x.parent=py


        elif a[0]==2:
            x=node_dict[a[1]]
            while x.left:
                x=x.left

            print(x.key)


