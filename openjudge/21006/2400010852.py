m,n=map(int,input().split())
def f(m,n):
    if n==1 and m>=0:
        return 1
    elif m<0:
        return 0
    else:
        return f(m-n,n)+f(m,n-1)
print(f(m,n))
