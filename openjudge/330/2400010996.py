#转化到x轴上，从而变为区间包含问题
from math import sqrt
answer=[]
while True:
    n,d=map(int,input().split())
    if n==0 and d==0:
        break
    else:
        locations=[]
        for i in range(n):
            x,y=map(int,input().split())
            if abs(y)>d:
                locations.append([-10**30,10**30])
            else:
                delta=sqrt(d**2-y**2)
                locations.append([x-delta,x+delta])
        locations.sort(key=lambda x:x[1],reverse=False)
        sum=0
        if [-10**30,10**30]  in locations:
            sum=-1
        elif len(locations)==1:
            sum=1
        else:
            right=locations[0][1]
            sum+=1
            for i in range(1,len(locations)):
                if locations[i][0]>right:
                    sum+=1
                    right=locations[i][1]
        answer.append(sum)
    input()
for i in range(len(answer)):
    print(f'Case {i+1}: {answer[i]}')
