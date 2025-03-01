from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def build_tree(sequence):
    if not sequence:
        return None
    
    nodes = deque()
    root = Node(sequence[0])
    nodes.append((root, sequence[1]))
    
    i = 2
    while i < len(sequence):
        current, degree = nodes.popleft()
        for _ in range(degree):
            child = Node(sequence[i])
            current.children.append(child)
            nodes.append((child, sequence[i+1]))
            i += 2
    return root

def post_order_traversal(root):
    result = []
    if root:
        for child in root.children:
            result.extend(post_order_traversal(child))
        result.append(root.value)
    return result

def main():
    n = int(input())
    forest = []
    for _ in range(n):
        sequence = input().split()
        sequence = [s if idx % 2 == 0 else int(s) for idx, s in enumerate(sequence)]
        root = build_tree(sequence)
        forest.append(root)
    
    result = []
    for tree in forest:
        result.extend(post_order_traversal(tree))
    
    print(' '.join(result))

if __name__ == "__main__":
    main()