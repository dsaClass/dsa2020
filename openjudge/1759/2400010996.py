#bisect函数的巧妙用法
#这题往后结合迪尔沃斯定理可以进一步增加难度
from bisect import bisect_left
N = int(input())
nums = list(map(int,input().split()))
lis = []
for i in nums:
    idx = bisect_left(lis,i)
    if idx == len(lis):
        lis.append(i)
    else:
        lis[idx] = i
print(len(lis))
