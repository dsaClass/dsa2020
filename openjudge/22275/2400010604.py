def build_tree(preorder):
    if not preorder:
        return None
    root = preorder[0]
    left = [x for x in preorder if x < root]
    right = [x for x in preorder if x > root]
    return {
        'val': root,
        'left': build_tree(left),
        'right': build_tree(right)
    }

def postorder_traversal(root):
    if not root:
        return []
    return postorder_traversal(root['left']) + postorder_traversal(root['right']) + [root['val']]

n = int(input())
preorder = list(map(int, input().split()))
tree = build_tree(preorder)
postorder = postorder_traversal(tree)
print(' '.join(map(str, postorder)))