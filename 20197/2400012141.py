n,m=map(int,input().split())
count_square=0
while m>0 and n>0:
    m,n=max(m,n)-min(m,n),min(m,n)
    count_square+=1
print(count_square)