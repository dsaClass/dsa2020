result=[]
t=int(input())
for _ in range(t):
    n=int(input())
    stack=[]
    list1=[]
    for i in range(n):
        list1.append(list(map(int,input().split())))
    for i in list1:
        s1=i[0]
        s2=i[1]
        if s1==1:
            stack.insert(0,s2)
        else:
            if s2==stack[0]:
                if len(stack) !=1:
                    result.append('Stack')
                    break
                else:
                    stack.pop(0)
            elif  s2==stack[-1]:
                if len(stack)!=1:
                    result.append('Queue')
                    break
                else:
                    stack.pop()
for i in result:
    print(i)