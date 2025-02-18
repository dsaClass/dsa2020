n = int(input())
dic = {}
su = {}
for i in range(1, n + 1):
    dic[i] = i ** 3
for b in range(2, n + 1):
    for c in range(b, n + 1):
        for d in range(c, n + 1):
            s = dic[b] + dic[c] + dic[d]
            if s not in su:
                su[s] = [(b, c, d)]
            else:
                su[s].append((b, c, d))
for a in range(1, n + 1):
    q = dic[a]
    if q in su:
        for triple in su[q]:
            b, c, d = triple
            print(f"Cube = {a}, Triple = ({b},{c},{d})")