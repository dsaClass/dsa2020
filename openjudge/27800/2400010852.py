l=list(map(str,input().split()))
dic={'+','-','*','/'}
q=[]
for i in l:
    if i in dic:
        q.append(i)
    else:
        q.append(float(i))
    while len(q) >= 2 and q[-1] not in dic and q[-2] not in dic:
        b= q.pop()
        a= q.pop()
        r = q.pop()
        if r == '+':
            q.append(a + b)
        elif r == '-':
            q.append(a - b)
        elif r == '*':
            q.append(a * b)
        else:
            q.append(a / b)
print(f"{q[0]:.1f}")
