from collections import deque

def is_valid_sequence(operations):
    q = deque()
    for op in operations:
        if op.startswith('+'):
            num = int(op[1:])
            q.append(num)
        elif op.startswith('-'):
            if not q:
                return False
            expected = int(op[1:])
            if q[0] != expected:
                return False
            q.popleft()
    return True

T = int(input())
for case in range(1, T + 1):
    n = int(input())
    ops = input().split()
    valid = is_valid_sequence(ops)
    print(f"Case {case}: {'yes' if valid else 'no'}")