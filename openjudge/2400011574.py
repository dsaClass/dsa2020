import sys
sys.setrecursionlimit(10**7)

inorder = input().strip()
postorder = input().strip()

# 建树
def build(in_l, in_r, post_l, post_r):
    if in_l > in_r:
        return None
    root_val = postorder[post_r]
    root = {'val': root_val, 'left': None, 'right': None}
    root_idx = inorder_index[root_val]
    left_size = root_idx - in_l
    root['left'] = build(in_l, root_idx - 1, post_l, post_l + left_size - 1)
    root['right'] = build(root_idx + 1, in_r, post_l + left_size, post_r - 1)
    return root

def print_tree(node, level):
    if not node:
        return
    # 打印当前节点
    print('\t' * level + node['val'])
    left = node['left']
    right = node['right']
    if left is None and right is not None:
        # 空左子树用*表示
        print('\t' * (level + 1) + '*')
        print_tree(right, level + 1)
    else:
        if left:
            print_tree(left, level + 1)
        if right:
            print_tree(right, level + 1)

# 预处理字母在中序中的索引，便于快速切分
inorder_index = {c: i for i, c in enumerate(inorder)}

root = build(0, len(inorder) - 1, 0, len(postorder) - 1)
print_tree(root, 0)








