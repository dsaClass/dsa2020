def calculate(n):
    data=[]
    for i in range(0,n+1):
            data.append([i,n-i])
    return data
def nums(i):
    a=str(i)
    sum=0
    for j in a:
        sum+=cal[int(j)]
    return sum
s=0
n=int(input())
cal=[6,2,5,5,4,5,6,3,7,6]
if n < 13 :
    print(0)
else:
    n-=4
    for i in range(1000):
        a=calculate(i)
        for da in a:
            if (n-(nums(da[0])+nums(da[1]))) == nums(i) and da[0] + da[1] == i :
                s+=1
    print(s)
