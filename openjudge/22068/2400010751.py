def check_pop_sequence(origin, target):
    stack = []  # 模拟栈，用于存储压入的字符
    i = 0  # 指向 origin 的索引，用于逐步压栈
    for t in target:
        while i < len(origin) and (not stack or stack[-1] != t):
            stack.append(origin[i])  
            i += 1  
        if stack and stack[-1] == t:
            stack.pop()
        else:
            return "NO"
    if len(origin) != len(target):
        return "NO"
    return "YES"
origin = input()
while True:
    try:
        target = input()  
        print(check_pop_sequence(origin, target)) 
    except EOFError:
        break  
