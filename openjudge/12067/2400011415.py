nl, kl, al, bl = [], [], [], []
while True:
    n, k = [int(i) for i in input().split()]
    if n == 0 and k == 0:
        break
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    nl.append(n)
    kl.append(k)
    al.append(a)
    bl.append(b)

def max_score(n, k, a, b):
    dp = [0] * (k + 1)
    for i in range(n):
        