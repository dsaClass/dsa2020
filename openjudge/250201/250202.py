n=int(input())
n=2*n-1
sq=[[0 for _ in range(n)] for _ in range(n)]
x=n//2
y=0
sq[y][x]=1
for i in range(2,n*n+1):
    x=x+1
    y=y-1
    if y<0:
        y+=n
    if x>=n:
        x-=n
    if sq[y][x]!=0:
        x=(x-1)%n
        y=(y+2)%n
    sq[y][x]=i
for row in sq:
    print(" ".join(map(str, row)))
