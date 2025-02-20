n=int(input())
a,b,c=1,1,1
for i in range(n):
    a,b,c=a+b+c,a+b,a+c
print(a)