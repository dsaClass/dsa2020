n = int(input().strip())
l1 = list(map(int, input().strip().split()))
l2 = list(map(int, input().strip().split()))
i, j = 0, 0
ans = []
while i < n and j < n:
    if l1[i] <= l2[j]:
        ans.append(l1[i])
        i += 1
    else:
        ans.append(l2[j])
        j += 1
while i < n:
    ans.append(l1[i])
    i += 1
while j < n:
    ans.append(l2[j])
    j += 1
for i in ans:
    print(i, end=' ')