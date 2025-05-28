import sys
from collections import deque

class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
        self.l_process=None
        self.r_process=None

class FenwickTree:
    def __init__(self,dat):
        self.root=Node(dat)
        self.nodes={self.root.data:self.root}

    def add(self,parent,symbol):
        if symbol=='*':
            parent_node = self.nodes[parent]
            parent_node.l_process=True
            return

        if symbol not in self.nodes:
            self.nodes[symbol]=Node(symbol)
        new_node=self.nodes[symbol]
        parent_node=self.nodes[parent]
        if not parent_node.l_process:
            parent_node.left=new_node
            parent_node.l_process=True
        else:
            parent_node.right=new_node

    def pre_order(self,res,cur):
        if cur==None:
            return
        res.append(str(cur.data))
        self.pre_order(res,cur.left)
        self.pre_order(res,cur.right)
        return res

    def in_order(self,res,cur):
        if cur==None:
            return
        self.in_order(res,cur.left)
        res.append(str(cur.data))
        self.in_order(res,cur.right)
        return res

    def post_order(self,res,cur):
        if cur==None:
            return
        self.post_order(res,cur.left)
        self.post_order(res,cur.right)
        res.append(str(cur.data))
        return res

def main():
    n=int(input())
    for i in range(n):
        if i:
            print()
        stack=deque()
        processed=[]
        while True:
            line=sys.stdin.readline().strip()
            level=len(line)-1
            if level==0 and line[0]=='0':
                break
            symbol=line[level]
            stack.append((level,symbol))

        while len(stack)>0:
            level, symbol=stack.popleft()
            if level==0:
                tree=FenwickTree(symbol)
            else:
                while level-1!=processed[-1][0]:
                    processed.pop()
                tree.add(processed[-1][1],symbol)
            processed.append((level,symbol))

        print(''.join(tree.pre_order([],tree.root)))
        print(''.join(tree.post_order([], tree.root)))
        print(''.join(tree.in_order([], tree.root)))


if __name__ == '__main__':
    main()