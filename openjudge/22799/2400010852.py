def f(n):
    p,q,r=0,1,1
    for i in range(n-1):
        p,q,r=q,r,q+r
    return r
n=int(input())
print(f(n))
