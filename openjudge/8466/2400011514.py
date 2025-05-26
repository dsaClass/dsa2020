digit_cost = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def get_cost(num):
    if num == 0:
        return digit_cost[0]
    cost = 0
    while num > 0:
        digit = num % 10
        cost += digit_cost[digit]
        num = num // 10
    return cost

n = int(input())
total = n - 4
if total < 0:
    print(0)
    exit()
elif total == 0:
    print(0)
    exit()

count = 0
max_num = 2000  # 根据实际情况调整这个值，以覆盖可能的解

for a in range(0, max_num + 1):
    cost_a = get_cost(a)
    if cost_a > total:
        continue
    for b in range(0, max_num + 1):
        cost_b = get_cost(b)
        if cost_a + cost_b > total:
            continue
        c = a + b
        cost_c = get_cost(c)
        if cost_a + cost_b + cost_c == total:
            count += 1

print(count)