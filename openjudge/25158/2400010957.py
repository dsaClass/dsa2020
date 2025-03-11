n,m=[int(x) for x in input().split()]
alist=[]
for i in range(n):
    blist=[]
    str1=input()
    for i in range(len(str1)):
        blist.append(str1[i])
    alist.append(blist)
clist=[]
dlist=[]
for i in range(m+2):
    clist.append(-1)
for i in range(n+2):
    dlist.append(clist[:])
def  f(i,j):
    if dlist[i][j]!=(-1 or 1):
        return dlist[i][j]
    else:
        dlist[i][j]=1
        if i<=0 or j<=0 or i>=n+1 or j>=m+1:
            dlist[i][j]=False
            return False
        elif i==1 and j==1:
            return True
        else:
            if alist[i-1][j-1]=="." and ((dlist[i][j-1]!=1 and f(i,j-1)) or(dlist[i][j+1]!=1 and f(i,j+1))or (dlist[i-1][j]!=1 and f(i-1,j))or (dlist[i+1][j]!=1 and f(i+1,j))):
                dlist[i][j]==True
                return True
            else:
                dlist[i][j]==False
                return False
if f(n,m)==True:
    print("1")
else:
    print("0")
