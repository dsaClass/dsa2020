n = input()
for i in range(len(n)):
    if n[i] == '2':
        t = int(n) + 10**(len(str(n))-i-1)
        break
print(t)
