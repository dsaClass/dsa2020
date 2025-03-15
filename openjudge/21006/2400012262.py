m,n=map(int,input().split())
sum=0
memo={}
def find(a,b,m):
    if (a,b) in m:
        return m[(a,b)]
    if b==1 or a == 0:
        return 1
    if b > a:
        return find(a,a,m)
    return find(a,b-1,m) + find(a-b,b,m)
sum=find(m,n,memo)
print(sum)
