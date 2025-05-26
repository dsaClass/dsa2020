while True :
    n=int(input())
    if n==0 :
        break

    INF=float('inf')
    dist=[[INF]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1) :
        dist[i][i]=0

    for u in range(1,n+1) :
        ipt=list(map(int,input().split()))
        num=ipt[0]

        for i in range(1,num+1) :
            v,w=ipt[2*i-1],ipt[2*i]
            dist[u][v]=w
    
    for k in range(1,n+1) :
        for i in range(1,n+1) :
            for j in range(1,n+1) :
                if dist[i][k]+dist[k][j]<dist[i][j] :
                    dist[i][j]=dist[i][k]+dist[k][j]

    min_time=INF
    person=0

    for i in range(1,n+1) :
        person_max_time=max(dist[i][1:])

        if person_max_time<min_time :
            min_time=person_max_time
            person=i

    if min_time==INF :
        print("disjoint")
    else :
        print(person,min_time) 