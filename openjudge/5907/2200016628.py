import sys

class Node:
    def __init__(self, val): #
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def solve():
    t = int(sys.stdin.readline())
    for test in range(t):
        n, m = map(int, sys.stdin.readline().split())
        nodes_map = [Node(i) for i in range(n)]

        for line in range(n):
            x, y, z = map(int, sys.stdin.readline().split())

            if y != -1:
                nodes_map[x].left = nodes_map[y]
                nodes_map[y].parent = nodes_map[x]
            if z != -1:
                nodes_map[x].right = nodes_map[z]
                nodes_map[z].parent = nodes_map[x]

        for op in range(m):
            op_parts = list(map(int, sys.stdin.readline().split()))
            op_type = op_parts[0]

            if op_type == 1:  #交换操作
                x, y = op_parts[1], op_parts[2]

                node_x = nodes_map[x]
                node_y = nodes_map[y]

                parent_x = node_x.parent
                parent_y = node_y.parent

                if parent_x.val==parent_y.val:
                    parent_xy = parent_x
                    if parent_xy.left==node_x:
                        parent_xy.left=node_y
                        parent_xy.right=node_x
                    else:
                        parent_xy.right=node_y
                        parent_xy.left=node_x

                else:#两节点不是一个父亲
                    if parent_x.left==node_x:#x是他父亲的左节点
                        parent_x.left = node_y
                        if parent_y.left==node_y:#y是他父亲的左节点
                            parent_y.left=node_x
                        else:#y是他父亲的右节点
                            parent_y.right=node_x
                    
                    else:#x是他父亲的右节点
                        parent_x.right=node_y
                        if parent_y.left==node_y:#y是他父亲的左节点
                            parent_y.left=node_x
                        else:#y是他父亲的右节点
                            parent_y.right=node_x
                    
                    node_x.parent=parent_y
                    node_y.parent=parent_x

            elif op_type == 2:  #查询
                x = op_parts[1]

                current_node = nodes_map[x]

                while current_node.left:
                    current_node = current_node.left

                sys.stdout.write(str(current_node.val) + "\n")


solve()