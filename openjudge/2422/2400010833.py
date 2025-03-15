r, c, s = map(str, input().split(maxsplit=2))
r = int(r)
c = int(c)


# 将字符转换为二进制编码
code = ''
for char in s:
    if char == ' ':
        a = 0
    else:
        a = ord(char) - ord('A') + 1
    code += f'{a:05b}'
for i in range(len(s)+1,5*r*c+3):
    code+='00000'

p = [[5]*(c+2)]  
mx = p + [[5] + [-1]*c + [5] for _ in range(r)] + p

# 右、下、左、上
dirL = [[0, 1], [1, 0], [0, -1], [-1, 0]]
row, col = 1, 1  # 从(1, 1)开始填充
N = 0  
drow, dcol = dirL[0]  # 初始方向为右

# 螺旋填充矩阵
for j in range(r*c):
    mx[row][col] = code[j] 
    if mx[row + drow][col + dcol] != -1:  # 如果下一个位置已经填充过，则改变方向
        N += 1
        drow, dcol = dirL[N % 4]  # 改变方向
    # 移动到下一个位置
    row += drow
    col += dcol

# 输出结果
print(*[(''.join(map(str, mx[i][1:-1]))) for i in range(1,r+1)],sep='')