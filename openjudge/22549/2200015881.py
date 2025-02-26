s = input()
dic = {}
t = len(s) 
for i in range(t):
    if s[i] not in dic:
        dic[s[i]] = i
    else:
        dic[s[i]] = t
lis = list(dic.values())
if sum(lis) == t * len(lis):
    print(-1)
else:
    print(min(lis))
