n = int(input())
arr = list(map(int, input().split()))
k = int(input())

# 排序数组
arr.sort(reverse=True)

# 输出前k大的数
for num in arr[:k]:
    print(num)