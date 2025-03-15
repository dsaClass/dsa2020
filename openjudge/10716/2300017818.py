n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

if n==1:
    result=a[0]
elif n==2:
   result=max(a[0]+b[1],b[0]+a[1])
else:
 leftmax=[[0,0] for i in range(n-1)]
 for i in range(n-1):
    if i==0:
        leftmax[i][1]=b[0] #leftmax[i][1]保存当坐入第i个位置时若右侧已被占，前面所有座位最大能力值总和
        leftmax[i][0]=a[0] #反之，右侧未被占
    else:
        leftmax[i][1]=max(leftmax[i-1][1]+b[i],leftmax[i-1][0]+c[i])
        leftmax[i][0]=max(leftmax[i-1][1]+a[i],leftmax[i-1][0]+b[i])

 result=max(leftmax[n-2][0]+b[n-1],leftmax[n-2][1]+a[n-1])
print(result)
        
