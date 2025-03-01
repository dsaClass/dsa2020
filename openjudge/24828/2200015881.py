# 姓名：杨济泽 学号：2200015881
# 本题逻辑比较简单，但是最大的问题是提高运行效率，因此采用了滑动窗口的维护
# 通过弹出非极值减少内存，从而加快运行效率
n, k = map(int, input().split())
dat = list(map(int, input().split()))
min_queue = []
max_queue = []
s_min = []
s_max = []
for i in range(n):
    while min_queue and dat[min_queue[-1]] > dat[i]:
        min_queue.pop()
    min_queue.append(i)
    while max_queue and dat[max_queue[-1]] < dat[i]:
        max_queue.pop()
    max_queue.append(i)
    if i >= k - 1:
        s_min.append(dat[min_queue[0]])
        s_max.append(dat[max_queue[0]])
        if min_queue[0] == i - k + 1:
            min_queue.pop(0)
        if max_queue[0] == i - k + 1:
            max_queue.pop(0)
for value in s_min:
    print(value, end=' ')
print()
for value in s_max:
    print(value, end=' ')
