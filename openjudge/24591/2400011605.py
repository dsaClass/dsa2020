def convert(exp:str) -> str:
    '''中序表达式转化为后缀表达式'''

    #表达式字符串转化为表格
    initial_list = []
    temp = ""
    for i in exp:
        if i.isdigit() or i == ".": temp = temp + i
        else:
            if temp: initial_list.append(temp)
            temp = ""
            initial_list.append(i)
    if temp: initial_list.append(temp) #如果最后是数字，那么再把最后的temp放入list中
    
    #依据括号和运算优先级转化为后缀表达式
    precedence = {"+":1, "-":1, "*":2, "/":2}
    operators= []
    result = []
    for i in initial_list:
        if i.replace(".","").isdigit():
            result.append(i)
        elif i == "(":
            operators.append(i)
        elif i == ")":
            top = operators.pop()
            while top != "(":
                result.append(top)
                top = operators.pop()
        else:
            while operators and precedence.get(operators[-1], 0) >= precedence.get(i, 0):
                result.append(operators.pop())
            operators.append(i)
    while operators:
        result.append(operators.pop())

    return " ".join(result)

n = int(input())
for _ in range(n):
    exp = input()
    print(convert(exp))
