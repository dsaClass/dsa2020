n=input()
for i in range(len(n)):
    if n[i] == '2':
        print(n[:i]+'3'+n[i+1:])
        break