from collections import *

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def is_present(root, value):
    if root is None:
        return False
    return root.value == value

def level_order(root):
    if root is None:
        return []
    queue = deque()
    queue.append(root)
    result = []
    while queue:
        current = queue.popleft()
        result.append(str(current.value))
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result

# 读取输入
digits = list(map(int, input().split()))
unique_digits = []
seen = set()
for d in digits:
    if d not in seen:
        seen.add(d)
        unique_digits.append(d)

# 构建二叉搜索树
root = None
for d in unique_digits:
    root = insert(root, d)

# 进行层次遍历并输出
print(' '.join(level_order(root)))