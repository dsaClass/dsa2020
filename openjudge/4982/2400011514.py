n = int(input())
if n == 0:
    print(1)
else:
    a, b = 1, 2
    for _ in range(n-1):
        new_a = a + b
        new_b = 2 * a + b
        a, b = new_a, new_b
    print(a + b)