#前序遍历+中序遍历 得到 后序遍历
def post(pre,mid):
    if not pre or not mid:
        return []
    else:
        root=pre[0]
        idx=mid.index(root)
        left=mid[:idx]
        right=mid[idx+1:]
        pre_left=pre[1:idx+1]
        pre_right=pre[idx+1:]
        return post(pre_left,left)+post(pre_right,right)+[root]
    
#建立二叉搜索树（列表实现） 用[val,left,right]表示
def insert_bst_tree(tree,val):
    if tree is None:
        return [val,None,None]
    if val < tree[0]:
        tree[1] = insert_bst_tree(tree[1],val)
    elif val > tree[0]:
        tree[2] = insert_bst_tree(tree[2],val)
    return tree

def build_bst_tree(nums):
    tree=None
    for num in nums:
        tree=insert_bst_tree(tree,num)
    return tree

#DST（前、中、后）
pre,ino,post =[],[],[]
def dst(tree):
    if not tree:
        return
    pre.append(tree[0])
    dst(tree[1])
    ino.append(tree[1])
    dst(tree[2])
    post.append(tree[2])
print(''.join(pre))

#递归计算一般树高度（列表表示）
def general_tree_height(tree):
    if not tree:
        return 0
    _, children = tree
    child_heights = [general_tree_height(child) for child in children]
    return 1 + (max(child_heights) if child_heights else 0)


#用每个编号的左、右儿子表示的二叉树
#寻找根节点
n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
ll=[i for j in l for i in j]
def findroot():
    for i in range(n):
        if not i in ll:
            return i
root=findroot()

#递归计算高度和叶子节点数
count=0
def height(root):
    global count
    if root==-1:
        return 0
    #可选：若不计算叶子节点数，可删去
    if l[root]==[-1,-1]:
        count+=1
        return 0
    return 1+max(height(l[root][0]),height(l[root][1]))

#计算宽度
depth=[[root]]
while depth[-1]:
    l1=[]
    for i in depth[-1]:
        if l[i][0]!=-1:
            l1.append(l[i][0])
        if l[i][1]!=-1:
            l1.append(l[i][1])
    depth.append(l1)
l2=[len(i) for i in depth]
print(max(l2))


'''一般的树'''
#处理括号嵌套树 输入为a(b(c,d),e) 得到一个节点的子树
def bulid(node):
    root=node[0]
    if not node:
        return

    node=node[2:-1]
    a=0
    children=[]
    curr=-1
    for i in range(len(node)):
        if node[i]=='(':
            a+=1
        elif node[i]==')':
            a-=1
        elif node[i]==',':
            if a==0:
                children.append(node[curr+1:i])
                curr=i
    children.append(node[curr+1:])
    for child in children:
        pass


#已知前序、后序，求树的个数（重复直接记为0，未优化时间）
def count(pre,post):
    pre,post=list(pre),list(post)
    if len(set(pre))!=len(pre) or len(set(post))!=len(post):
        return False
    if set(pre)!=set(post):
        return False
    if len(pre)==1:
        return 1
    if pre[0]!=post[-1]:
        return False
    del pre[0]
    del post[-1]
    if pre[0]==post[-1]:
        n1=count(pre,post)
        if n1==False:
            return False
        return 2*n1
    for i in range(len(pre)):
        if set(pre[:i+1])==set(post[:i+1]):
            n2=count(pre[:i+1],post[:i+1])
            n3=count(pre[i+1:],post[i+1:])
            if not n2 or not n3:
                return False
            return n2*n3
        
