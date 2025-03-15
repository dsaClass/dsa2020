# 定义树节点
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.first_child = None  # 第一个子节点
        self.next_sibling = None  # 下一个兄弟节点

# 构建树的函数
def build_tree(data):
    nodes = {}  # 用于存储所有节点
    root = None  # 根节点

    for line in data:
        parts = line.strip().split()
        parent = parts[0]
        children = parts[1:]

        # 如果父节点不在字典中，先创建它
        if parent not in nodes:
            nodes[parent] = TreeNode(parent)
        parent_node = nodes[parent]

        # 设置当前父节点的第一个子节点
        if children:
            first_child = children[0]
            if first_child not in nodes:
                nodes[first_child] = TreeNode(first_child)
            parent_node.first_child = nodes[first_child]

            # 设置兄弟节点
            current_child = parent_node.first_child
            for i in range(1, len(children)):
                sibling = children[i]
                if sibling not in nodes:
                    nodes[sibling] = TreeNode(sibling)
                current_child.next_sibling = nodes[sibling]
                current_child = current_child.next_sibling

        # 如果根节点还没有设置，设置为当前父节点
        if not root:
            root = parent_node

    return root

# 后序遍历儿子-兄弟树
def post_order_traversal(node):
    if not node:
        return []
    # 先遍历左子树（第一个子节点）
    left = post_order_traversal(node.first_child)
    # 然后遍历右子树（下一个兄弟节点）
    right = post_order_traversal(node.next_sibling)
    # 最后访问根节点
    return left + right + [node.value]

# 主程序
if __name__ == "__main__":
    # 读取输入
    data = [line.strip() for line in open(0).readlines()]

    # 构建树
    root = build_tree(data)

    # 后序遍历并输出
    result = post_order_traversal(root)
    print(''.join(result))