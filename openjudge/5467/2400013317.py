n=int(input())
for _ in range(n):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    dic={}
    lst=[]
    for i in range(len(a)//2-1):
        dic[a[2*i+1]]=dic.get(a[2*i+1],0)+a[2*i]
        lst.append(a[2*i+1])
    for i in range(len(b)//2-1):
        dic[b[2*i+1]]=dic.get(b[2*i+1],0)+b[2*i]
        lst.append(b[2*i+1])
    lst=sorted(set(lst),reverse=True)
    output=[]
    for j in lst:
        if dic[j]!= 0:
            output.append(f'[ {dic[j]} {j} ]')
    print(' '.join(output))
