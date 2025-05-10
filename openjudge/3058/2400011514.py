n = int(input())
h = [int(input()) for _ in range(n)]
stack = []
total = 0

for i in range(n-1, -1, -1):
    while stack and h[stack[-1]] < h[i]:
        stack.pop()
    if not stack:
        j = n
    else:
        j = stack[-1]
    total += j - i - 1
    stack.append(i)

print(total)