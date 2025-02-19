def main():
    l0=input().strip().split()
    n,w=int(l0[0]),int(l0[1])
    tmp=[]
    for i in range(n):
        row=input().strip().split()
        int_row=[int(x) for x in row]
        tmp.append(int_row)
    tmp.sort(key=lambda x:-x[0]/x[1])
    ans=0
    l=0
    while w and l<n:
        weight=min(w,tmp[l][1])
        w-=weight
        ans+=weight*(tmp[l][0]/tmp[l][1])
        l+=1
    print(round(ans,1))
if __name__=="__main__":
    main()