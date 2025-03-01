def convert(l:str) -> str:
    """
    把字符转换成二进制代码的字符串。
    :param l: 字符
    :return: 二进制代码的字符串
    """
    if l == ' ':
        return '00000'
    else:
        cache = ord(l) - 64
        cache = bin(cache)
        cache = cache[2:] # 这里本来是removeprefix('0b')，但是OJ的Python版本是3.8。:(
        cache = f'{cache:0>5}'
        return cache

# 生成准备填进矩阵里面的二进制串。
# temp = list(input())
# r = int(''.join((temp[0:temp.index(' ')])))
# temp = temp[temp.index(' ') + 1:]
# c = int(''.join((temp[0:temp.index(' ')])))
# text = ''.join(temp[temp.index(' ') + 1:])

r, c, text = input().split(sep=' ', maxsplit=2)
r, c = int(r), int(c)
cnt = r * c
s = ''.join(list(map(convert, list(text))))
s += (cnt - len(s)) * '0'
s = list(reversed(s)) # 变成一个倒着的列表，因为.pop()的效率较高。
# 准备矩阵。
m = [[-1 for j in range(c)] for i in range(r)]
# 填充状态初始化
h_fill = c
v_fill = r - 1
status = 'hr' # 状态标志：向右移动
x, y = 0, 0 # “指针”位置
while s: # 如果s是一个空列表，这说明已经填充结束。
    if status == 'hr':
        for i in range(h_fill):
            m[x][y + i] = s.pop()
        y += h_fill - 1
        x += 1
        h_fill -= 1
        status = 'vd' # 状态标志：向下移动
    elif status == 'vd':
        for i in range(v_fill):
            m[x + i][y] = s.pop()
        x += v_fill - 1
        y -= 1
        v_fill -= 1
        status = 'hl' # 状态标志：向左移动
    elif status == 'hl':
        for i in range(h_fill):
            m[x][y - i] = s.pop()
        y -= h_fill - 1
        x -= 1
        h_fill -= 1
        status = 'vu' # 状态标志：向上移动
    elif status == 'vu':
        for i in range(v_fill):
            m[x - i][y] = s.pop()
        x -= v_fill - 1
        y += 1
        v_fill -= 1
        status = 'hr' # 状态标志：向右移动
    else:
        pass
# 分别融合m中每一行的字符。
m = [''.join(m[i]) for i in range(r)]
# 融合m中的所有字符。
print(''.join(m))
