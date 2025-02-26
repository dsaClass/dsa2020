def maximize_number(n):
    # 将数字转换为字符列表，方便修改
    digits = list(str(n))

    # 遍历每一位，找到第一个 '2' 并改为 '3'
    for i in range(len(digits)):
        if digits[i] == '2':
            digits[i] = '3'
            break  # 只修改第一个 '2'

    # 将字符列表转换回数字
    return int(''.join(digits))


n = int(input())
print(maximize_number(n))