t=0
while True:
    t+=1
    lis=input()
    if lis == '#':
        break
    else:
        g=-1
        a=[0]*(len(lis)//2)
        u=0
        s=0
        r=0
        r1=0
        for i in range(len(lis)):
            if lis[i]=='d':
                g+=1
                a[g]+=1
                s+=1
                r=max(s,r)
                r1=max(r1,g)
            else:
                g-=1
                if i<len(lis)-1 and lis[i+1]=='u':
                    s-=a[g+1]
                    a[g+1]=0

        print('Tree ',t,': ',r1+1,' => ',r,sep='')