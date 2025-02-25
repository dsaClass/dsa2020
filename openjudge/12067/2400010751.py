def check(v, a, b, n, k):
    temp = []
    for i in range(n):
        temp.append(a[i] - v * b[i])
    temp.sort()
    sum_val = sum(temp[k:])
    return sum_val >= 0


def solve():
    while True:
        n,k=map(int,input().split())
        if n==0 and k==0:
            break
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))

        L,R = 0.0, 1.0
        while R-L>1e-5:
            mid=(L+R)/2.0
            if check(mid,a,b,n,k):
                L=mid
            else:
                R=mid
        print(round(100*L))
solve()
