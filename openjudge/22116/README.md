# P0020:删除链表元素(Python版)
------

总时间限制: 1000ms 内存限制: 65536kB

### 描述

程序填空，删除链表元素
```python
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
```
```python
        // 在此处补充你的代码
```
```python
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
```

### 输入

第一行为整数t，表示有t组数据。
每组数据2行
第一行是若干个整数，构成了一张链表
第二行是若干整数，是要从链表中删除的数。

### 输出

对每组数据第二行中的每个整数x:
1) 如果链表已经为空，则输出 "EMPTY"
2) 如果x在链表中，则将其删除，并且输出删除后的链表。如果删除后链表为空，则没输出。如果有重复元素，则删前面的。
3）如果链表不为空且x不在链表中，则输出"NOT FOUND"<br>

### 样例输入
```python
2
1 2 3
3 2 2 9 5 1 1 4
1
9 88 1 23
```
### 样例输出
```python
1 2 
1 
NOT FOUND
NOT FOUND
NOT FOUND
EMPTY
EMPTY
----------------
NOT FOUND
NOT FOUND
EMPTY
----------------
```

