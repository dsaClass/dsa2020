def josephus_simulation(n, k):
    # 初始化囚犯列表
    prisoners = list(range(1, n + 1))
    result = []
    index = 0  # 开始的位置

    while len(prisoners) > 1:
        # 计算下一个要处决的囚犯的索引
        index = (index + k - 1) % len(prisoners)
        # 将该囚犯添加到结果列表中
        result.append(prisoners[index])
        # 将该囚犯从列表中移除
        prisoners.pop(index)

    # 最后剩下的囚犯不会被处决
    return result

# 读取输入
n, k = map(int, input().split())

# 调用函数并输出结果
output = josephus_simulation(n, k)
print(' '.join(map(str, output)))