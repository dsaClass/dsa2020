class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None

def calculate_depth(node):
    if node is None:
        return 0
    left_depth = calculate_depth(node.left)
    right_depth = calculate_depth(node.right)
    return max(left_depth, right_depth) + 1

def build_tree(n, nodes):
    tree_nodes = [TreeNode() for _ in range(n)]
    
    for i in range(n):
        left, right = nodes[i]
        if left != -1:
            tree_nodes[i].left = tree_nodes[left - 1]
        if right != -1:
            tree_nodes[i].right = tree_nodes[right - 1]
    
    return tree_nodes[0]

def main():
    n = int(input())  # 二叉树节点个数
    nodes = []
    for _ in range(n):
        left, right = map(int, input().split())
        nodes.append((left, right))
    
    root = build_tree(n, nodes)
    depth = calculate_depth(root)
    print(depth)

if __name__ == "__main__":
    main()