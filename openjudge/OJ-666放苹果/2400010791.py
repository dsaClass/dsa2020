def f(m, n):
    if n == 1 or m == 1 or m == 0:
        return 1
    elif m < 0 or n <= 0:
        return 0
    elif m == 2:
        return 2
    else:
        return f(m, n - 1) + f(m - n, n)


t = int(input())
for _ in range(0, t):
    a = input().split(" ")
    p = int(a[0])
    q = int(a[1])
    k = f(p, q)
    print(k)