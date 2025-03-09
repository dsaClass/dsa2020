def convert2(n,memo):
    if n in memo:
        return memo[n]
    if n==0:
        return 0
    if n==1:
        return "2(0)"
    if n==2:
        return "2"
    if n==3:
        return "2+2(0)"
    alist=[]

    while n>0:
        alist.append(n%2)
        n=n//2
    astr=""
    blist=[]
    for i in range(len(alist)-1,-1,-1):
        if alist[i]!=0:
           if i>=2:
              blist.append(f"2({convert2(i,memo)})")
           elif i==1:
               blist.append("2")
           else:
               blist.append("2(0)")
    astr="+".join(map(str,blist))
    memo[n]=astr
    return memo[n]
memo={}
n=int(input())
print(convert2(n,memo))
