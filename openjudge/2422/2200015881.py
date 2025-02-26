n, m, p = input().split(maxsplit=2)
row, column = int(n), int(m)
number = row * column
dic = {chr(i): i - ord("A") + 1 for i in range(ord("A"), ord("Z") + 1)}
dic[" "] = 0
str1 = ''.join(bin(dic[letter])[2:].zfill(5) for letter in p)
str_fill = str1.ljust(number, '0')
matrix = [[0 for _ in range(column)] for _ in range(row)]
def num_fill(matrix, str_fill):
    top, bottom = 0, row - 1
    left, right = 0, column - 1
    index = 0
    while index < number:
        for i in range(left, right + 1):
            if index < number:
                matrix[top][i] = str_fill[index]
                index += 1
        top += 1
        if top > bottom:
            break
        for i in range(top, bottom + 1):
            if index < number:
                matrix[i][right] = str_fill[index]
                index += 1
        right -= 1
        if right < left:
            break
        for i in range(right, left - 1, -1):
            if index < number:
                matrix[bottom][i] = str_fill[index]
                index += 1
        bottom -= 1
        if bottom < top:
            break
        for i in range(bottom, top - 1, -1):
            if index < number:
                matrix[i][left] = str_fill[index]
                index += 1
        left += 1
        if left > right:
            break
    return matrix
matrix_res = num_fill(matrix, str_fill)
res = ''.join(matrix_res[i][j] for i in range(row) for j in range(column))
print(res)
