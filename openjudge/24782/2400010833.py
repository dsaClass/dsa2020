# 2400010833 闵诗珈
def PKU(s):
    stack = []
    for char in s:
        stack.append(char)
        if len(stack) >= 3 and ''.join(stack[-3:]) == 'PKU':
            stack.pop()
            stack.pop()
            stack.pop()

    return ''.join(stack)
print(PKU(input()))