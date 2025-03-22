def evaluate_polish_expression(tokens):
    stack = []  # 用于存储操作数的栈
    # 从右向左遍历 tokens
    for token in reversed(tokens):
        if token in ['+', '-', '*', '/']:  # 如果是运算符
            # 弹出栈顶的两个操作数
            operand1 = stack.pop()
            operand2 = stack.pop()
            # 根据运算符进行计算
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            # 将结果压入栈中
            stack.append(result)
        else:  # 如果是操作数
            # 将操作数压入栈中
            stack.append(float(token))
    # 最终栈中剩下的唯一元素就是结果
    return stack[0]

def main():
    # 读取输入
    expression = input().strip()
    # 将输入字符串分割成 tokens
    tokens = expression.split()
    # 调用函数计算结果
    result = evaluate_polish_expression(tokens)
    # 输出结果，保留一位小数
    print('{:.1f}'.format(result))

if __name__ == "__main__":
    main()