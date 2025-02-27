dic={" ":0}
keys = ""
for _ in range(ord('A'), ord('Z') + 1):
    keys += chr(_)
for i in range(26):
    dic[keys[i]]=i
input_list = input().split(" ",2)
R,C,info = int(input_list[0]),int(input_list[1]),input_list[2]

def erjinzhi(zimu):
    output = []
    shuzi=dic[zimu]
    while shuzi >= 2:
       output.append(shuzi % 2)
       shuzi = shuzi // 2
    output.append(shuzi)
    while len(output) < 5:
        output.append(0)
    output.reverse()
    return output

sequential = []
for _ in info:
    for n in erjinzhi(_):
        sequential.append(n)
# print(sequential)

def generateMatrix(R,C):
    # 构造R行C列的矩阵
    matrix = [[0] * C for _ in range(R)]
    directions = [(0,1),(1,0),(0,-1),(-1,0)] #向右，向下，向左，向上
    row,col,di = 0,0,0
    visited = [[False] * C for _ in range(R)]
    for i in sequential:
        matrix[row][col] = i
        visited[row][col] = True  # 标记当前位置已访问
        dr,dc = directions[di]
        if not (0<= row+dr < R and 0<= col+dc < C and not visited[row+dr][col+dc]):
            di = (di+1) % 4 #变方向
            dr, dc = directions[di]
        row,col = row+dr, col+dc

    #将二维矩阵输出
    encryption = ""
    for row in matrix:
        for num in row:
            encryption += str(num)

    return encryption

print(generateMatrix(R,C))


