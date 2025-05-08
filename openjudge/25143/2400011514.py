n = int(input())
children = []
child_set = set()

for _ in range(n):
    left, right = map(int, input().split())
    children.append((left, right))
    if left != -1:
        child_set.add(left)
    if right != -1:
        child_set.add(right)

# 找到根节点
root = (set(range(n)) - child_set).pop()

from collections import deque

queue = deque()
queue.append((root, 1))
max_depth = 0
leaf_count = 0

while queue:
    node, depth = queue.popleft()
    left, right = children[node]
    
    # 检查是否是叶节点
    if left == -1 and right == -1:
        leaf_count += 1
    
    # 更新最大深度
    if depth > max_depth:
        max_depth = depth
    
    # 处理左子节点
    if left != -1:
        queue.append((left, depth + 1))
    
    # 处理右子节点
    if right != -1:
        queue.append((right, depth + 1))

height = max_depth - 1
print(height, leaf_count)