# P0050:寻找链表交叉点(Python版)
总时间限制: 1000ms 内存限制: 65536kB
## 描述
两个单链表，从某个结点开始，后面所有的结点都是两者共享的(类似于字母Y形状)。请设计O(n)算法求两者共享的第一个结点(n是两者中间较长的链表的长度)。

请填空补齐寻找第一个共享结点的 findJointPoint 函数

不必阅读 genLinkList函数，只要知道它返回两个交叉成Y字形的链表a和b即可。
```
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

def genLinkList():
	a  = list(map(int,input().split()))
	b =  list(map(int,input().split()))
	n = int(input())
	la = LinkList(a)
	lb = LinkList(b)
	p = la.head
	last = None
	while p is not None:
		last = p
		p = p.next
	p = lb.head
	for i in range(n-1):
		p = p.next
	last.next = p
	return la,lb
a,b = genLinkList()
def findJointPoint(a,b):
// 在此处补充你的代码
print(findJointPoint(a,b))
```
## 输入
第1行：不超过100000个整数，是链表a最初的内容
第2行：不超过100000个整数，是链表b的内容
第3行：整数n。表示程序会将链表a的最后一个结点的next指针指向链表b的第n个结点（结点编号从1开始算），这样链表a就被延长了，和b一起形成了Y字形状，而且链表b的第n个结点就成为Y字形的分叉点。
## 输出
链表b的第n个结点
## 样例输入
1 2 3 4 5
7 8 9 10 11
3
## 样例输出
9
