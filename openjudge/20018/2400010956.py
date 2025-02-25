n = int(input())
num = [1]
kind = [int(input())]
# 从大到小排列
# 首次输入特殊处理
ans = 0


def search_place(x:int,start:int,end:int):
    '''二分查找'''
    global kind,num,ans
    if x == kind[start]:
        num[start] += 1
        ans += sum(num[start+1:])
        return None
    if x == kind[end]:
        num[end] += 1
        ans += sum(num[end+1:])
        return None
    if end - start == 1:
        ans += sum(num[end:])
        kind = kind[:end] + [x] + kind[end:]
        num = num[:end] + [1] + num[end:]
        return None
    mid = int((start + end)/2)
    if x == kind[mid]:
        num[mid] += 1
        ans += sum(num[mid+1:])
        return None
    if x < kind[mid]:
        search_place(x,mid,end)
        # 不+1和-1避免bug出现
        return None
    search_place(x,start,mid)
    # 不+1和-1避免bug出现
    return None


for i in range(1,n):
    x = int(input())
    if x > kind[0]:
        kind = [x] + kind
        num = [1] + num
        ans += i
        continue
    if x < kind[-1]:
        kind.append(x)
        num.append(1)
        continue
    # 保证进入二分的数据在两端点之间
    search_place(x,0,len(kind)-1)
print(ans)
