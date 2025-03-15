class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    # 前序遍历的第一个元素是根节点
    root_val = preorder[0]
    root = TreeNode(root_val)
    
    # 在中序遍历中找到根节点的位置
    mid_idx = inorder.index(root_val)
    
    # 递归构建左子树和右子树
    root.left = build_tree(preorder[1:mid_idx+1], inorder[:mid_idx])
    root.right = build_tree(preorder[mid_idx+1:], inorder[mid_idx+1:])
    
    return root

def postorder_traversal(root):
    if not root:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    for i in range(0, len(data), 2):
        preorder = data[i]
        inorder = data[i+1]
        
        root = build_tree(preorder, inorder)
        postorder = postorder_traversal(root)
        
        print(''.join(postorder))

if __name__ == "__main__":
    main()