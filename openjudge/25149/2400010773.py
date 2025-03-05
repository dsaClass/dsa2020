class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(prefix):
    stack = []
    for char in prefix[::-1]:
        node = TreeNode(char)
        if char.isupper():
            node.left = stack.pop()
            node.right = stack.pop()
        stack.append(node)
    return stack[0]

def level_order_traversal(root):
    queue = [root]
    traversal = []
    while queue:
        node = queue.pop(0)
        traversal.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return traversal

n = int(input().strip())
for _ in range(n):
    prefix = input().strip()
    root = build_tree(prefix)
    queue_expression = level_order_traversal(root)[::-1]
    print(''.join(queue_expression))