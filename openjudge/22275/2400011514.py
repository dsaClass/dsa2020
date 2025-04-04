import sys
sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline())
pre = list(map(int, sys.stdin.readline().split()))

def get_post(pre_order):
    if not pre_order:
        return []
    root = pre_order[0]
    split = 1
    while split < len(pre_order) and pre_order[split] < root:
        split += 1
    left = pre_order[1:split]
    right = pre_order[split:]
    return get_post(left) + get_post(right) + [root]

post = get_post(pre)
print(' '.join(map(str, post)))