import itertools
s = input().strip()
for i in itertools.permutations(s):
    print(''.join(i))
