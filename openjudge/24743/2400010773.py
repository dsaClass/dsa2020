n=int(input())
num1=list(map(int,input().split()))
num2=list(map(int,input().split()))
i=0
j=0
ans=[]
while i<n and j<n :
    if num1[i]<num2[j]:
        ans.append(num1[i])
        i+=1
    else:
        ans.append(num2[j])
        j+=1
if i==n:
    for k in range(j,n):
        ans.append(num2[k])
else:
    for k in range(i,n):
        ans.append(num1[k])
for i in range(2*n-1):
    print(ans[i],end=' ')
print(ans[2*n-1])