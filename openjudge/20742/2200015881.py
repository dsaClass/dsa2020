n = int(input())
lis = [0,1,1]
while len(lis)<=31:
    lis.append(lis[-1]+lis[-2]+lis[-3])
print(lis[n])
