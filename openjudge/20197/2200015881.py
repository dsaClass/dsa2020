m,n = map(int, input().split())
count = 1
while m -n != 0:
    count += 1
    if m > n:
        m = m - n
    elif m < n:
        n = n - m
print(count)
