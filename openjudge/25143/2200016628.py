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


def count_leaves_and_get_height(root):
    if not root:
        return 0, -1
    queue = collections.deque([root])
    height = -1
    leaves = 0
    while queue:
        level_size = len(queue)
        height += 1
        for _ in range(level_size):
            node = queue.popleft()
            if not node.left and not node.right:
                leaves += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return leaves, height


n = int(input())
root = build_tree(n)
leaves, height = count_leaves_and_get_height(root)
print(f"{height} {leaves}")
    