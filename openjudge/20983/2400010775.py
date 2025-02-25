n=int(input())

def pmt(n,s):
    if n==1 or n==0:
        return 1
    elif n<=s:
        sum=0
        for i in range(1,n+1):
            sum+=pmt(n-i,i)
        return sum 
    else:
        sum=0
        for i in range(1,s+1):
            sum+=pmt(n-i,i)
        return sum 

print(pmt(n,n))
