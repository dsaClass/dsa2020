def calculate(exp:str) -> float:
    '''求解后序表达式的值'''

    result = exp.split()
    #用栈空间求解后缀表达式的值
    result.reverse()
    stack = []
    while result:
        i = result.pop()
        if i.replace(".","").isdigit(): stack.append(i)
        else:
            right = float(stack.pop())
            left = float(stack.pop())
            if i == "+":
                temp_result = left + right
            elif i == "-":
                temp_result = left - right
            elif i == "*":
                temp_result = left * right
            elif i == "/":
                temp_result = left / right
            stack.append(temp_result)

    return float(stack[0])

n = int(input())
for _ in range(n):
    exp = input()
    print("%.2f" % calculate(exp))
