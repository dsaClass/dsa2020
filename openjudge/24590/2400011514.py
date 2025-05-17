def evaluate_expression(expr):
    ops = []
    values = []
    i = 0
    n = len(expr)
    
    def apply_op():
        op = ops.pop()
        b = values.pop()
        a = values.pop()
        if op == '+':
            values.append(a + b)
        elif op == '-':
            values.append(a - b)
        elif op == '*':
            values.append(a * b)
        elif op == '/':
            values.append(a / b)
    
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    while i < n:
        if expr[i] == ' ':
            i += 1
            continue
        if expr[i] == '(':
            ops.append(expr[i])
            i += 1
        elif expr[i] == ')':
            while ops and ops[-1] != '(':
                apply_op()
            ops.pop()  # 弹出左括号
            i += 1
        elif expr[i] in '+-*/':
            while (ops and ops[-1] != '(' and
                   precedence[ops[-1]] >= precedence[expr[i]]):
                apply_op()
            ops.append(expr[i])
            i += 1
        else:
            # 处理数字
            num_str = ''
            while i < n and (expr[i].isdigit() or expr[i] == '.'):
                num_str += expr[i]
                i += 1
            num = float(num_str)
            values.append(num)
    
    while ops:
        apply_op()
    
    return values[0]

n = int(input())
for _ in range(n):
    expr = input().strip()
    result = evaluate_expression(expr)
    print("{0:.2f}".format(result))