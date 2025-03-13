def build_tree(inorder, postorder):
    if not inorder:
        return None
    # 后序遍历的最后一个元素是根节点
    root_val = postorder.pop()
    root = TreeNode(root_val)
    # 在中序遍历中找到根节点的位置
    mid = inorder.index(root_val)
    # 递归构建右子树和左子树
    root.right = build_tree(inorder[mid+1:], postorder)
    root.left = build_tree(inorder[:mid], postorder)
    return root

def preorder_traversal(root):
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_optimized(inorder, postorder, in_start, in_end, post_start, post_end, index_map):
    if in_start > in_end or post_start > post_end:
        return None
    # 后序遍历的最后一个元素是根节点
    root_val = postorder[post_end]
    root = TreeNode(root_val)
    # 找到根节点在中序遍历中的位置
    mid = index_map[root_val]
    # 计算左子树的节点数
    num_left = mid - in_start
    # 递归构建左子树和右子树
    root.left = build_tree_optimized(inorder, postorder, in_start, mid - 1, post_start, post_start + num_left - 1, index_map)
    root.right = build_tree_optimized(inorder, postorder, mid + 1, in_end, post_start + num_left, post_end - 1, index_map)
    return root

def create_index_map(inorder):
    return {val: idx for idx, val in enumerate(inorder)}

# 读取输入
inorder_seq = input().strip()
postorder_seq = input().strip()

# 创建中序遍历的哈希表
index_map = create_index_map(list(inorder_seq))

# 构建二叉树
root = build_tree_optimized(list(inorder_seq), list(postorder_seq), 0, len(inorder_seq) - 1, 0, len(postorder_seq) - 1, index_map)

# 生成前序遍历序列
preorder_seq = ''.join(preorder_traversal(root))

# 输出结果
print(preorder_seq)