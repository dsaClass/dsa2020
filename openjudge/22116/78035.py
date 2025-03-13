class Node:
    def __init__(self, data, next=None):
        self.data, self.next = data, next
class LinkList:  #循环链表
    def __init__(self):
        self.tail = None
        self.size = 0
    def isEmpty(self):
        return self.size == 0
    def pushFront(self,data):
        nd = Node(data)
        if self.tail == None:
            self.tail = nd
            nd.next = self.tail
        else:
            nd.next = self.tail.next
            self.tail.next = nd
        self.size += 1
    def pushBack(self,data):
        self.pushFront(data)
        self.tail = self.tail.next
    def popFront(self):
        if self.size == 0:
            return None
        else:
            nd = self.tail.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
            else:
                self.tail.next = nd.next
        return nd.data
    def printList(self):
        if self.size > 0:
            ptr = self.tail.next
            while True:
                print(ptr.data,end = " ")
                if ptr == self.tail:
                    break
                ptr = ptr.next
            print("")

    def remove(self,data):
        if self.isEmpty():
            return None
        p=self.tail
        #链表不为空，访问self.tail.next才安全
        c=self.tail.next
        for _ in range(self.size):
            if c.data==data:
                if self.size == 1:
                    #删除唯一结点
                    self.tail = None
                elif c is self.tail:
                    self.tail=p
                self.size -= 1
                p.next =c.next
                return True
            c=c.next
            p=p.next
        else:
            return False

t = int(input())
for i in range(t):
    lst = list(map(int,input().split()))
    lkList = LinkList()
    for x in lst:
        lkList.pushBack(x)
    lst = list(map(int,input().split()))
    for a in lst:
        result = lkList.remove(a)
        if result == True:
            lkList.printList()
        elif result == False:
            print("NOT FOUND")
        else:
            print("EMPTY")
    print("----------------")
