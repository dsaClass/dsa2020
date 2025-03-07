sign = {'+', '-', '*', '/'}

def cal(a, b, char):
    a, b = float(a), float(b)
    if char == '+':
        return a + b
    elif char == '-':
        return a - b
    elif char == '*':
        return a * b
    else:
        return a / b

def polish(s):
    stack = []
    for token in reversed(s):  # 逆序遍历波兰表达式
        if token in sign:
            a = stack.pop()
            b = stack.pop()
            stack.append(cal(a, b, token))
        else:
            stack.append(token)  # 数字直接入栈
    print(f'{stack[0]:.6f}')  # 保持 6 位小数输出

# 读取输入并拆分
s = input().split()
polish(s)