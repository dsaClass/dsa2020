def fib(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n>=3:
        return fib(n-1)+fib(n-2)
    
n=int(input())
print(fib(n))