class Node:
	def __init__(self, data, next=None):
		self.data, self.next = data, next

class LinkList:
	def __init__(self):
		self.head = None

	def initList(self, data):
		self.head = Node(data[0])
		p = self.head
		for i in data[1:]:
			node = Node(i)
			p.next = node
			p = p.next

	def insertCat(self):
		if not self.head:
			self.head=Node(6)
			return
		fast=self.head
		slow=self.head
		prev=None
		while fast and fast.next:
			prev=slow
			slow=slow.next
			fast=fast.next.next
		new=Node(6)
		if fast is not None:
			a=slow.next
			slow.next=new
			new.next=a
			
		else:
			prev.next=new
			new.next=slow
########            
	def printLk(self):
		p = self.head
		while p:
			print(p.data, end=" ")
			p = p.next
		print()

lst = list(map(int,input().split()))
lkList = LinkList()
lkList.initList(lst)
lkList.insertCat()
lkList.printLk()