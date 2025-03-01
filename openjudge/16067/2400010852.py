def f(x,n):
    sum=1
    end=x[0][1]
    for i in range(1,n):
        if x[i][0]>=end:
            sum+=1
            end=x[i][1]
    return sum
while True:
    n=int(input())
    if n==0:
        break
    x=[]
    for i in range(n):
        x.append(list(map(int,input().split())))
    x.sort(key=lambda x:x[1])
    print(f(x,n))
