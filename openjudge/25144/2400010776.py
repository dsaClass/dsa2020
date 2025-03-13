n=int(input())
g=[]
for i in range(n):
    a,b=map(int,input().split())
    g.append([a,b,i])
c=[0]*n
c[0]=n
while list(g):
    for x in g:
        if x[0]==-1 and x[1]==-1:
            g.remove(x)

        elif x[0]==-1:
            if c[x[1]]!=0:
                c[x[2]]=c[x[1]]-1
                g.remove(x)

            elif c[x[2]]!=0:
                c[x[1]]=c[x[2]]+1
                g.remove(x)

        elif x[1]==-1:
            if c[x[0]]!=0:
                c[x[2]]=c[x[0]]-1
                g.remove(x)

            elif c[x[2]] != 0:
                c[x[0]] = c[x[2]] + 1
                g.remove(x)

        elif c[x[2]] != 0:
            c[x[1]] = c[x[2]] + 1
            c[x[0]] = c[x[2]] + 1
            g.remove(x)

        elif c[x[0]]!=0:
            c[x[2]] = c[x[0]] - 1
            c[x[1]] = c[x[0]]
            g.remove(x)

        elif c[x[1]]!=0:
            c[x[2]] = c[x[1]] - 1
            c[x[0]] = c[x[1]]
            g.remove(x)
s=0
for y in c:
    s=max(s,c.count(y))
print(s)