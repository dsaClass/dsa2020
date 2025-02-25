n = int(input())
l = list(map(int,input().split()))
ans = [1]
for i in range(1,len(l)):
    m = 0
    for j in range(i):
        if l[i] > l[j] and ans[j] > m:
            m = ans[j]
    ans.append(m+1)
if n:
    print(max(ans))
else:
    print(0)