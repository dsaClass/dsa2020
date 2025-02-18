while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    lst=[i for i in range(1,n+1)]
    while len(lst)>1:
        if len(lst)>=m:
            lst=lst[m:]+lst[:m-1]
        elif len(lst)<m:
            r=m%len(lst)
            if r!=0:
                lst=lst[r:]+lst[:r-1]
            else:
                lst=lst[:-1]
    print(lst[0])