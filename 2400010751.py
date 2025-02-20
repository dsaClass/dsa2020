s,s1,s2 = map(str, input().split(','))
if s1 in s and s2 in s:
    tail=0
    head=len(s)
    while s1 not in s[:tail]:
        tail+=1
    while s2 not in s[head-1:]:
        head-=1
    if tail<=head:
        print(head-tail-1)
    else:
        print(-1)
else:
    print(-1)
    
