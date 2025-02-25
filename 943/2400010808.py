def sierpinski_triangle(n):
    if n == 1:
        return [' /\\', '/__\\']
    smaller_triangle = sierpinski_triangle(n - 1)
    width = len(smaller_triangle[0])
    top = []
    # 生成顶部三角形，添加合适的前导空格
    for line in smaller_triangle:
        spaces = ' ' * (width // 2 + 1)
        top.append(spaces + line + spaces)
    bottom = []
    # 生成底部两个三角形，正确处理中间的空格
    for line in smaller_triangle:
        new_line = line + ' ' * (width - len(line) + 1) + line
        bottom.append(new_line)
    return top + bottom


while True:
    n = int(input())
    if n == 0:
        break
    result = sierpinski_triangle(n)
    for line in result:
        print(line)
    print()