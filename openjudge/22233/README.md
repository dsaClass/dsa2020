# P1330:二叉查找树的lower_bound和upper_bound(Python版)

------

总时间限制: 1000ms 内存限制: 65536kB

### 描述

程序填空  
为二叉排序树类Tree添加方法lower_bound(self,x)和upper_bound(self,x)。  
前者返回一个元组，包含关键字小于x的最大元素的关键字和值  
后者返回一个元组，包含关键字大于x的最小元素的关键字和值  
如果找不到符合要求的元组，这两个函数都返回None

不要求只能写这两个函数，可以写额外的辅助函数

### 已给出代码：
    class TreeNode: #节点类
    	#father在删除节点的时候有用,以及找一个节点的后继节点的时候有用
    	def __init__(self,key,val,father=None,left=None,right=None):
    		self.key,self.val,self.left,self.right ,self.father \
    			= key,val,left,right,father
    	def isLeftChild(self):
    		return self.father and self.father.left == self
    	def isRightChild(self):
    		return self.father and self.father.right == self
    class Tree:
    	def __init__(self,NodeType = TreeNode,less=lambda x,y:x<y ):
    		self.root,self.size = None,0 #root是树根，size是节点总数
    		self.less = less #less是比较函数,
    		self.NodeType = NodeType #NodeType是节点类型
    	def __find(self,key,root): #私有方法，不宜也不易直接访问
    		if self.root == None:
    			return None
    		if self.less(key,root.key):
    			if root.left:
    				return self.__find(key,root.left)
    			else:
    				return None
    		elif self.less(root.key,key):
    			if root.right:
    				return self.__find(key,root.right)
    			else:
    				return None
    		else:
    			return root
    	def insert(self,key,val): #插入节点 #modi
    		if self.root == None:
    			self.root = self.NodeType(key,val)
    			self.size += 1
    		else:
    			if self.__inserter(key,val,self.root):
    				self.size += 1
    	def __inserter(self,key,val,root): #modi
    		if self.less(key,root.key) :
    			if root.left == None:
    				root.left = self.NodeType(key, val,root) #root是father
    				return True
    			else:
    				return self.__inserter(key,val,root.left)
    		elif self.less(root.key,key):
    			if root.right == None:
    				root.right = self.NodeType(key,val,root)
    				return True
    			else:
    				return self.__inserter(key,val,root.right)
    		else:
    			root.val = val  #相同关键字，则更新
    			return False
    	def findMin(self): #寻找最小节点  #modi
    		if self.root == None:
    			return None
    		nd = self.__findMin(self.root)
    		return (nd.key,nd.val)
    	def __findMin(self,root):
    		if root.left == None:
    			return root
    		else:
    			return self.__findMin(root.left )
    	def __findMax(self,root):
    		if root.right == None:
    			return root
    		else:
    			return self.__findMax(root.right)
    	def pop(self,key):
    		#删除键为key的元素，返回该元素的值。如果没有这样的元素，则引发异常
    		nd = self.__find(key,self.root)
    		if nd == None:
    			raise Exception("key not found")
    		else:
    			self.size -= 1
    			self.__deleteNode(nd)
    	def __deleteNode(self,nd): #删除节点nd
    		if nd.left and nd.right: #左右子树都有
    			minNd = self.__findMin(nd.right)
    			nd.key,nd.val = minNd.key,minNd.val
    			self.__deleteNode(minNd)
    		elif nd.left:	#只有左子树
    			if nd.isLeftChild():
    				nd.father.left = nd.left
    				nd.left.father = nd.father
    			elif nd.isRightChild():
    				nd.father.right = nd.left
    				nd.left.father = nd.father
    			else: #是树根
    				self.root = nd.left
    				self.root.father = None
    		elif nd.right : #只有右子树
    			if nd.isRightChild():
    				nd.father.right = nd.right
    				nd.right.father = nd.father
    			elif nd.isLeftChild():
    				nd.father.left = nd.right
    				nd.right.father = nd.father
    			else:
    				self.root = nd.right
    				self.root.father = None
    		else: #nd是叶子
    			if nd.isLeftChild():
    				nd.father.left = None
    			elif nd.isRightChild():
    				nd.father.right = None
    			else:
    				self.root = None
    	def inorderTravelSeq(self): #中序遍历生成器
    		if self.root == None:
    			return
    		stack = [[self.root,0]] #0表示self的左子树还没有遍历过
    		while len(stack) > 0:
    			node = stack[-1]
    			if node[0] == None: #node[0]是树节点
    				stack.pop()
    				continue
    			if node[1] == 0: #左子树还没有遍历过
    				node[1] = 1
    				stack.append([node[0].left,0])
    			elif node[1] == 1: #左子树已经遍历过
    				yield (node[0].key,node[0].val)
    				node[1] = 2
    				stack.append([node[0].right, 0])
    			else: #右子树也遍历完了
    				stack.pop()
    	def __contains__(self, key):
    		return self.__find(key,self.root) != None
    	def __iter__(self): #返回迭代器
    		return self.inorderTravelSeq()
    	def __getitem__(self,key):
    		nd = self.__find(key,self.root)
    		if nd == None:
    			raise Exception("key not found")
    		else:
    			return nd.val
    	def __setitem__(self, key, value): #
    		nd = self.__find(key,self.root)
    		if nd == None:
    			self.insert(key,value)
    		else:
    			nd.val = value

        // 在此补充你的代码

    tree = Tree()
    while True:
    	try:
    		s = input().split()
    		if s[0] == "ADD":
    			tree[int(s[1])] = int(s[1])
    		elif s[0] == "LB":
    			print(tree.lower_bound(int(s[1])))
    		elif s[0] == "UB":
    			print(tree.upper_bound(int(s[1])))
    	except:
    		break
    

### 输入

若干行。每行是如下三种形式之一：  

1) ADD n  
   n是个整数。表示要往树中添加一个节点，关键字和值都是n  
2) LB n  
   表示要求tree.lower_bound(n)  
3) UB n  
   表示要求tree.upper_bound(n)

### 输出

输出:  
如程序和样例所示

### 样例输入

    ADD 68
    ADD 42
    LB 180
    UB 35
    LB 50
    ADD 75
    ADD 101
    LB 114
    UB 40
    ADD 26
    LB 68
    UB 63
    ADD 88
    UB 173
    UB 39

### 样例输出

    (68, 68)
    (42, 42)
    (42, 42)
    (101, 101)
    (42, 42)
    (42, 42)
    (68, 68)
    None
    (42, 42)

### 来源：

    郭炜
