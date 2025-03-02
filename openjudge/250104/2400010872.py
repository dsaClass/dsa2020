s=list(input())
for i in range(len(s)):
    if s[i]=='2':
        s[i]='3'
        break
print(int(''.join(s)))
