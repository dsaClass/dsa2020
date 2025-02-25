dp=[3]
def run():
    num=len(dp)
    ans=2
    for i in range(num):
        if i==0:
            ans+=dp[-1-i]
        ans+=dp[-1-i]*2
    dp.append(ans)
while True:
    n=int(input())
    if n==-1:
        break
    elif n==0:
        print(1)
        continue
    elif n%2!=0:
        print(0)
        continue
    else:
        n=n//2
    while len(dp)<n:
        run()
    print(dp[n-1])
