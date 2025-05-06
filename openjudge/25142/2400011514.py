class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(in_order, post_order):
    if not post_order:
        return None
    root_val = post_order[-1]
    root = TreeNode(root_val)
    index = in_order.index(root_val)
    left_in = in_order[:index]
    right_in = in_order[index+1:]
    left_post = post_order[:index]
    right_post = post_order[index:-1]
    root.left = build_tree(left_in, left_post)
    root.right = build_tree(right_in, right_post)
    return root

def collect_nodes(node, level, result):
    if node is None:
        return
    result.append((level, node.val))
    if node.left is None and node.right is not None:
        result.append((level + 1, '*'))
    else:
        collect_nodes(node.left, level + 1, result)
    collect_nodes(node.right, level + 1, result)

# 读取输入
in_order = input().strip()
post_order = input().strip()

# 构建二叉树
root = build_tree(in_order, post_order)

# 收集节点信息
result = []
if root:
    collect_nodes(root, 0, result)

# 生成输出
for level, val in result:
    print('\t' * level + val)