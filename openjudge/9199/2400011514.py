from collections import deque

def solve():
    M, N = map(int, input().split())
    words = list(map(int, input().split()))
    
    memory = deque()
    memory_set = set()
    count = 0
    
    for word in words:
        if word in memory_set:
            continue
        else:
            count += 1
            if len(memory) >= M:
                removed_word = memory.popleft()
                memory_set.remove(removed_word)
            memory.append(word)
            memory_set.add(word)
    
    print(count)

solve()