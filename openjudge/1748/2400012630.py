from functools import lru_cache
@lru_cache(maxsize=None)
def f(n,m) :
    if n==1 :
        return 1
    else :
        return (f(n-1,m)+m-1)%n+1

while True :
    n,m=map(int,input().split())
    if n==0 and m==0 :
        break
    print(f(n,m))