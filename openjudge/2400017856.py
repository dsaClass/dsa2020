from collections import deque

t=int(input())
for i in range(t):
    n=int(input())
    s=input().split()
    q=deque()
    flag=1
    for j in range(len(s)):
        if s[j][0]=='+':
            q.append(s[j][1])
        else:
            if q:
                k=q.popleft()
            else:
                flag=-1
                break
            if k==s[j][1]:
                continue
            else:
                flag=-1
                break
    if flag==1:
        print (f'Case {i+1}: yes')
    else:
        print (f'Case {i+1}: no')