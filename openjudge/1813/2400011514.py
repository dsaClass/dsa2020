# 读取输入
original_grid = []
for _ in range(5):
    row = list(map(int, input().split()))
    original_grid.append(row)

# 枚举第一行的所有可能按法
for k in range(64):
    # 初始化press矩阵
    press = [[0] * 6 for _ in range(5)]
    # 设置第一行的按法
    for j in range(6):
        press[0][j] = (k >> (5 - j)) & 1  # 修正列的顺序对应二进制的高位到低位
    
    # 复制初始灯的状态
    temp_grid = [row.copy() for row in original_grid]
    
    # 处理第一行的按钮影响
    for j in range(6):
        if press[0][j]:
            i = 0
            temp_grid[i][j] ^= 1
            # 处理上方
            if i > 0:
                temp_grid[i-1][j] ^= 1
            # 处理下方
            if i < 4:
                temp_grid[i+1][j] ^= 1
            # 处理左方
            if j > 0:
                temp_grid[i][j-1] ^= 1
            # 处理右方
            if j < 5:
                temp_grid[i][j+1] ^= 1
    
    # 处理第2到第5行的按钮按法
    for i in range(1, 5):
        # 确定当前行的按法
        for j in range(6):
            if temp_grid[i-1][j] == 1:
                press[i][j] = 1
            else:
                press[i][j] = 0
        
        # 应用当前行的按钮影响
        for j in range(6):
            if press[i][j]:
                temp_grid[i][j] ^= 1
                # 处理上方
                if i > 0:
                    temp_grid[i-1][j] ^= 1
                # 处理下方
                if i < 4:
                    temp_grid[i+1][j] ^= 1
                # 处理左方
                if j > 0:
                    temp_grid[i][j-1] ^= 1
                # 处理右方
                if j < 5:
                    temp_grid[i][j+1] ^= 1
    
    # 检查第五行是否全灭
    if all(x == 0 for x in temp_grid[4]):
        # 输出结果
        for row in press:
            print(' '.join(map(str, row)))
        exit()