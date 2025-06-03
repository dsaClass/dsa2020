class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self,lst): #用列表创建
        self.head = Node(lst[0])
        p = self.head
        for i in lst[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def __init__(self,val=None): #用头节点创建
        if val is not None:
            self.head=Node(val)
        else:
            self.head=None

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val, end=' -> ')
            curr = curr.next
        print("None")

    def get_list(self):
        l=[]
        curr = self.head
        while curr:
            l.append(curr.data)
            curr = curr.next
        return l
    

    def insert_head(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def insert_tail(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def insert_at(self, index, val):
        if index == 0:
            self.insert_head(val)
            return
        prev = self.head
        for _ in range(index - 1):
            if not prev:
                raise IndexError("Index out of range")
            prev = prev.next
        node = Node(val)
        node.next = prev.next
        prev.next = node

    def delete_head(self):
        if self.head:
            self.head = self.head.next

    def delete_val(self, val):
        if not self.head:
            return
        if self.head.val == val:
            self.head = self.head.next
            return
        prev = self.head
        while prev.next and prev.next.val != val:
            prev = prev.next
        if prev.next:
            prev.next = prev.next.next

    def search(self, val):
        curr = self.head
        while curr:
            if curr.val == val:
                return True
            curr = curr.next
        return False

    def get(self, index):
        curr = self.head
        for _ in range(index):
            if not curr:
                raise IndexError("Index out of range")
            curr = curr.next
        if not curr:
            raise IndexError("Index out of range")
        return curr.val

    def length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    #重置链表，断开原始引用(需定义创建空链表)
    def clone(self):
        if not self.head:
            return LinkedList()
        
        new_list = LinkedList()
        new_list.head = Node(self.head.data)
        
        curr_old = self.head.next
        curr_new = new_list.head
        
        while curr_old:
            node = Node(curr_old.data)
            curr_new.next = node
            curr_new = curr_new.next
            curr_old = curr_old.next

        return new_list
    

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
    
    #不修改原链表，而是返回一个新的链表（需定义创建空链表）
    def reverse_copy(self):
        prev = None
        curr = self.head
        while curr:
            new_node = Node(curr.data)
            new_node.next = prev
            prev = new_node
            curr = curr.next
        new_list = LinkedList()
        new_list.head = prev
        return new_list
    

    # 判断是否有环
    def detect_cycle_start(head):
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        has_cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break
        
        if not has_cycle:
            return None
        
        # 找到环的起点
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


#循环单链表
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            #找到尾部节点，让新节点在尾部节点后，指向head
            current.next = new_node
            new_node.next = self.head
    
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            #让尾部节点指向新节点
            current.next = new_node
            new_node.next = self.head
            self.head = new_node
    
    def print_list(self):
        if not self.head:
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")