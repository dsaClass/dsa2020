n=int(input())
lst=[0,1,1]
for i in range(3,31):
    a=lst[i-1]+lst[i-2]+lst[i-3]
    lst.append(a)
print(lst[n])