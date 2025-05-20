from collections import deque

def create_tree(postorder:str,inorder:str):
    if not postorder or not inorder:
        return []
    root = postorder[-1]
    index = inorder.index(root)
    post_l = postorder[0:index]
    post_r = postorder[index:-1]
    in_l = inorder[:index]
    in_r = inorder[index+1:]
    return [root,create_tree(post_l,in_l),create_tree(post_r,in_r)]

def cengxu(lst):
    q = deque([lst])
    re = ""
    while q:
        current = len(q)
        for i in range(current):
            node = q.popleft()
            re += node[0]
            if node[1]:
                q.append(node[1])
            if node[2]:
                q.append(node[2])
    return re

n = int(input().strip())
for _ in range(n):
    in1 = input().strip()
    post = input().strip()
    print(cengxu(create_tree(post,in1)))
