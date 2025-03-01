n = input()
print(int(n.replace('2', '3', 1)) if '2' in n else n)