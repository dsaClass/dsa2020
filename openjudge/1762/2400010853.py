n=int(input())
mat=[]
result=[[0]*n for i in range(n)]
for i in range(n):
    row=list(map(int,input().split()))
    mat.append(row)
result[-1]=mat[-1]
for j in range(n-2,-1,-1):
    for l in range(j+1):
       result[j][l]=max(result[j+1][l],result[j+1][l+1])+mat[j][l]
print(result[0][0])