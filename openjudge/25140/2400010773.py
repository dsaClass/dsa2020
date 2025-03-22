from collections import deque
class TreeNode:
	def __init__(self,val,left=None,right=None):
		self.val=val
		self.left=left
		self.right=right
n=int(input())


for _ in range(n):
	s=input()
	stack=[]
	for char in s:
		if ord(char)>96:
			node=TreeNode(char)
			stack.append(node)
		else:
			node=TreeNode(char)
			right=stack.pop()
			left=stack.pop()
			node.left=left
			node.right=right
			stack.append(node)
	root=stack[0]
	queue=deque()
	queue.append(root)
	traversal=[]
	while queue:
		node=queue.popleft()
		traversal.append(node.val)
		if node.left:
			queue.append(node.left)
		if node.right:
			queue.append(node.right)
	traversal=traversal[::-1]
	print(''.join(traversal))