a=list(map(int,input().split()))
n,m=a[0],a[1]

def sum(n):
    ans=0
    while n>0:
        ans+=n%2 
        n=n//2 
    return ans

if n>m:
    print(n-m)


else:
    k=0
    p=1
    while p*n<=m:
        k+=1
        p*=2              
        
    d1=m-(p//2)*n
    nm1=d1//(p//2)+sum(d1%(p//2))+k-1
            
    d2=p*n-m   
    nm2=d2//(p)+sum(d2%(p))+k
    
    print(min(nm1,nm2))