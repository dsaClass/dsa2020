n = int(input())
for _ in range(n):
    # 初始化可能是重假币和轻假币的集合
    heavy_possible = set('ABCDEFGHIJKL')
    light_possible = set('ABCDEFGHIJKL')
    for _ in range(3):
        left, right, result = input().split()
        if result == 'even':
            # 当天平平衡时，两边的硬币都是真币，从可能的假币集合中移除
            for coin in left + right:
                heavy_possible.discard(coin)
                light_possible.discard(coin)
        elif result == 'up':
            # 左边上升，假币可能在左边且轻，或者在右边且重
            new_heavy = set(left)
            new_light = set(right)
            # 只保留之前也在可能集合中的硬币
            heavy_possible = heavy_possible.intersection(new_heavy)
            light_possible = light_possible.intersection(new_light)
        elif result == 'down':
            # 左边下降，假币可能在左边且重，或者在右边且轻
            new_heavy = set(right)
            new_light = set(left)
            # 只保留之前也在可能集合中的硬币
            heavy_possible = heavy_possible.intersection(new_heavy)
            light_possible = light_possible.intersection(new_light)

    # 确定假币及轻重
    if heavy_possible:
        weight = 'heavy'
        coin = heavy_possible.pop()
    else:
        weight = 'light'
        coin = light_possible.pop()

    print(f"{coin} is the counterfeit coin and it is {weight}.")
                 

