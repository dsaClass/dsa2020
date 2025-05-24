pairs = {')': '(', ']': '[', '*/': '/*'}
openers = pairs.values()  # '(', '[', '/*'

while True:
    try:
        s = input().strip()
        stack = []
        valid = True
        i = 0

        while i < len(s):
            if s[i] in '()[]':
                token = s[i]
                i += 1
            elif s[i:i+2] in ('/*', '*/'):
                token = s[i:i+2]
                i += 2
            else:
                valid = False  # 非法字符（比如孤立的 * 或 /）
                break

            if token in openers:
                stack.append(token)
            elif token in pairs: 
                if not stack or stack[-1] != pairs[token]:
                    valid = False  
                    break
                stack.pop()

        if valid and not stack:
            print(True)
        else:
            print(False)

    except EOFError:
        break
