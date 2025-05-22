def cantor(n):
    length = 3 ** n
    s = ['*'] * length

    def remove_middle(l, r, depth):
        if depth == 0:
            return
        third = (r - l + 1) // 3 #一段的长度
        mid_start = l + third
        mid_end = r - third
        for i in range(mid_start, mid_end + 1):
            s[i] = '-'
        remove_middle(l, mid_start - 1, depth - 1)
        remove_middle(mid_end + 1, r, depth - 1)

    remove_middle(0, length - 1, n)
    print(''.join(s))

# 示例使用
n = int(input())
cantor(n)