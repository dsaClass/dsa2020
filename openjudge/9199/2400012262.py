from collections import OrderedDict
def machine_translation(M,words):
    memory = OrderedDict()
    dictionary_lookup_count = 0
    for word in words:
        if word in memory:
            continue
        else:
            dictionary_lookup_count += 1
            if len(memory) >= M:
                memory.popitem(last=False)
            memory[word] = None
    return dictionary_lookup_count

M, N = map(int, input().split())  
words = list(map(int, input().split()))  

result = machine_translation(M, words)
print(result)
