ans_=[]
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    mmap = []
    k = True
    # k记录了是否仍未找到起始点
    # 记录地图
    for i in range(h):
        row = list(input())
        if k and '@' in row:
            x = row.index('@')
            y = i
            k = False
        mmap.append(row)
    ans = 1


    def tanlu(x:int,y:int):
        '''深搜函数，不走回头路，因为回头路总可以被另外的方式抵达，将走过的地方标记为‘@’避免重复检索，走路时不检查起点即可避免问题'''
        # 修改地图
        global mmap,ans
        if x != 0:
            #可以向左走
            if mmap[y][x-1] == '.':
                #只有黑色瓷砖可走
                mmap[y][x-1] = '@'
                #标记为已经走过的黑色瓷砖
                ans += 1
                tanlu(x-1, y)
        if x != w-1:
            # 可以向右走
            if mmap[y][x+1] == '.':
                mmap[y][x+1] = '@'
                ans += 1
                tanlu(x+1,y)
        if y != 0:
            # 可以向上走
            if mmap[y-1][x] == '.':
                mmap[y-1][x] = '@'
                ans += 1
                tanlu(x,y-1)
        if y != h-1:
            # 可以向下走
            if mmap[y+1][x] == '.':
                mmap[y+1][x] = '@'
                ans += 1
                tanlu(x,y+1)
        return None
    tanlu(x,y)
    ans_.append(ans)


for i in ans_:
    print(i)
    '''for i in mmap:
        print(''.join(i)) 测试用'''
    