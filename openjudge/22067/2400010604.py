stack = []
min_stack = []

def push(n):
    stack.append(n)
    if not min_stack or n <= min_stack[-1]:
        min_stack.append(n)

def pop():
    if stack:
        val = stack.pop()
        if val == min_stack[-1]:
            min_stack.pop()

def get_min():
    if min_stack:
        print(min_stack[-1])

# 读取输入并处理
import sys
for line in sys.stdin:
    command = line.strip().split()
    if not command:
        continue
    if command[0] == 'push':
        n = int(command[1])
        push(n)
    elif command[0] == 'pop':
        pop()
    elif command[0] == 'min':
        get_min()