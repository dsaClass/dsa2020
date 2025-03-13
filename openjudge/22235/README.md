# P0800:二叉树形式表示的树

总时间限制: 1000ms 内存限制: 65536kB
## 描述
输入一棵文本形式表示的树，树节点都是大写字母。
建立一棵儿子兄弟形式的二叉树来表示该树，并且输出该二叉树的前序遍历序列和中序遍历序列。注意，是二叉树，而不是原来那棵树的遍历序列。
程序填空，填写 `buildTreeInBinary`函数，该函数建立所需的二叉树
```
class BinaryTree:
	def __init__(self,data,left = None,right = None):
		self.data,self.left,self.right = data,left,right
	def addLeft(self,tree):
		self.left = tree
	def addRight(self,tree):
		self.right = tree
	def preorderTravel(self,op):
		op(self.data)
		if self.left:
			self.left.preorderTravel(op)
		if self.right:
			self.right.preorderTravel(op)
	def inorderTravel(self,op):
		if self.left:
			self.left.inorderTravel(op)
		op(self.data)
		if self.right:
			self.right.inorderTravel(op)
	def postorderTravel(self,op):
		if self.left:
			self.left.postorderTravel(op)
		if self.right:
			self.right.postorderTravel(op)
		op(self.data)

nodes = []
#nodes内容形如：[(0, 'A'), (1, 'B'), (2, 'E')......]
nodesPtr = 0  #表示看到nodes里的第几行
def buildTreeInBinary(level):
#要求此函数返回一个BinaryTree对象
// 在此处补充你的代码
while True:
	try:
		s = input().rstrip()
		nodes.append((len(s)-1,s.strip()))
	except:
		break
tree = buildTreeInBinary(0)
tree.preorderTravel(lambda x :print(x,end=""))
print()
tree.inorderTravel(lambda x :print(x,end=""))
```

## 输入
第一行是根节点，没有缩进。根节点是第0层的节点
接下来每行一个节点。第n层的节点，就缩进n个制表符
一个第i层的节点，其父节点就是其上方距其最近的那个第i-1层的节点
## 输出
先输出二叉树的前序遍历序列，再输出中序遍历序列
## 样例输入
A
	B
		E
	C
		F
		G
	D
		H
			I
## 样例输出
ABECFGDHI
EBFGCIHDA