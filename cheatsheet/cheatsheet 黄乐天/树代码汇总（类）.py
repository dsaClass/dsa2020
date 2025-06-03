#二叉树
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


#DFS：同时前、中、后续遍历
pre, ino, post = [], [], []
def dfs(node):
    if node is None:
        return
    pre.append(node.val)
    dfs(node.left)
    ino.append(node.val)
    dfs(node.right)
    post.append(node.val)

dfs('root')
print(''.join(pre))
print(''.join(ino))
print(''.join(post))


#BFS:层序遍历
from collections import deque
def level_order(root):
    ans=[]
    if not root: return
    q = deque([root])
    while q:
        node = q.popleft()
        ans.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return ans

#前序+中序建立树
def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    root_val = preorder[0]
    root = Node(root_val)
    mid = inorder.index(root_val)
    root.left = build_tree(preorder[1:1+mid], inorder[:mid])
    root.right = build_tree(preorder[1+mid:], inorder[mid+1:])
    return root


#建立二叉搜索树
def insert_bst_tree(tree, val):
    if tree is None:
        return Node(val)
    if val < tree.val:
        tree.left = insert_bst_tree(tree.left, val)
    elif val > tree.val:
        tree.right = insert_bst_tree(tree.right, val)
    return tree

def build_bst_tree(nums):
    tree=None
    for num in nums:
        tree=insert_bst_tree(tree,num)
    return tree

#求高度
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))

from collections import deque


#用前序遍历建立扩展二叉树（即根节点均为'.')
def build_tree(preorder):
    def helper():
        nonlocal index
        if index >= len(preorder):
            return None
        val = preorder[index]
        index += 1
        if val == '.':
            return None
        node = Node(val)
        node.left = helper()
        node.right = helper()
        return node

    index = 0
    return helper()


#判断是否为二叉搜索树
def is_bst(node, low=float('-inf'), high=float('inf')):
    if not node:
        return True
    if not (low < node.val < high):
        return False
    return is_bst(node.left, low, node.val) and is_bst(node.right, node.val, high)


#DFS 模板：寻找和为指定树的路径
def has_path_sum_dfs(node, target):
    if not node:
        return False
    if not node.left and not node.right:
        return node.val == target
    return  has_path_sum_dfs(node.left,  target - node.val) or has_path_sum_dfs(node.right, target - node.val)
 
#BFS 模板
from collections import deque
def has_path_sum_bfs(root, target):
    if not root:
        return False
    q = deque([(root, root.val)])
    while q:
        node, cur_sum = q.popleft()
        if not node.left and not node.right and cur_sum == target:
            return True
        if node.left:
            q.append((node.left,  cur_sum + node.left.val))
        if node.right:
            q.append((node.right, cur_sum + node.right.val))
    return False

#修改子树
def modify_subtree(node, func):
    if node is None:
        return
    func(node)
    modify_subtree(node.left,  func)
    modify_subtree(node.right, func)


#一般树
class Node:
    def __init__(self):
        self.children = []

#用dfs序列‘d u’建立树的结构
def build_general_tree(trace: str):
    root = Node()
    stack = [root]
    for ch in trace:
        if ch == 'd':
            new_node = Node()
            stack[-1].children.append(new_node)
            stack.append(new_node)
        elif ch == 'u':
            stack.pop()
    return root

#邻接表
from collections import defaultdict
adj = defaultdict(list)
edges=[]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

n=1
#DFS 构建深度和父亲表
LOG = n.bit_length() + 1  # 最多跳 2^k 层祖先
depth = [0] * (n + 1)
parent = [[-1] * (n + 1) for _ in range(LOG)]

def dfs(u, fa):
    parent[0][u] = fa
    for v in adj[u]:
        if v != fa:
            depth[v] = depth[u] + 1
            dfs(v, u)

dfs('root', -1)


#树与二叉树互相转化
class GenTreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

class BinTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None   # 第一个孩子
        self.right = None  # 下一个兄弟

#树转化为二叉树
def gen_to_bin(root: GenTreeNode) -> BinTreeNode:
    if not root:
        return None
    b_root = BinTreeNode(root.val)
    if not root.children:
        return b_root
    # 第一个孩子作为左子树
    b_root.left = gen_to_bin(root.children[0])
    # 后续孩子串为右兄弟链
    current = b_root.left
    for child in root.children[1:]:
        current.right = gen_to_bin(child)
        current = current.right
    return b_root

#二叉树转化为树
def bin_to_gen(root: BinTreeNode) -> GenTreeNode:
    if not root:
        return None
    g_root = GenTreeNode(root.val)
    child = root.left
    while child:
        g_root.children.append(bin_to_gen(child))
        child = child.right
    return g_root


#打印树（用缩进表示）
def print_gen_tree(node, depth=0):
    if node:
        print('  ' * depth + str(node.val))
        for child in node.children:
            print_gen_tree(child, depth + 1)

def print_bin_tree(node, depth=0):
    if node:
        print('  ' * depth + str(node.val))
        print_bin_tree(node.left, depth + 1)
        print_bin_tree(node.right, depth)



#建立哈夫曼树
class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq  # 频率
        self.char = char  # 字符（叶子节点才有）
        self.left = left
        self.right = right

    def __lt__(self, other):  # 定义小于
        if self.freq==other.freq:
            self.char.sort()
            other.char.sort()
            return ord(self.char[0]) < ord(other.char[0])
        return self.freq < other.freq

n=int(input())
l=[input().split() for _ in range(n)]
freqs = {i[0]:int(i[1]) for i in l}

# 初始堆：每个字符一个节点
import heapq
heap = [Node(freq, char) for char, freq in freqs.items()]
heapq.heapify(heap)

# 构建哈夫曼树
while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)
    new_node = Node(left.freq + right.freq, char=left.char+right.char , left=left, right=right)
    heapq.heappush(heap, new_node)

# 最终堆中只剩一个节点，就是树的根
root = heap[0]

def print_codes(node, prefix=""):
    if node.char:
        print(f"{node.char}: {prefix}")
    else:
        print_codes(node.left, prefix + "0")
        print_codes(node.right, prefix + "1")

print_codes(root)
