m,n=map(int,input().split())
def choice(m,n):
    if n==1 or m==0:
        return 1
    elif m<0:
        return 0
    else:
        return choice(m,n-1)+choice(m-n,n)
print(choice(m,n))