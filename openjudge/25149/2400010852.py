class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def build_tree(s,index):
    if index[0]>=len(s):
        return None
    current_char=s[index[0]]
    node=Node(current_char)
    index[0]+=1
    if current_char.isupper():
        node.left=build_tree(s,index)
        node.right=build_tree(s,index)
    return node

def level_order(root):
    if not root:
        return []
    queue=[root]
    result=[]
    while queue:
        node=queue.pop(0)
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
n=int(input())
for _ in range(n):
    s=input().strip()
    index=[0]
    root=build_tree(s,index)
    level=level_order(root)
    print(''.join(reversed(level)))
