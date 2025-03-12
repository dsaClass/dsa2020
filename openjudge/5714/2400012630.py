t=int(input())
for _ in range(t) :
    sign='s'
    n=int(input())
    stack=[]
    for _ in range(n) :
        ty,val=map(int,input().split())
        if ty==1 :
            stack.append(val)
        else :
            if stack.pop() != val :
                sign='q'
    if sign=='s' :
        print("Stack")
    else :
        print("Queue")