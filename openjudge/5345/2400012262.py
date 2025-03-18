n, m_ops = map(int, input().split())
x_list = list(map(int, input().split()))

pre_list = []
for i in range(16):
    m = 1 << (i + 1)
    cnt = [0] * m
    for x in x_list:
        r = x % m
        cnt[r] += 1
    pre = [0] * m
    pre[0] = cnt[0]
    for r in range(1, m):
        pre[r] = pre[r - 1] + cnt[r]
    pre_list.append(pre)

D = 0  

for _ in range(m_ops):
    parts = input().split()
    if parts[0] == 'C':
        d = int(parts[1])
        D = (D + d) % 65536
    else:
        i = int(parts[1])
        m = 1 << (i + 1)
        threshold = 1 << i
        b = D % m
        s = (threshold - b) % m
        e = (m - 1 - b) % m
        pre = pre_list[i]
        
        if s <= e:
            if s == 0:
                total = pre[e]
            else:
                total = pre[e] - pre[s - 1]
        else:
            part1 = pre[m - 1]
            if s > 0:
                part1 -= pre[s - 1]
            part2 = pre[e] if e >= 0 else 0
            total = part1 + part2
        print(total)
