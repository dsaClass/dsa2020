class TreeNode:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
def buildtree(inorder,postorder):
    if not inorder or not postorder:
        return None
    root_val=postorder[-1]
    root=TreeNode(root_val)
    x=inorder.index(root_val)
    left_inorder=inorder[:x]
    right_inorder=inorder[x+1:]
    y=len(left_inorder)
    left_postorder=postorder[:y]
    right_postorder=postorder[y:-1]
    root.left=buildtree(left_inorder,left_postorder)
    root.right=buildtree(right_inorder,right_postorder)
    return root
def text_tree(root,depth=0):
    if root is not None:
        print("\t"*depth+root.value)
        if root.left is not None:
            text_tree(root.left,depth+1)
        elif root.left is None and root.right is not None:
            print("\t"*(depth+1)+"*")
        if root.right is not None:
            text_tree(root.right,depth+1)
inorder=input()
postorder=input()
root=buildtree(inorder,postorder)
text_tree(root)
