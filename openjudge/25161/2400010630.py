n=int(input())
if n==1:
    print(1)
elif n==2:
    print(2)
else:
    a=2
    b=3
    for i in range(n-2):
        c=a+b
        a=b
        b=c
    print(b-1)