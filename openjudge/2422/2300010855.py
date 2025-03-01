#获得未加密字符串
a, b, message = input().split(maxsplit=2) #输入数据
a=int(a)
b=int(b)
shuchu = ""
chang = len(message)
#转换成二进制
for char in message:
    if char == " ":
        shuchu += "00000"
    else: 
        i = ord(char)-64
        i= format(i, '05b')
        shuchu += i

#补全长度
k = a*b-chang*5
for i in range(k):
    shuchu+='0'


# 创建一个 4x4 的二维空列表，初始化为 None
matrix = [[None for _ in range(b)] for _ in range(a)]

# 保存原始行和列数，用于打印
aa, bb = a, b
h = 0  # 行索引
l = 0  # 列索引
weizhi = 0  # 字符串 shuchu 的位置索引

# 方向控制：0=右，1=下，2=左，3=上
direction = 0
steps = b  # 每种方向的步数
step_count = 0  # 当前方向的步数计数
steps_taken = 0  # 总步数


while weizhi < len(shuchu):
    matrix[h][l] = shuchu[weizhi]
    weizhi += 1
    step_count += 1
    steps_taken += 1

    

    # 检查是否需要改变方向
    if step_count == steps:
        if steps==b:
            steps=a
        else:
            steps=b

        if direction % 2 == 0:  # 每改变一次水平方向，步数减少
            a -= 1
            b -= 1
            steps-=1
        step_count = 0

       
        
        direction = (direction + 1) % 4
    
    # 根据方向移动
    if direction == 0:  # 向右
        l += 1
    elif direction == 1:  # 向下
        h += 1
    elif direction == 2:  # 向左
        l -= 1
    elif direction == 3:  # 向上
        h -= 1

   

# 打印矩阵
for i in range(aa):
    for j in range(bb):
        print(matrix[i][j], end="")
