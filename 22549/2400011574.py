s=input()
dic={}
n=len(s)
for i in range(n):
    if s[i] in dic:
        dic[s[i]].append(i)
    else:
        dic[s[i]]=[i]
result=float('inf')
for t in dic:
    if len(dic[t])==1:
        result=dic[t]
        break
if result==float('inf'):
    print('-1')
else:
    for k in result:
        print(k)