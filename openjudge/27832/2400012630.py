import sys

def main() :
    #读入
    input=sys.stdin.read().split()
    ptr=0
    N=int(input[ptr])
    ptr+=1
    M=int(input[ptr])
    ptr+=1
    nums=list(map(int,input[ptr:ptr+N]))
    ptr+=N

    mod_values=[1<<(i+1) for i in range(16)]
    
    # 每个i的余数计数
    cnt=[]
    for i in range(16) :
        cnt.append([0]*mod_values[i])
    
    for x in nums :
        for i in range(16) :
            r=x%mod_values[i]
            cnt[i][r]+=1
    
    # 前缀和数组
    pre_sum=[]
    for i in range(16) :
        m=mod_values[i]
        ps=[0]*m
        current_sum=0
        for r in range(m) :
            current_sum+=cnt[i][r]
            ps[r]=current_sum
        pre_sum.append(ps)
    
    add=0  # 全局累加
    for _ in range(M) :
        op=input[ptr]
        ptr+=1
        if op=='C' :
            d=int(input[ptr])
            ptr+=1
            add=(add+d)%65536
        elif op=='Q' :
            i=int(input[ptr])
            ptr+=1
            m=mod_values[i]
            s=1<<i
            add_mod=add%m
            t=(s-add_mod)%m
            e=((m-1)-add_mod)%m
            
            if t<=e :
                if t==0 :
                    ans=pre_sum[i][e]
                else :
                    ans=pre_sum[i][e]-pre_sum[i][t-1]
            else :
                p1=pre_sum[i][m-1]-pre_sum[i][t-1]
                p2=pre_sum[i][e] 
                ans=p1+p2
            print(ans)
            
if __name__ == '__main__':
    main()