n=int(input())
def stj(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return stj(n-1)+stj(n-2)
print(stj(n))
