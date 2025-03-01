def f(s):
    stack=[]
    left='[{('
    right=']})'
    for i in s:
        if i in left:
            stack.append(i)
        elif i in right:
            if  not stack:   
                return 'NO'
            elif left.index(stack[-1])==right.index(i):    #括号配对
                stack.pop()
            else:     
                return 'NO'
    if stack:   #如果栈非空，则此时也为NO
        return "NO"
    return 'YES'
n=int(input())
for i in range(n):
    s=input()
    print(f(s))
