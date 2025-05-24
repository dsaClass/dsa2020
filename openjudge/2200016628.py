import sys

def safe_eval(expr):
    return eval(expr)

n = int(input())
for _ in range(n):
    expr = input().strip()
    result = safe_eval(expr)
    print(f"{result:.2f}")