n=int(input())

f0,f1=0,1
for _ in range(n-1):
    f0,f1=f1,f0+f1+1

print(f1)