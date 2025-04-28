scores = list(map(float, input().split()))
n = len(scores)
required = 0.6 * n

left = 1
right = 10**9
answer = 10**9  # 初始设为最大值

while left <= right:
    mid = (left + right) // 2
    a = mid / 10**9
    count = 0
    
    for x in scores:
        adjusted = x * a + 1.1 ** (a * x)
        if adjusted >= 85:
            count += 1
    
    if count >= required:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)