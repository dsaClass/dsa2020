def main():
    # 读取输入
    clocks = []
    for _ in range(3):
        clocks.extend(map(int, input().split()))
    
    # 定义每种移动影响的时钟
    moves = [
        [0, 1, 3, 4],  # 移动1
        [0, 1, 2],     # 移动2
        [1, 2, 4, 5],  # 移动3
        [0, 3, 6],     # 移动4
        [1, 3, 4, 5, 7],  # 移动5
        [2, 5, 8],     # 移动6
        [3, 4, 6, 7],  # 移动7
        [6, 7, 8],     # 移动8
        [4, 5, 7, 8]   # 移动9
    ]
    
    # 枚举每种移动的次数（0到3次）
    min_steps = float('inf')
    best_sequence = []
    
    for m1 in range(4):
        for m2 in range(4):
            for m3 in range(4):
                for m4 in range(4):
                    for m5 in range(4):
                        for m6 in range(4):
                            for m7 in range(4):
                                for m8 in range(4):
                                    for m9 in range(4):
                                        # 计算每种移动后的时钟状态
                                        temp_clocks = clocks.copy()
                                        for _ in range(m1):
                                            for clock in moves[0]:
                                                temp_clocks[clock] = (temp_clocks[clock] + 1) % 4
                                        for _ in range(m2):
                                            for clock in moves[1]:
                                                temp_clocks[clock] = (temp_clocks[clock] + 1) % 4
                                        for _ in range(m3):
                                            for clock in moves[2]:
                                                temp_clocks[clock] = (temp_clocks[clock] + 1) % 4
                                        for _ in range(m4):
                                            for clock in moves[3]:
                                                temp_clocks[clock] = (temp_clocks[clock] + 1) % 4
                                        for _ in range(m5):
                                            for clock in moves[4]:
                                                temp_clocks[clock] = (temp_clocks[clock] + 1) % 4
                                        for _ in range(m6):
                                            for clock in moves[5]:
                                                temp_clocks[clock] = (temp_clocks[clock] + 1) % 4
                                        for _ in range(m7):
                                            for clock in moves[6]:
                                                temp_clocks[clock] = (temp_clocks[clock] + 1) % 4
                                        for _ in range(m8):
                                            for clock in moves[7]:
                                                temp_clocks[clock] = (temp_clocks[clock] + 1) % 4
                                        for _ in range(m9):
                                            for clock in moves[8]:
                                                temp_clocks[clock] = (temp_clocks[clock] + 1) % 4
                                        
                                        # 检查是否所有时钟都指向12点
                                        if all(clock == 0 for clock in temp_clocks):
                                            # 计算总移动次数
                                            total_steps = m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9
                                            if total_steps < min_steps:
                                                min_steps = total_steps
                                                best_sequence = [m1, m2, m3, m4, m5, m6, m7, m8, m9]
    
    # 输出结果
    result = []
    for i in range(9):
        if best_sequence[i] > 0:
            result.extend([str(i+1)] * best_sequence[i])
    print(' '.join(result))

if __name__ == "__main__":
    main()