'''
利用 python 自带的 heapq 库建堆
'''
import heapq
heap=[]
num=int(input())
heapq.heappush(heap,num)  #将新元素插入堆
heapq.heappop(heap)  #弹出堆顶
heapq.heapify(heap)  #建堆操作
#针对一个列表建堆，依据列表中某一位置的元素排序
#可以模拟lambda表达式的结构
a1=1
a2=2
a3=3
arr=[a1,a2,a3]
arr_heap=(a2,arr)
heapq.heappush(heap,arr_heap)#默认按照元组的第一个元素排序

'''
利用边的信息(node,left=-1,right=-1)建树
利用字典node_dist储存结点与key的关系，方便地返回对应值的结点
'''
#二叉树的操作（去年机考题）
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

'''
利用文本信息建树
本题的启示：1. 通过设置self.children_count检验下一个数据放在左子树还是右子树
        2. 通过设置last_node来储存某一层最后一个处理的结点，方便构建树
'''
#文本二叉树（去年机考题）
#读入数据
class NodeTree():
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.parent=None
        self.child_count=0

n = int(input())
for _ in range(n):
    # 读入数据
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

'''
深度优先搜索：前序中序与后序遍历
此处给出一例题：由前序、中序遍历生成后序遍历
'''
#重建二叉树（作业题）
def rebuild(pre,mid):
    if not pre and not mid:
        return ""
    root=pre[0]
    mid_index=mid.index(root)
    pre_left=pre[1:mid_index+1]
    pre_right=pre[mid_index+1:]
    mid_left=mid[:mid_index]
    mid_right=mid[mid_index+1:]
    return rebuild(pre_left,mid_left)+rebuild(pre_right,mid_right)+root

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

'''
二叉搜索树
建树过程展示如下：
'''
class TreeNode:
    def __init__(self,val,left=None,right=None,parent=None):
        self.val=val
        self.left=left
        self.right=right
        self.parent=parent

class BinarySearchTree:
    TreeNode=TreeNode
    def __init__(self):
        self.root=None
        self.size=0
    def put(self,val=0):
        self.root=self._put(val,self.root)
    def _put(self,val,curr):
        if curr is None:
            return TreeNode(val)
        elif val<curr.val:
            curr.left=self._put(val,curr.left)
        elif val>curr.val:
            curr.right=self._put(val,curr.right)
        else:
            curr.val=val
        return curr

tree=BinarySearchTree()
nums=[41,467,334,500,169,724,478,358,962,436]
for num in nums:
    tree.put(num)

'''
二叉树的最近公共祖先查询(LCA问题)
'''
q=int(input())
for _ in range(q):
    a,b=map(int,input().split())
    na,nb=node_dict[a],node_dict[b]
    while True:
        if na.depth>nb.depth:  #保证a的层数一定比b少
            na,nb=nb,na
        while na.depth<nb.depth:
            nb=nb.parent
        if na==nb:
            print(na.data)
            break
        else:
            na,nb=na.parent,nb.parent








'''
这一章中我们学习树结构
Chapter7.1 二叉树(binary tree)
7.1.1 一些常见术语：
根节点、叶节点、节点所在的层、节点的度（0,1,2）、
二叉树的高度、节点的深度、节点的高度（经过边的数量）

常见二叉树类型：
perfect binary tree: 所有层的节点被完全填满
complete binary tree: 只有最底层的节点未被填满，且最底层节点尽量靠左填充
full binart tree: 除了叶节点，其余所有都有两个子节点
balanced binary tree:任意节点左子树与右子树高度差绝对值不超过 1
'''
#结点链接法初始化二叉树
class TreeNode:
    def __init__(self,data,left=None,right=None):
        self.val:int=data
        self.left:TreeNode|None=None
        self.right:TreeNode|None=None

    def insertLeft(self,newNode):
        self.left=TreeNode(newNode,left=self.left)
    def insertRight(self,newNode):
        self.right=TreeNode(newNode,right=self.right)
    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setRootVal(self,data):
        self.data=data
    def getRootVal(self):
        return self.data

#初始化节点
if __name__=="__main__":
    n1=TreeNode(data=1)
    n2=TreeNode(data=2)
    n3=TreeNode(data=3)
    n4=TreeNode(data=4)
    n5=TreeNode(data=5)
#构建节点之间的引用关系（指针）
    n1.left=n2
    n1.right=n3
    n2.left=n4
    n2.right=n5
#在n1与n2之间插入节点P
    p=TreeNode(data=6)
    n1.left=p
    p.left=n2
#删除节点P
    n1.left=n2


"""
Chapter 7.2 二叉树遍历
"""
#层序遍历(level-order traversal)，属于广度优先遍历
def level_order(root):
    queue=[]
    queue.append(root)
    res=[]
    while queue:
        tps=queue.pop(0)
        res.append(tps.val)
        if tps.left:
            queue.append(tps.left)
        if tps.right:
            queue.append(tps.right)
    return res
#时间复杂度：O(N) 所有节点被访问一次
#空间复杂度：最差情况：满二叉树，(n+1)/2，时间复杂度O(N)

#前序、中序、后序遍历，均属于深度优先遍历(depth-first traversal)
#深度优先遍历相当于绕着整棵二叉树外围走一圈

def pre_order(root):
    if root is None:
        return
    #访问优先级：根节点->左子树->右子树
    res.append(root.val)
    pre_order(root.left)
    pre_order(root.right)

def in_order(root):
    if root is None:
        return
    #访问优先级：左子树->根节点->右子树
    in_order(root.left)
    res.append(root.val)
    in_order(root.right)

def post_order(root):
    if root is None:
        return
    #访问优先级：左子树->根节点->右子树
    post_order(root.left)
    post_order(root.right)
    res.append(root.val)

res=[]
#时间复杂度分析：O(N)
#空间复杂度分析：最差情况下，树退化为链表，递归深度达到n，占用O(N)栈帧空间

'''
Chapter 7.3 二叉树数组表示
可以根据层序遍历将所有节点存储在一个数组中
对于完全二叉树，设父节点索引为i，则左子节点索引为2i+1，右子节点索引为2i+2
对于非完全二叉树，这种索引失效，可以在数组中显式地表达所有的None
优点：
连续内存空间，缓存友好；完全二叉树节省空间；允许随机访问节点
缺点：
不适合存储数据量过大、None过多的树；插入与删除的效率较低
'''
class ArrayBinaryTree:
    def __init__(self,arr:list[int|None]):
        self._tree=list(arr)

    def size(self):    #列表长度
        return len(self._tree)

    def val(self,i):
        if i<0 or i>=self.size():
            return None
        return self._tree[i]

    def left(self,i):    #获得第i个节点的左子节点索引
        if i<0 or 2*i+1>=self.size():
            return None
        return 2*i+1

    def right(self,i):
        if i<0 or 2*i+2>self.size():
            return None
        return 2*i+2

    def parent(self,i):
        if i<0 or i>self.size():
            return None
        return (i-1)//2

    def level_order(self):  #层序遍历
        self.res=[]
        for i in range(self.size()):
            if not self.val:
                self.res.append(self.val(i))
        return self.res

'''
从全括号表达式建立表达式解析树
'''
def buildParseTree(fpexp):
    fplist=fpexp.split()
    pStack=[]
    currentTree=eTree=TreeNode("")
    pStack.append(currentTree)
    for i in fplist:
        if i=="(":
            currentTree.insertLeft(" ")
            pStack.append(currentTree)
            currentTree=currentTree.getLeftChild(" ")
        elif i in ["+","-","*","/"]:
            currentTree.setRootVal(i)
            currentTree.insertRight("")
            pStack.append(currentTree)
            currentTree=currentTree.getRightChild(" ")
        elif i==")":
            currentTree=pStack.pop()
        elif ord("0")<=ord(i)<=ord("9"):
            currentTree.setRootVal(int(i))
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

import operator
def postorderval(tree):
    opers={"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv}
    if tree:
        left=postorderval(tree.left)
        right=postorderval(tree.right)
        if left and right:
            return opers[tree.getRootVal()](left,right)
        else:
            return tree.getRootVal()
    else:
        return None


'''
作业题
'''
#1790 二叉树
nums=[]
#while True:
 #   test=list(map(int,input().split()))
  #  if test==[0,0]:
   #     break
    #nums.append(test)


def left(m):
    return 2*m
def right(m):
     return 2*m+1
def node(m,n):
     if m>n:
         return 0
     elif m==n:
         return 1
     else:
         return node(left(m),n)+node(right(m),n)+1


# 这样递归可能导致栈溢出，且时间复杂度较高O(NlogN)
def count_subtree_nodes(m,n):
    if m==0:
        return 0
    sum_nodes=0
    level=0
    while True:
        start=m*(2**level)
        if start>n:
            break
        end=start+(2**level-1)
        if end<=n:
            sum_nodes+=2**level
        else:
            sum_nodes+=n-start+1
        level+=1
    return sum_nodes

#for _ in nums:
#   print(count_subtree_nodes(_[0],_[1]))


#1257 重建二叉树
def rebuild(pre,mid):
    if not pre and not mid:
        return ""
    root=pre[0]
    index=mid.index(root)
    lmid=mid[:index]
    rmid=mid[index+1:]
    lpre=pre[1:index+1]
    rpre=pre[index+1:]
    return rebuild(lpre,lmid)+rebuild(rpre,rmid)+root

#while True:
    # try:
    # a, b = input().split()
    #   print(rebuild(a,b))
    #except EOFError:
     #   break

#5431 二叉搜索树
'''
class TreeNode:
    def __init__(self,val,left=None,right=None,parent=None):
        self.val=val
        self.left=left
        self.right=right
        self.parent=parent

class BinarySearchTree:
    TreeNode=TreeNode
    def __init__(self):
        self.root=None
        self.size=0
    def put(self,val=0):
        self.root=self._put(val,self.root)
    def _put(self,val,curr):
        if curr is None:
            return TreeNode(val)
        elif val<curr.val:
            curr.left=self._put(val,curr.left)
        elif val>curr.val:
            curr.right=self._put(val,curr.right)
        else:
            curr.val=val
        return curr

nums=list(map(int,input().split()))
tree=BinarySearchTree()
for i in nums:
    tree.put(i)

def preorder(root,ans):
    if root is None:
        return
    ans.append(root.val)
    preorder(root.left,ans)
    preorder(root.right,ans)

ans=[]
preorder(tree.root,ans)
print(" ".join(map(str,ans)))
'''

#6947 树的转换
class GNode:
    def __init__(self):
        self.children=[]
def build_general_tree(sequence):
    root=GNode()
    stack=[root]
    for char in sequence:
        if char=="d":
            new_node=GNode()
            root.children.append(new_node)
            stack.append(new_node)
        elif char=="u":
            stack.pop()
    return root
def calc_general_height(node):
    if not node.children:
        return 0
    return max(calc_general_height(child) for child in node.children)+1

class BNode:
    def __init__(self):
        self.left=None
        self.right=None
def convert_to_binary(g_node):
    if not g_node:
        return None
    b_node=BNode()
    if g_node.children:
        b_node.left=convert_to_binary(g_node.children[0])
    current=b_node.left
    for child in g_node.children[1:]:
        current.right=convert_to_binary(child)
        current=current.right
    return b_node
def calc_binary_height(b_node):
    if b_node is None:
        return -1
    left_height=calc_binary_height(b_node.left)
    right_height=calc_binary_height(b_node.right)
    return max(left_height,right_height)+1

'''
if __name__=="__main__":
    sequence=input().strip()

    general_root=build_general_tree(sequence)
    h1=calc_general_height(general_root)
    binary_root=convert_to_binary(general_root)
    h2=calc_binary_height(binary_root)

    print(f"{h1}=>{h2}")
'''

#14863 合并果子
'''
import heapq
n=int(input())
nums=list(map(int,input().split()))
if n==1:
    print(0)
else:
    ans=0
    heap=[]
    for i in nums:
        heapq.heappush(heap,i)

    while len(heap)>1:
        a=heapq.heappop(heap)
        b=heapq.heappop(heap)
        s=a+b
        ans+=s
        heapq.heappush(heap,s)

    print(ans)
'''


#24686 树的重量
import sys
def main():
    input=sys.stdin.read().split()
    ptr=0
    k,n=int(input[ptr]),int(input[ptr+1])
    ptr+=2

    size=(1<<k)-1
    weight=[0]*(size+2)
    lazy=[0]*(size+2)
    def push_down(node,node_range):
        if lazy[node]!=0:
            left=2*node
            right=2*node+1
            if left<=size:
                lazy[left]+=lazy[node]
            if right<=size:
                lazy[right]+=lazy[node]
            weight[node]+=lazy[left]+lazy[right]
            lazy[node]=0
    def update_range(node,l,r,start,end,delta):
        if r<start or l>end:
            return
        if start<=l and r<=end:
            lazy[node]+=delta
            return
        mid=(l+r)//2
        push_down(node,r-l+1)
        update_range(2*node,l,mid,start,end,delta)
        update_range(2*node+1,mid+1,r,start,end,delta)
        weight[node]=weight[2*node]+weight[2*node+1]+lazy[2*node]*(mid-l+1)\
        +weight[2*node+1]*(r-mid)
    def query_range(node,l,r,start,end):
        if r<start or l>end:
            return 0
        if start<=l and r<=end:
            return weight[node]+lazy[node]*(r-l+1)
        push_down(node,r-l+1)
        mid=(l+r)//2
        left_sum=query_range(2*node,l,mid,start,end)
        right_sum=query_range(2*node+1,mid+1,r,start,end)
        return left_sum+right_sum

    for _ in range(n):
        parts=input[ptr]
        if parts=="1":
            x=int(input[ptr+1])
            y=int(input[ptr+2])
            ptr+=3
            level=0
            tmp=x
            while tmp<=size:
                level+=1
                tmp=2*tmp
            subtree_size=(1<<(k-(x.bit_length()-1)))-1
            start=x
            end=x+subtree_size-1
            update_range(1,1,size,start,end,y)
        else:
            x=int(input[ptr+1])
            ptr+=2
            level=0
            tmp=x
            while tmp<=size:
                level+=1
                tmp=2*tmp
            subtree_size=(1<<(k-(x.bit_length()-1)))-1
            start=x
            end=x+subtree_size-1
            res=query_range(1,1,size,start,end)
            print(res)

#if __name__=="__main__":
#    main()


#24682 简单树上最近公共祖先查询(LCA问题)
#24637 宝藏二叉树
class TreeNode:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
n=int(input())
lsts=list(map(int,input().strip().split()))
nodes=[TreeNode(i) for i in lsts]
for i in range(n):
    if 2*i+1<n:
        nodes[i].left=nodes[2*i+1]
    if 2*i+2<n:
        nodes[i].right=nodes[2*i+2]
def dfs(root):
    if not root:
        return 0,0
    l1,l2=dfs(root.left)
    r1,r2=dfs(root.right)
    root1=root.value+l2+r2   #包含root值本身，不包含其左右子结点
    root2=max(l1,l2)+max(r1,r2) #不包含root值本身，可能包含其左右子结点
    return root1,root2

print(max(dfs(nodes[0])))
