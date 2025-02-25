def max_candy_value(n, w, candies):
    # 计算每箱糖果的单位重量价值
    for candy in candies:
        candy.append(candy[0] / candy[1])  # 单位重量价值

    # 按单位重量价值从高到低排序
    candies.sort(key=lambda x: x[2], reverse=True)

    total_value = 0.0
    remaining_weight = w

    for candy in candies:
        if remaining_weight == 0:
            break
        # 尽可能多地取当前糖果
        take_weight = min(candy[1], remaining_weight)
        total_value += take_weight * candy[2]
        remaining_weight -= take_weight

    return total_value


# 读取输入
n, w = map(int, input().split())
candies = []
for _ in range(n):
    v, cw = map(int, input().split())
    candies.append([v, cw])

# 计算最大价值
result = max_candy_value(n, w, candies)

# 输出结果，保留1位小数
print(f"{result:.1f}")