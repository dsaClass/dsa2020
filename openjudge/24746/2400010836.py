class Node:
	def __init__(self, data, next=None):
		self.data, self.next = data, next
class LinkList:
	def __init__(self,lst):
		self.head = Node(lst[0])
		p = self.head
		for i in lst[1:]:
			node = Node(i)
			p.next = node
			p = p.next
	def reverse(self):  #通过三个变量来回倒实现反转
		p = self.head
		q = p.next
		p.next = None
		while q != None:
			u = q.next
			q.next = p
			p = q
			q = u
		self.head = p  #不要忘记更新.head
	def print(self):
		p = self.head
		while p:
			print(p.data, end=" ")
			p = p.next
		print()
a  = list(map(int,input().split()))
a = LinkList(a)
a.reverse()
a.print()