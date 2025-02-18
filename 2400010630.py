n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
i=0
j=0
while i<n and j<n:
    if a[i]>b[j]:
        c.append(b[j])
        j+=1
    else:
        c.append(a[i])
        i+=1
while i<n:
    c.append(a[i])
    i+=1
while j<n:
    c.append(b[j])
    j+=1
for d in c:
    print(d,end=' ')
    
