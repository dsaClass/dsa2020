import sys

def integer_partition() :
    max_n=50

    dp_k=[[0]*(max_n+1) for _ in range(max_n+1)]
    dp_k[0][0]=1
    for i in range(1,max_n+1) :
        for j in range(1,i+1) :
            dp_k[i][j]=dp_k[i-1][j-1]+dp_k[i-j][j]

    dp_diff=[0]*(max_n+1)
    dp_diff[0]=1
    for i in range(1,max_n+1) :
        for j in range(max_n,i-1,-1) :
            dp_diff[j]+=dp_diff[j-i]

    dp_odd=[0]*(max_n+1)
    dp_odd[0]=1
    for i in range(1,max_n+1,2) :
        for j in range(i,max_n+1) :
            dp_odd[j]+=dp_odd[j-i]

    for line in sys.stdin :
        line=line.strip()
        if not line :
            continue
        N,K=map(int,line.split())
        print(dp_k[N][K])
        print(dp_diff[N])
        print(dp_odd[N])

integer_partition()