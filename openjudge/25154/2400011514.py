def count_trees(pre, post):
    n = len(pre)
    if n != len(post):
        return 0
    if n == 0:
        return 1
    if pre[0] != post[-1]:
        return 0
    if n == 1:
        return 1
    # Check for left_root in post
    left_root = pre[1]
    try:
        j = post.index(left_root, 0, n-1)  # Search in post[0..n-2]
    except ValueError:
        return 0
    left_size = j + 1
    left_pre = pre[1: 1 + left_size]
    left_post = post[:j+1]
    right_pre = pre[1 + left_size:]
    right_post = post[j+1: n-1]
    # Check if left and right roots are valid
    if len(left_pre) > 0 and left_pre[0] != left_post[-1]:
        return 0
    if len(right_pre) > 0:
        if len(right_post) == 0 or right_pre[0] != right_post[-1]:
            return 0
    # Recursive calls
    left = count_trees(left_pre, left_post)
    if left == 0:
        return 0
    right = count_trees(right_pre, right_post)
    if right == 0:
        return 0
    res = left * right
    # Multiply by 2 if right subtree is empty
    if len(right_pre) == 0:
        res *= 2
    return res

import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split()
    if len(parts) != 2:
        print(0)
        continue
    pre, post = parts
    if len(pre) != len(post):
        print(0)
        continue
    if len(set(pre)) != len(pre) or len(set(post)) != len(post):
        print(0)
        continue
    if pre[0] != post[-1]:
        print(0)
        continue
    print(count_trees(pre, post))