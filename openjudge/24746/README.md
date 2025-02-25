P0040:颠倒链表(Python版)  
查看提交统计提问  
总时间限制: 1000ms  
内存限制: 65536kB  
描述  
填空补足链表的reverse方法，单链表颠倒过来。要求额外空间复杂度为O(1)。
####
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
        def reverse(self):
// 在此处补充你的代码
####
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
输入  
一行，不超过1000个整数，是一张链表的内容  
输出  
用从右到左顺序输出输入的那行整数  
样例输入  
1 2 3 4 5  
样例输出  
5 4 3 2 1  
来源  
Guo Wei  