def tokenize(s):
    tokens = []
    i = 0
    while i < len(s):
        if s[i] in '+-*/()':
            tokens.append(s[i])
            i += 1
        else:
            j = i
            while j < len(s) and (s[j].isdigit() or s[j] == '.'):
                j += 1
            tokens.append(s[i:j])
            i = j
    return tokens

n = int(input())
for _ in range(n):
    s = input().strip()
    tokens = tokenize(s)
    output = []
    stack = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    for token in tokens:
        if token.replace('.', '', 1).isdigit():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # 弹出左括号但不输出
        else:
            while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    print(' '.join(output))