import queue

class Node:
    def __init__(self):
        self.lc = None
        self.rc = None
        self.papa = None # 记录父节点的二叉树

def wid(treeroot:Node): # 使用层次遍历（一种广度优先搜素）来改一下
    if not treeroot.lc and not treeroot.rc: #无子树，宽度为1
        return 1
    q = queue.Queue()
    q.put(treeroot)
    n = 1# 用来记录接下来的多少个是下一层的节点。
    max_w = 1
    while n != 0:
        curw = 0 # 当前这一层的宽度
        for i in range(n):
            cur = q.get()
            if cur.lc:
                q.put(cur.lc)
                curw += 1
            if cur.rc:
                q.put(cur.rc)
                curw += 1
        n = curw
        if curw > max_w: # 更新最大值
            max_w = curw
    return max_w

n = int(input())
nodes = []
Nodes = [Node() for i in range(n)]
for i in range(n):
    temp = tuple(map(int,input().split()))
    nodes.append(temp)
for i in range(n): # 建立父子关系
    if nodes[i][0] != -1:
        Nodes[i].lc = Nodes[nodes[i][0]]
        Nodes[nodes[i][0]].papa = Nodes[i]
    if nodes[i][1] != -1:
        Nodes[i].rc = Nodes[nodes[i][1]]
        Nodes[nodes[i][1]].papa = Nodes[i]
for i in Nodes:
    if i.papa is None:
        root = i # 无父节点的节点是根节点
        break
h = wid(root)
print(h)
