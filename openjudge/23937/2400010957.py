n=int(input())
alist=[]
for i in range(n):
    blist=[int(x) for x in input().split()]
    alist.append(blist)
clist=[]
dlist=[]
for i in range(n):
    clist.append(-1)
for i in range(n):
    dlist.append(clist[:])
def  f(i,j):
    if dlist[i][j]!=-1:
        return dlist[i][j]
    else:
        if i==0 and j==0:
            return True
        elif i==0:
            dlist[i][j]=alist[i][j]==0 and f(i,j-1)
            return alist[i][j]==0 and f(i,j-1)
        elif j==0:
            dlist[i][j]=alist[i][j]==0 and f(i-1,j)
            return alist[i][j]==0 and f(i-1,j)
        else:
            dlist[i][j]=alist[i][j]==0 and (f(i-1,j) or f(i,j-1))
            return alist[i][j]==0 and (f(i-1,j) or f(i,j-1))
if f(n-1,n-1)==True:
    print("Yes")
else:
    print("No")
