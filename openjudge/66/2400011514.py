n, k = map(int, input().split())
cables = []

for _ in range(n):
    s = input().strip()
    if '.' in s:
        a, b_part = s.split('.', 1)
        b = b_part.ljust(2, '0')[:2]
    else:
        a = s
        b = '00'
    cm = int(a) * 100 + int(b)
    cables.append(cm)

sum_cm = sum(cables)

if sum_cm < k:
    print("0.00")
else:
    max_cm = max(cables)
    left = 1
    right = max_cm
    res = 0
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for c in cables:
            cnt += c // mid
        if cnt >= k:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    print("{0:.2f}".format(res / 100))