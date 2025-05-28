inorder=input()
postorder=input()
class Treenode():
    def __init__(self,name):
        self.val=name
        self.left=None
        self.right=None
def build_up_tree(inorder,postorder):
    if len(inorder)==0:
        return None
    root_val=postorder[-1]
    root=Treenode(root_val)
    idx=inorder.index(root_val)
    root.left = build_up_tree(inorder[:idx],postorder[:idx])
    root.right = build_up_tree(inorder[idx+1:],postorder[idx:-1])
    return root
def print_tree(node, level=0):
    if not node:
        return
    print('\t' * level + node.val)
    if not node.left and node.right:
        print('\t' * (level + 1) + '*')
    if node.left:
        print_tree(node.left, level + 1)
    if node.right:
        print_tree(node.right, level + 1)
root = build_up_tree(inorder, postorder)
print_tree(root)