p,e,i,d=map(int,input().split())
sum=0
while True:
    if (sum-p)%23==0 and (sum-e)%28==0 and (sum-i)%33==0:
        print(sum-d if sum>d else sum+21252-d)
        break
    sum+=1
