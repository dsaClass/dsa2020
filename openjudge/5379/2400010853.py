n= int(input())
for i in range(n):
    n = int(input())
    operations = input().split()
    queue = []
    is_valid = True
    for op in operations:
        if op[0] == '+':
            queue.append(int(op[1:]))
        elif op[0] == '-':
            if not queue or queue[0] != int(op[1:]):
                is_valid = False
                break
            else:
                queue.pop(0)
    if is_valid:
        print(f"Case {i+1}: yes")
    else:
        print(f"Case {i+1}: no")