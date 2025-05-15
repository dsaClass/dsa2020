n = int(input())
nums = list(map(int, input().split()))
tails = []
for num in nums:
    # 二分查找插入位置
    left, right = 0, len(tails)
    while left < right:
        mid = (left + right) // 2
        if tails[mid] < num:
            left = mid + 1
        else:
            right = mid
    if left == len(tails):
        tails.append(num)
    else:
        tails[left] = num  # 替换更小的末尾元素
print(len(tails))