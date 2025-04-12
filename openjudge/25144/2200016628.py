import collections

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(n):
    nodes = [TreeNode(i) for i in range(n)]
    children = set()
    for i in range(n):
        left, right = map(int, input().split())
        if left != -1:
            nodes[i].left = nodes[left]
            children.add(left)
        if right != -1:
            nodes[i].right = nodes[right]
            children.add(right)
    for i in range(n):
        if i not in children:
            return nodes[i]
    return None

def tree_width(root):
    if not root:
        return 0
    queue = collections.deque([root])
    max_width = 0
    while queue:
        max_width = max(max_width, len(queue))
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return max_width

n = int(input())
root = build_tree(n)
width = tree_width(root)
print(width)
    