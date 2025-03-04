def count_possible_trees(preorder, postorder):
    if len(preorder) != len(postorder):
        return 0
    if len(set(preorder)) != len(preorder) or len(set(postorder)) != len(postorder):
        return 0
    if not preorder:
        return 1
    if preorder[0] != postorder[-1]:
        return 0
    if len(preorder) == 1:
        return 1
    
    root = preorder[0]
    left_pre = []
    left_post = []
    count = 0
    
    for i in range(len(preorder)):
        left_pre = preorder[1:i+1]
        left_post = postorder[:i]
        right_pre = preorder[i+1:]
        right_post = postorder[i:-1]
        
        if set(left_pre) == set(left_post) and set(right_pre) == set(right_post):
            count += count_possible_trees(left_pre, left_post) * count_possible_trees(right_pre, right_post)
    
    return count

def main():
    import sys
    for line in sys.stdin:
        preorder, postorder = line.strip().split()
        print(count_possible_trees(preorder, postorder))

if __name__ == "__main__":
    main()