## 002:想要插队的Y君

- 总时间限制: 1000ms 内存限制: 65536kB

- ### 描述

  很遗憾，一意孤行的Y君没有理会你告诉他的饮食计划并很快吃完了他的粮食储备。 但好在他捡到了一张校园卡，凭这个他可以偷偷混入领取物资的队伍。 为了不被志愿者察觉自己是只猫，他想要插到队伍的最中央。（插入后若有偶数个元素则选取靠后的位置） 于是他又找到了你，希望你能帮他修改志愿者写好的代码，在发放顺序的中间加上他的学号6。 你虽然不理解志愿者为什么要用链表来写这份代码，但为了不被发现只得在此基础上进行修改：
  ```python
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
  // 在此处补充你的代码
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
  ```

  

  ### 输入

  一行，若干个整数，组成一个链表。

  ### 输出

  一行，在链表中间位置插入数字6后得到的新链表

  ### 样例输入

  ```
  ### 样例输入1
  8 1 0 9 7 5
  ### 样例输入2
  1 2 3
  ```

  

  ### 样例输出

  ```
  ### 样例输出1
  8 1 0 6 9 7 5
  ### 样例输出2
  1 2 6 3
  ```

  ### 来源

  Lou Yuke