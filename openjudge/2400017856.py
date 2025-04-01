n=int(input())
a=list(map(int,input().split()))
m=int(input())
a.sort()
i=0
j=n-1
flag=0
while(i<j):
    if a[i]+a[j]==m:
        flag=1
        print (a[i], a[j])
        break
    elif a[i]+a[j]<m:
        i+=1
    else:
        j-=1
if flag==0:
    print ("No")