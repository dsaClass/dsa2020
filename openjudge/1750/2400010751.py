def permute(s, path, used):
    if len(path) == len(s):
        print(''.join(path))
        return

    for i in range(len(s)):
        if not used[i]:
            used[i] = True
            permute(s, path + [s[i]], used)
            used[i] = False
s = input().strip()
permute(sorted(s), [], [False] * len(s))
