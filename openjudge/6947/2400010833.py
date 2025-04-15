class GNode:
    def __init__(self):
        self.children = []

def build_general_tree(sequence):
    root = GNode()
    stack = [root]
    for char in sequence:
        if char == 'd':
            new_node = GNode()
            stack[-1].children.append(new_node)
            stack.append(new_node)
        elif char == 'u':
            stack.pop()
    return root

def calc_general_height(node):
    # 一般树：如果没有孩子，高度为0；否则高度为 max(孩子高度) + 1
    if not node.children:
        return 0
    return max(calc_general_height(child) for child in node.children) + 1

class BNode:
    def __init__(self):
        self.left = None   # 左儿子（第一个孩子）
        self.right = None  # 右兄弟

def convert_to_binary(g_node):
    """
    将一般树结点转换为左儿子右兄弟的二叉树结点，返回二叉树根结点
    """
    if not g_node:
        return None
    b_node = BNode()
    if g_node.children:
        # 第一个孩子转换为左儿子
        b_node.left = convert_to_binary(g_node.children[0])
        # 后续孩子作为前一个孩子的右兄弟
        current = b_node.left
        for child in g_node.children[1:]:
            current.right = convert_to_binary(child)
            current = current.right
    return b_node

def calc_binary_height(b_node):
    # 二叉树高度定义为：空树高度=-1, 单个结点高度=0
    if b_node is None:
        return -1
    left_height = calc_binary_height(b_node.left)
    right_height = calc_binary_height(b_node.right)
    return max(left_height, right_height) + 1

if __name__ == "__main__":
    sequence = input().strip()
    
    # 建立一般树并计算原树高度
    general_root = build_general_tree(sequence)
    h1 = calc_general_height(general_root)
    
    # 转换为二叉树，并计算二叉树高度
    binary_root = convert_to_binary(general_root)
    h2 = calc_binary_height(binary_root)
    
    print(f"{h1} => {h2}")