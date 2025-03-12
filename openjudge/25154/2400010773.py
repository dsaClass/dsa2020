class TreeNode:
	def __init__(self,val,children=[],parent=None,l=None,r=None):
		self.val=val
		self.children=children
		self.parent=parent
		self.l=l
		self.r=r
info=[]
while True:
	try:
		s=input().split()
		info.append(s)
	except EOFError:
		break

nodes_val={}
for s in info:
	root_val=s[0]
	children_val=s[1:]
	if root_val in nodes_val:
		root=nodes_val[root_val]

	else:
		root=TreeNode(root_val,children=[])
		nodes_val[root_val]=root
	for child_val in children_val:
		if child_val in nodes_val:
			child=nodes_val[child_val]
			child.parent=root
		else:
			child=TreeNode(child_val,children=[])
			nodes_val[child_val]=child
			child.parent=root

		root.children.append(child)
nodes=[nodes_val[val] for val in nodes_val]	
for node in nodes:
	if not node.parent:
		root=node
for node in nodes:
	if node.children:
		first_children=node.children[0]
		node.l=first_children
	if node.parent and node.parent.children[-1]!=node:
		k=node.parent.children.index(node)
		next_sibling=node.parent.children[k+1]
		node.r=next_sibling

def postorder_traversal(root):
	if not root:
		return ''
	else:
		return postorder_traversal(root.l)+postorder_traversal(root.r)+root.val


print(postorder_traversal(root))