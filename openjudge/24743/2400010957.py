n=int(input())
alist=[int(x) for x in input().split()]
blist=[int(x) for x in input().split()]
Max=max(alist[n-1],blist[n-1])
i,j,k=0,0,0
clist=[]
while i<=Max:
    if j<n:
        while alist[j]==i:
            clist.append(i)
            j+=1
            if j==n:
                break
    if k<n:
        while blist[k]==i:
            clist.append(i)
            k+=1
            if k==n:
                break
    i+=1
for s in clist:
    print(s,end=" ")
