class Node:
    def __init__(self, data, next=None):
        self.data, self.next = data, next

class LinkList:
    def __init__(self, lst):
        self.head = Node(lst[0])
        p = self.head
        for i in lst[1:]:
            node = Node(i)
            p.next = node
            p = p.next

def genLinkList():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    n = int(input())
    la = LinkList(a)
    lb = LinkList(b)
    p = la.head
    last = None
    while p is not None:
        last = p
        p = p.next
    p = lb.head
    for i in range(n - 1):
        p = p.next
    last.next = p
    return la, lb

a, b = genLinkList()

def findJointPoint(a, b):
    def getLength(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    lenA = getLength(a.head)
    lenB = getLength(b.head)

    pA, pB = a.head, b.head

    # Move the longer list's pointer ahead by the difference in lengths
    if lenA > lenB:
        for _ in range(lenA - lenB):
            pA = pA.next
    else:
        for _ in range(lenB - lenA):
            pB = pB.next

    # Move both pointers until they meet
    while pA != pB:
        pA = pA.next
        pB = pB.next

    return pA.data

print(findJointPoint(a, b))