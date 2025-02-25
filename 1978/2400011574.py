#方法一
import math
def lcm(a, b):
    return a * b // math.gcd(a, b)
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1
def find_next_triple_peak(p, e, i):
    m1, m2, m3 = 23, 28, 33
    M = lcm(lcm(m1, m2), m3)
    M1, M2, M3 = M // m1, M // m2, M // m3
    y1, y2, y3 = mod_inverse(M1, m1), mod_inverse(M2, m2), mod_inverse(M3, m3)

    n = (p * M1 * y1 + e * M2 * y2 + i * M3 * y3) % M
    return n, M
p, e, i, d = map(int, input().split())
n, M = find_next_triple_peak(p, e, i)
if n <= d:
        n += M
print(n-d)

#方法二
s=list(map(int,input().split()))
p=s[0]%23
e=s[1]%28
i=s[2]%33
d=s[3]
for n in range(d+1,d+21253):
    if (n-p)%23 == 0 and (n-e)%28 == 0 and (n-i)%33 ==0:
        a=n-d
        break
print(a)