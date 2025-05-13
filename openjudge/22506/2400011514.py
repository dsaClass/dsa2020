import sys

def parse(s):
    symbols = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == '/':
            if i + 1 < n and s[i+1] == '*':
                symbols.append('/*')
                i += 2
            else:
                return None
        elif s[i] == '*':
            if i + 1 < n and s[i+1] == '/':
                symbols.append('*/')
                i += 2
            else:
                return None
        elif s[i] in '()[]':
            symbols.append(s[i])
            i += 1
        else:
            return None
    return symbols

def is_matched(symbols):
    stack = []
    mapping = {')': '(', ']': '[', '*/': '/*'}
    for sym in symbols:
        if sym in ['(', '[', '/*']:
            stack.append(sym)
        else:
            if not stack:
                return False
            top = stack.pop()
            if mapping[sym] != top:
                return False
    return len(stack) == 0

for line in sys.stdin:
    line = line.strip()
    symbols = parse(line)
    if symbols is None:
        print("False")
    else:
        print("True" if is_matched(symbols) else "False")