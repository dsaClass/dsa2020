def isvalid(num): # 检查是否是可能的距离值
    global barn
    cnt = 1
    prev = barn[0] # 在x1处放一只牛
    for i in range(len(barn)):
        if barn[i] - prev >= num:
            cnt += 1
            prev = barn[i] # 在放了一只牛之后的第一个距离大于num的stall放另一只牛
        else:
            pass
    if cnt >= c: # 如果放的牛数量超过c，说明是可能的距离值。
        return True
    else:
        return False


n, c = map(int, input().split())
barn = []
for i in range(n):
    barn.append(int(input()))
barn.sort() # 对stall的坐标由小到大排序。
left = 1 # 二分查找，确定牛的间隔的最小值的最大值。
right = barn[-1] // c + 1
while left <= right:
    mid = (left + right) // 2
    if isvalid(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right)
