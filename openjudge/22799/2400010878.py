n=int(input())
def fun(n):
    if n==0 or n==1:
        return 1
    else:
        a,b=1,1
        for _ in range(2,n+1):
            a,b=b,a+b
        return b
print(fun(n))