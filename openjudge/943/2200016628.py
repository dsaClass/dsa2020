def draw_triangle(canvas, x, y, size): #从 (x,y) 位置开始，画一个高度为 size 的谢尔宾斯基三角形。
    if size == 2:
        canvas[x][y] = '/' 
        canvas[x][y + 1] = '\\'
        canvas[x + 1][y - 1] = '/'
        canvas[x + 1][y] = '_'
        canvas[x + 1][y + 1] = '_'
        canvas[x + 1][y + 2] = '\\'
    else:
        half = size // 2 #把当前大三角形拆成三个小三角形，每个小三角形的高度是 half
        # 画上面的三角
        draw_triangle(canvas, x, y, half)
        # 画左下角三角
        draw_triangle(canvas, x + half, y - half, half)
        # 画右下角三角
        draw_triangle(canvas, x + half, y + half, half)

while True:
    n = int(input())
    if n == 0:
        break
    height = 2 ** n
    width = 2 * height
    # 建立空白画布
    canvas = [[' ' for _ in range(width)] for _ in range(height)]

    draw_triangle(canvas, 0, height - 1, height)

    for row in canvas:
        print(''.join(row).rstrip())  # 去掉每行末尾空格
    print()  # 每组数据后空一行
