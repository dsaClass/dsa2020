n,w=input().split()
n=int(n)
w=int(w)
zl=[]
for i in range(n):
    a=list(map(int,input().split()))
    a[0]=a[0]/a[1]
    if len(zl)==0:
        zl.append(a)
    else:
        for j in range(len(zl)):
            if a[0]<zl[j][0]:
                zl.insert(j,a)
                break
            if j==len(zl)-1:
                zl.append(a)

n-=1
su=0
while w!=0 and n!=-1:
    if w>zl[n][1]:
        w-=zl[n][1]
        su+=zl[n][0]*zl[n][1]
        n-=1
    else:
        su+=w*zl[n][0]
        break
print(round(su,1))