n = int(input())
for _ in range(n):
    poly1 = list(map(int, input().split()))
    poly2 = list(map(int, input().split()))

    coeff_dict = {}

    # 处理第一个多项式
    i = 0
    while i < len(poly1):
        if i + 1 >= len(poly1):
            break
        coeff = poly1[i]
        power = poly1[i + 1]
        if power < 0:
            break
        if power in coeff_dict:
            coeff_dict[power] += coeff
        else:
            coeff_dict[power] = coeff
        i += 2

    # 处理第二个多项式
    j = 0
    while j < len(poly2):
        if j + 1 >= len(poly2):
            break
        coeff = poly2[j]
        power = poly2[j + 1]
        if power < 0:
            break
        if power in coeff_dict:
            coeff_dict[power] += coeff
        else:
            coeff_dict[power] = coeff
        j += 2

    # 生成结果并按幂降序排序
    result = []
    for power in sorted(coeff_dict.keys(), reverse=True):
        coeff = coeff_dict[power]
        if coeff != 0:
            result.append(f"[ {coeff} {power} ]")

    print(' '.join(result))