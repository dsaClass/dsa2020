n, c=map(int, input().split())
stall = []
for i in range(n):
    stall.append(int(input()))
stall.sort()
mmax = (stall[-1] - stall[1]) // (c - 1)
# 不论如何划分，总会有至少一个间距小于等于mmax
# 下面利用二分法查找ans
mmin = 1
while mmin < mmax - 1:
    # 注意到不论何时，mmin作为间距总是可以的
    # 最后一次循环，mmax - mmin = 2
    dis = (mmax + mmin) // 2
    now = stall[0]
    # 首栏放置一头牛
    remain = c - 1
    # 记录剩余牛数
    for i in stall:
        if i - now >= dis:
            now = i
            remain -= 1
            if remain == 0:
                # 分散成功，尝试扩大dis
                mmin = dis
                break
    else:
        # 没有成功，缩小dis再试
        mmax = dis
# 循环结束，此时mmax - mmin = 1，试试mmax是否可行
now = stall[0]
# 首栏放置一头牛
remain = c - 1
# 记录剩余牛数
for i in stall:
    if i - now >= mmax:
        now = i
        remain -= 1
        if remain == 0:
            # 分散成功
            print(mmax)
            break
else:
    # 没有成功
    print(mmin)
