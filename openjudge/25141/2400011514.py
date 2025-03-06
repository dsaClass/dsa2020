class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.left_processed = False
        self.right_processed = False

def build_tree(lines):
    root = None
    level_parents = {}  # 保存各层级当前的父节点
    for line in lines:
        if not line.strip():
            continue
        stripped_line = line.lstrip('\t')
        t = len(line) - len(stripped_line)
        val = stripped_line.strip()
        if t == 0:
            root = Node(val)
            level_parents = {0: root}
        else:
            parent_level = t - 1
            if parent_level not in level_parents:
                continue  # 输入错误，但题目保证输入合法
            parent = level_parents[parent_level]
            if not parent.left_processed:
                if val == '*':
                    parent.left = None
                    parent.left_processed = True
                else:
                    node = Node(val)
                    parent.left = node
                    parent.left_processed = True
                    level_parents[t] = node
            else:
                if val == '*':
                    continue  # 右子节点不能为*，题目保证输入合法
                node = Node(val)
                parent.right = node
                parent.right_processed = True
                level_parents[t] = node
    return root

def preorder(root):
    if not root:
        return ''
    res = root.val
    res += preorder(root.left)
    res += preorder(root.right)
    return res

def inorder(root):
    if not root:
        return ''
    res = inorder(root.left)
    res += root.val
    res += inorder(root.right)
    return res

def postorder(root):
    if not root:
        return ''
    res = postorder(root.left)
    res += postorder(root.right)
    res += root.val
    return res

# 读取输入并处理
import sys
lines = [line.rstrip('\n') for line in sys.stdin]

root = build_tree(lines)

print(preorder(root))
print(inorder(root))
print(postorder(root))