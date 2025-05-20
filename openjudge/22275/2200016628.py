class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(preorder):
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    left = [x for x in preorder if x < root.val]
    right = [x for x in preorder if x > root.val]
    root.left= build_tree(left)
    root.right= build_tree(right)
    return root


def postorder_traversal(root):
    if not root:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]

n = int(input())
preorder = list(map(int, input().split()))
tree = build_tree(preorder)
postorder = postorder_traversal(tree)
print(' '.join(map(str, postorder)))