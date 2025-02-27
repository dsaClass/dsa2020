def cut(x,y):
    if x==y:
        return -1
    if x>y:
        return x-y,y
    if x<y:
        return x,y-x

n,m=map(int,input().split())
time=0
while True:
    if cut(n,m)==-1:
        break
    else:
        n,m=cut(n,m)
        time+=1
print(time+1)