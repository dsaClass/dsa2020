class Node:
    """
    最简单的单链表结点
    属性data和next直接访问
    """
    def __init__(self, dt=None, nxt=None):
        self.data = dt
        self.next = nxt

def insertSort(header:Node):
    if header is None:
        return None
    p, q = header, header.next
    p.next = None
    while q is not None:
        n, n.next, q = q, None, q.next
        prev, i = None, p
        while i is not None and i.data <= n.data:
            prev, i = i, i.next
        if prev is not None:
            prev.next, n.next = n, i
        else:
            n.next, p = p, n
    return p

def printList(header:Node):
    l = []
    while header is not None:
        l.append(str(header.data))
        header = header.next
    print("->".join(l))

if __name__ == "__main__":
    while True:
        header = None
        for c in reversed(input()):
            header = Node(c, header)
        if header is None:
            break
        printList(header)
        printList(header := insertSort(header))
