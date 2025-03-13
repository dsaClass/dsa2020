s=input()
for i in range(len(s)):
    if s[i]=='2':
        result=s[:i]+'3'+s[i+1:]
        break
try:
    print(result)
except:
    print(s)