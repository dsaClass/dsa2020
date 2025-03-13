from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(inorder, postorder):
    if not inorder:
        return None
    root_val = postorder.pop()
    root = TreeNode(root_val)
    mid = inorder.index(root_val)
    root.right = build_tree(inorder[mid+1:], postorder)
    root.left = build_tree(inorder[:mid], postorder)
    return root

def level_order_traversal(root):
    if not root:
        return ""
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return ''.join(result)

n = int(input())
for _ in range(n):
    inorder = input().strip()
    postorder = input().strip()
    tree = build_tree(list(inorder), list(postorder))
    print(level_order_traversal(tree))