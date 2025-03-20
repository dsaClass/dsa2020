s = input()
d = {}
def steps(s):
    if s in d:
        return d[s]
    if len(s) < 2:
        d[s] = 0
        return 0
    if s[0] == s[-1]:
        d[s] = steps(s[1:-1:])
        return d[s]
    else:
        d[s] = min(steps(s[1:-1:]), steps(s[1::]), steps(s[:-1:])) + 1
        return d[s]
print(steps(s))