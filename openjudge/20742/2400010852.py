def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    a,b,c=0,1,1
    for i in range(n-2):
        a,b,c=b,c,a+b+c
    return c
n=int(input())
print(f(n))
