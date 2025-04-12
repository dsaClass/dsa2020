import collections
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
n=int(input())
# 存储每个节点对象
nodes = [None] * (n + 1)
# 先创建所有节点对象
for i in range(1, n + 1):
    nodes[i] = TreeNode(i)
for i in range(1,n+1):
    left,right=map(int,input().split())
    if left != -1:
        nodes[i].left = nodes[left]
    if right != -1:
        nodes[i].right = nodes[right]

queue = collections.deque([nodes[1]])
level=0
while queue:
    for _ in range(len(queue)):
        cur = queue.popleft()
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    level+=1
print(level)




