m, n = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))


memory = [-1] * m
memory_set = set()
# 初始化左指针
left = 0

count = 0

for word in nums:
    if word not in memory_set:
        count += 1
        if len(memory_set) == m:
            removed_word = memory[left]
            memory_set.remove(removed_word)
        memory[left] = word
        memory_set.add(word)
        # 左指针后移，若超出内存容量则回到 0 位置
        left = (left + 1) % m

print(count)