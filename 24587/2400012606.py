def check_good(s: str):
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for char in s:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return 'NO'
    return 'YES' if not stack else 'NO'
n = int(input())
for _ in range(n):
    print(check_good(input()))

