while True:
    m,n=map(int,input().split())
    if m==0 and n==0:
        break
    else:
        s,i=0,0
        while 2*m<=n:
            s+=2**i
            i+=1
            m=2*m
        if m+2**i-1<=n:
            s+=2**i
        else:
            s+=n-m+1
        print(s)