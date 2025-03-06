char=list(input())
n=len(char)
used=[0]*n
ans=[0]*n

def put(i) :
    if i==n :
        for chr in ans :
            print(chr,end='')
        print('')
        return 
    else :
        for k in range(n) :
            if not used[k] :
                ans[i]=char[k]
                used[k]=1

                put(i+1)
                used[k]=0

put(0)