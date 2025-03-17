class Node: # 节点类，含有一个值和一个指针。
    def __init__(self, value, pointer):
        self.value = value
        self.pointer = pointer

class CLinkList: # 循环链表类
    def __init__(self, lst): # 初始化，使用lst中的内容建立一个循环链表。
        self.head = Node(lst[0], None)
        self.current = self.head # 创建头部
        a = self.head
        for i in lst[1:]: # 新建一个节点，然后把刚刚最后一个节点的指针连到这新的节点。
            b = Node(i, None)
            a.pointer = b
            a = b
        a.pointer = self.head # 把最后一个建立的节点的指针连到头节点上面，构成循环链表。
    def deleteandprint(self, numpass): # 删除越过k-1个节点后面的那个节点并且输出。
        for i in range(numpass):
            self.current = self.current.pointer # 每运行一次，current会变成后一个节点一次。
        print(self.current.pointer.value, end='') # 按照所想要的格式打印出被删掉的节点的value。
        self.current.pointer = self.current.pointer.pointer # 把current节点的pointer连接到被删掉的那个节点的指针所指的节点，相当于把current的pointer原来所指的节点删除出循环链表。
    def is1left(self): # 查看循环链表里是否只剩下一个元素。
        return self.current.pointer == self.current # 如果current节点的指针所指的是它自己，说明只剩下一个元素，返回True。

n, k = map(int, input().split())
l = list(range(1, n + 1))
people = CLinkList(l) # 建立有n个人的循环链表，每个节点的值是这个人的编号。
people.deleteandprint(k - 2) # 第一次越过k - 2个人，然后把后面那个人干掉
while not people.is1left():
    print(' ', end='') # 剩下每次越过k - 1个人然后把后面那个人干掉，直到只剩下最后一个人。
    people.deleteandprint(k - 1)
