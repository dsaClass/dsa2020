
#处理多行输入
import sys
lines=[line.strip() for line in sys.stdin if line.strip()]
for line in lines:
    pass


#复杂排序：先按key1升序，再按key2降序
l=[]
def key1(x):
    pass
def key2(x):
    pass

l.sort(key=lambda x:(key1(x),key2(x)))


#多元枚举
from itertools import product
for counts in product(range(4),repeat=9):
    pass

#判断类型
if isinstance(1,int):
    pass

#完全拆解列表嵌套
def fla(lst):
    for item in lst:
        if isinstance(item, list):  # 如果当前元素仍然是列表，递归调用fla
            yield from fla(item)
        else:
            yield item
l=[i for i in fla([[[1, 2], [3, 4]], 5, [6, 7, [8, 9]]])]



#二叉堆用于找最大最小
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)

min_val = heapq.heappop(heap)  # 弹出最小值

top = heap[0]  # 查看最小值

heap = [5, 1, 3]
heapq.heapify(heap)  # 用列表建立堆
