n=int(input())
input1=[]
result=[]
for i in range(n):
    s1,s2=map(str,input().split())
    current=[]
    if len(s1)>=len(s2):
        j=0
        while j in range(len(s1)-len(s2)+1):
            if s2==s1[j:j+len(s2)]:
                current.append(j)
                j+=len(s2)
            else:
                j+=1
        if current!=[]:
            result.append(current)
        else:
            result.append(['no'])
    else:
        result.append(['no'])
for i in result:
    for j in range(len(i)):
        print(i[j],end=" "if j<len(i)-1 else "\n")