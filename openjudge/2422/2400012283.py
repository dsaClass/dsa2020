def jiema(c):
    if c ==' ':
        return '00000'
    return bin(ord(c) - 64)[2:].zfill(5)

def matr(r, c, ming):
    mat = [[0] * c for _ in range(r)]
    top, bottom, left, right = 0, r - 1, 0, c - 1
    num = 0
    while num < len(ming):  # 只要 num 小于 ming 的长度
        for i in range(left, right + 1):  # 从左到右填充
            if num < len(ming):  # 确保不越界
                mat[top][i] = ming[num]
                num += 1
        top += 1  # 顶部边界向下移动
        if top > bottom:  # 检查是否填充完
            break

        for j in range(top, bottom + 1):  # 从上到下填充
            if num < len(ming):  # 确保不越界
                mat[j][right] = ming[num]
                num += 1
        right -= 1  # 右边界向左移动
        if right < left:  # 检查是否填充完
            break

        for p in range(right, left - 1, -1):  # 从右到左填充
            if num < len(ming):  # 确保不越界
                mat[bottom][p] = ming[num]
                num += 1
        bottom -= 1  # 底部边界向上移动
        if bottom < top:  # 检查是否填充完
            break

        for q in range(bottom, top - 1, -1):  # 从下到上填充
            if num < len(ming):  # 确保不越界
                mat[q][left] = ming[num]
                num += 1
        left += 1  # 左边界向右移动
        if left > right:  # 检查是否填充完
            break

    ans = ''
    for i in mat:
        ans+="".join(str(j)for j in i)
    return ans

demand = input().replace(' ', '*', 2)
r, c, code = demand.split('*')
r, c = int(r), int(c)
ming = ''.join([jiema(ch) for ch in code])
print(matr(r, c, ming))