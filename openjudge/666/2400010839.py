def f(n,m):
    if n==0:
        return 1
    if n<0 or m<=0:
        return 0
    return f(n-m,m)+f(n,m-1)
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    print(f(n,m))
