n=int(input())
def jump(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n==3:
        return 2
    elif n==4:
        return 3
    elif n==5:
        return 5
    else:
        return jump(n-1)+jump(n-3)+jump(n-5)
print(jump(n))
