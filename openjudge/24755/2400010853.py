n=int(input())
lst=[1]*(2*n+1)
for i in range(1,2*n+1):
    lst[i]=lst[i-1]*i
k=(lst[2*n])/(lst[n]*lst[n+1])
print(int(k))