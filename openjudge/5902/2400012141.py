t=int(input())
result=[]
for i in range(t):
    n=int(input())
    current=[]
    for j in range(n):
        list1=list(map(int,input().split()))
        if list1[0]==1:
            current.insert(0,list1[1])
        else:
            if list1[1]==0:
                current.pop()
            else:
                current.pop(0)
    if len(current)==0:
        result.append('NULL')
    else:
        result.append(reversed(current))
for i in result:
    if i == 'NULL':
        print('NULL')
    else:
        print(' '.join(map(str,i)))