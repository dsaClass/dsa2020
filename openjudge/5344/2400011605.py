class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Linklist:
    def __init__(self, lst):
        self.head = Node(lst[0])
        last = self.head
        for i in lst[1:]:
            node = Node(i)
            last.next = node
            last = node
        last.next = self.head
    
    def killed(self, k):
        Killed = []
        while self.head.next != self.head:
            count = self.head
            for _ in range(k - 1):
                previous = count
                count = count.next
            previous.next = count.next
            self.head = count.next
            Killed.append(count.value)
        return Killed
            

n, k = map(int, input().split())
linklist = Linklist(list(range(1, n + 1)))
print(*linklist.killed(k), sep = " ")