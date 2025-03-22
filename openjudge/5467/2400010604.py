def main():
    import sys
    
    # 读取输入
    input = sys.stdin.read
    data = input().split()
    
    # 读取有多少组多项式
    n = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(n):
        # 读取第一个多项式
        poly1 = []
        while index < len(data):
            coef = int(data[index])
            exp = int(data[index+1])
            if exp < 0:
                index += 2
                break
            poly1.append((coef, exp))
            index += 2
        
        # 读取第二个多项式
        poly2 = []
        while index < len(data):
            coef = int(data[index])
            exp = int(data[index+1])
            if exp < 0:
                index += 2
                break
            poly2.append((coef, exp))
            index += 2
        
        # 使用字典存储多项式系数
        poly_sum = {}
        
        # 处理第一个多项式
        for coef, exp in poly1:
            if exp in poly_sum:
                poly_sum[exp] += coef
            else:
                poly_sum[exp] = coef
        
        # 处理第二个多项式
        for coef, exp in poly2:
            if exp in poly_sum:
                poly_sum[exp] += coef
            else:
                poly_sum[exp] = coef
        
        # 去除系数为零的项，并按幂数从高到低排序
        filtered_poly = sorted([(exp, coef) for exp, coef in poly_sum.items() if coef != 0], reverse=True, key=lambda x: x[0])
        
        # 格式化输出
        output = ["[ {} {} ]".format(coef, exp) for exp, coef in filtered_poly]
        results.append(" ".join(output))
    
    # 输出结果
    for result in results:
        print(result.strip())
    
if __name__ == "__main__":
    main()