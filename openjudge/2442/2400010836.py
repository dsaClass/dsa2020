a,b,c,d = [],[],[],[]
n = int(input())
for i in range(n):
    l = list(map(int,input().split()))
    a.append(l[0])
    b.append(l[1])
    c.append(l[2])
    d.append(l[3])
ans = 0
count1 = {}
for i in a:
    for j in b:
        if i+j in count1:
            count1[i+j] += 1
        else:
            count1[i+j] = 1
for i in c:
    for j in d:
        if -i-j in count1:
            ans += count1[-i-j]
print(ans)
