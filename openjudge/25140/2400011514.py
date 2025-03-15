from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_expression_tree(postfix):
    stack = []
    for char in postfix:
        if char.islower():  # 操作数
            stack.append(Node(char))
        else:  # 运算符
            right = stack.pop()
            left = stack.pop()
            operator_node = Node(char)
            operator_node.left = left
            operator_node.right = right
            stack.append(operator_node)
    return stack.pop()

def level_order_traversal(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def postfix_to_queue_expression(postfix):
    tree = build_expression_tree(postfix)
    level_order = level_order_traversal(tree)
    return ''.join(level_order[::-1])  # 颠倒层次遍历结果

# 读取输入
n = int(input())
for _ in range(n):
    postfix = input().strip()
    queue_expression = postfix_to_queue_expression(postfix)
    print(queue_expression)