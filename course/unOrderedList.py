from node import Node

class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.next

        return count

    def search(self, item):
        current = self.head
        
        while current != None:
            if current.data == item:
                return True
            current = current.next

        return False

    def remove(self, item):
        current = self.head
        previous = None
        
        while current != None:
            if current.data == item:
                break
            previous = current
            current = current.next
        else:
            return

        if previous == None:
            self.head = current.next
        else:
            previous.next=current.next

    def __str__(self):
        l = []
        p = self.head
        while p is not None:
            l.append(str(p.data))
            p = p.next
        return ' '.join(l)


if __name__ == "__main__":
    mylist = UnorderedList()
    print(mylist.head)
    mylist.add(12)
    print(mylist.size())
    print(mylist.search(12))
    print(mylist.search(11))
    mylist.remove(11)
    print(mylist.size())
    mylist.remove(12)
    print(mylist.size())

    
