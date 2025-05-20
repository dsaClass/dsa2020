def max_height(n):
    s = [0, 1]
    h = 2
    while True:
        next_val = 1 + s[h - 1] + s[h - 2]
        if next_val > n:
            return h - 1
        s.append(next_val)
        h += 1

n = int(input())
print(max_height(n))
