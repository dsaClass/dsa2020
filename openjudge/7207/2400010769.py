def generate_magic_square(N):
    
    # 初始化幻方矩阵
    magic_square = [[0] * (2*N - 1) for _ in range(2*N - 1)]
    
    # 第一个数字写在第一行的中间
    i, j = 0, N - 1
    
    num = 1
    while num <= (2*N - 1)**2:
        magic_square[i][j] = num
        num += 1
        
        # 计算下一个数字的位置
        new_i, new_j = (i - 1) % (2*N - 1), (j + 1) % (2*N - 1)
        
        # 如果下一个位置已经有数字，则放在当前位置的下方
        if magic_square[new_i][new_j] != 0:
            i = (i + 1) % (2*N - 1)
        else:
            i, j = new_i, new_j
    
    # 打印幻方
    for row in magic_square:
        print(" ".join(f"{num}" for num in row))

# 输入阶数N
N = int(input())
generate_magic_square(N)
