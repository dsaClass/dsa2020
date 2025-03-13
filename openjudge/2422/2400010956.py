s = input()
size = []
# 格式为[R, C]
num_of_blank = 0
while num_of_blank <2:
    for i in range(len(s)):
        if s[i] == ' ':
            size.append(int(s[:i]))
            num_of_blank += 1
            s = s[i + 1:]
            break
code = ''
for i in s:
    code += bin(ord(i) % 32)[2:].rjust(5, '0')
    # 获取对应五位二进制
code = code.ljust(size[0] * size[1], '0')
# 补全数位
matrix = [[-1 for i in range(size[1])] for j in range(size[0])]
# 初始化矩阵
x, y = 0, 0
# 初始化坐标
mode = 0
manner = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 移动方向，0~3代表右下左上
for i in code:
    matrix[x][y] = i
    x += manner[mode][0]
    y += manner[mode][1]
    try:
        if matrix[x][y] != -1:
            x -= manner[mode][0]
            y -= manner[mode][1]
            mode += 1
            mode %= 4
            x += manner[mode][0]
            y += manner[mode][1]
        else:
            continue
    except:
        x -= manner[mode][0]
        y -= manner[mode][1]
        mode += 1
        mode %= 4
        x += manner[mode][0]
        y += manner[mode][1]
for i in matrix:
    print(''.join(i), end='')
print()
            

