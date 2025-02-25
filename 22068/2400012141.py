def popsequence(x, seq):
    stack = []
    idx = 0  # 记录压入栈的字符位置
    for char in seq:    # 模拟压栈和出栈
        while idx < len(x) and (not stack or stack[-1] != char):        # 压栈：直到栈顶是目标字符
            stack.append(x[idx])
            idx += 1
        if stack and stack[-1] == char:
            stack.pop()  # 出栈
        else:# 如果栈顶不是当前要出栈的字符，说明不合法
            return "NO"
    if len(x)!=len(seq): return "NO"
    return "YES"
x = input()
result=[]
while True:
    try:
        seq = input()
        print(popsequence(x, seq))
    except EOFError:
        break
