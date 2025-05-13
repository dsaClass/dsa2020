m, n = map(int,input().split())
words = input().split()
ram = [None] * (m + 1) # 使用足够大的列表实现的循环链表表示内存。这样可以实现高效的队列。
ramset = set() # 使用一个集合来存储内存中的数据，以便实现O(1)的查找操作。
head = 0 # 环形队列的头指针
rear = 0 # 环形队列的尾指针
cnt = 0
for i in words:
    if i not in ramset: # 这个词不在内存里
        if (rear + 1) % (m + 1) != head: # 内存未满
            ram[rear] = i
            rear = (rear + 1) % (m + 1) # 入队
            ramset.add(i) # 加入集合
        else: # 内存已满
            ramset.discard(ram[head]) # 从集合中删去
            head = (head + 1) % (m + 1) # 出队
            ram[rear] = i # 出队
            rear = (rear + 1) % (m + 1)
            ramset.add(i) # 加入集合
        cnt += 1 # 查词典数加一
    else: # 这个词在内存里
        pass
print(cnt)
