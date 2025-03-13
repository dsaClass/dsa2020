n,m=input().split()
n=int(n)
m=int(m)
li=list(map(int,input().split()))
lj=0
li2=[]
for j in range(16):
    li2.append([0]*2**(j+1))
for i in range(n):
    for j in range(16):
        li2[j][li[i]%2**(j+1)]+=1
for j in range(16):
    for k in range(1,2**(j+1)):
        li2[j][k]+=li2[j][k-1]
        
for i in range(m):
    cz=input()
    if cz[0]=='C':
        lj=(int(cz[2:])+lj)%65536
    else:
        j=int(cz[2:])
        k=lj%2**(j+1)
        if k<2**j:
            print(li2[j][2**(j+1)-1-k]-li2[j][2**j-k-1])
        else:
            print(li2[j][2**(j+1)-1-k]+li2[j][2**(j+1)-1]-li2[j][2**(j+1)+2**j-k-1])
        

        
    
