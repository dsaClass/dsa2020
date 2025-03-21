class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def build_tree(lines):
    root = None
    stack = []  # 用于维护当前路径上的节点
    for line in lines:
        indent = len(line) - len(line.lstrip())  # 计算缩进量
        node = TreeNode(line.strip())  # 创建当前节点
        while stack and stack[-1][1] >= indent:  # 如果栈顶节点的缩进大于等于当前节点的缩进，弹出
            stack.pop()
        if stack:  # 如果栈不为空，说明当前节点有父节点
            parent = stack[-1][0]
            parent.children.append(node)
        else:  # 如果栈为空，说明当前节点是根节点
            root = node
        stack.append((node, indent))  # 将当前节点及其缩进压入栈
    return root

def preorder_traversal(node, result):
    if not node:
        return
    result.append(node.value)
    for child in node.children:
        preorder_traversal(child, result)

def postorder_traversal(node, result):
    if not node:
        return
    for child in node.children:
        postorder_traversal(child, result)
    result.append(node.value)

def main():
    lines = []
    while True:
        try:
            line = input()
            if not line.strip():  # 如果输入为空行，结束输入
                break
            lines.append(line)
        except EOFError:
            break

    root = build_tree(lines)
    preorder_result = []
    postorder_result = []

    preorder_traversal(root, preorder_result)
    postorder_traversal(root, postorder_result)

    print(''.join(preorder_result))
    print(''.join(postorder_result))

if __name__ == "__main__":
    main()