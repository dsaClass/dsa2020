# P0060:链表寻环

总时间限制: 2000ms 内存限制: 655360kB
## 描述
请设计时间复杂度O(n)的算法判断一个单链表是否有环。要求额外空间复杂度O(1)。
```
import random
class Node:
	def __init__(self, data, next=None):
		self.data, self.next = data, next
class LinkList:
	def __init__(self,lst):
		self.head = Node(lst[0])
		p = self.head
		L = len(lst)
		for i in range(1,L):
			node = Node(lst[i])
			p.next = node
			p = p.next
	def loopExists(self):
		p1 = self.head
		p2 = self.head.next
		if p2 is not None:
			p2 = p2.next
		while p1 is not None and p2 is not None:
			p1 = p1.next
			p2 = p2.next
			if p2 is not None:
				p2 = p2.next
			if p1 is p2:
				return True
		return False

	def loopExists1(self):
// 在此处补充你的代码
####
while True:
	try:
		n,m = map(int,input().split())
	except:
		break
	a = [i for i in range(n+10)]
	random.shuffle(a)
	lst  = LinkList(a)
	if m == 1:
		if n > 10:
			pos = random.randint(0,n-5)
		else:
			pos = 0
		p = lst.head
		q = p
		for i in range(pos):
			q = q.next
		last = None
		while p is not None:
			last = p
			p = p.next
		last.next = q
	print(lst.loopExists())
```
## 输入
若干行。
每行有两个整数n和m，表示一个长度为n的链表。m为1表示该链表有环，为0表示该链表无环。
## 输出
对每张链表，如果有环输出"True"如果五环输出"False"。注意大小写。
## 样例输入
10 1
999992 1
20 0
3 0
## 样例输出
True
True
False
False