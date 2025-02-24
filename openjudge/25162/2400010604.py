l_min=[0]*50

f0,f1=0,1
for i in range(50):
    l_min[i]=f1
    f0,f1=f1,f0+f1+1

n=int(input())
for j in range(50):
    if n<l_min[j]:
        print(j)
        break