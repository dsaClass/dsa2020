n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
up = [(1e10,n)]
ans = 0
for i in range(n-1,-1,-1):
    for k in range(len(up)-1,-1,-1):
        if l[i] > up[k][0]:
            up.pop()
        else:
            up.append((l[i],i))
            ans += (up[k][1]-i)
            break
print(ans-n)