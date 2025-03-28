n = int(input())
for _ in range(n):
    coins = set('ABCDEFGHIJKL')
    one = input().split()
    two = input().split()
    three = input().split() # 分别读入各次尝试的数据
    real = set() # 一定真的硬币的集合
    posfakelight = set('ABCDEFGHIJKL') # 可能假且轻的硬币的集合
    posfakeheavy = set('ABCDEFGHIJKL') # 可能假且重的硬币的集合
    # 在没有数据输入的时候每一个都有可能是假的而且轻或者重，所以这两个集合开始时候应该为每一个硬币
    for i in [one, two, three]: # 对于每一个尝试
        if i[-1] == 'even': # 如果这一次尝试天平平衡
            real = real.union(set(i[0]).union(set(i[1]))) # 说明这次的八个硬币都是真的，把原来的real集合和这次的八个硬币取并集
        elif i[-1] == 'up': # 如果这一次尝试天平右端高
            posfakelight &= set(i[1]) # 右端的硬币可能轻
            posfakeheavy &= set(i[0]) # 左端的硬币可能重
        elif i[-1] == 'down': # 如果这一次尝试天平右端低
            posfakelight &= set(i[0]) # 左端的硬币可能轻
            posfakeheavy &= set(i[1]) # 右端的硬币可能重
        # 由于每次尝试都显示可能轻的硬币才是可能轻，所以应该取交集。
    for i in coins.difference(real): # 遍历在硬币集合和一定真硬币集合的差集中的硬币并按照其可能的轻或重输出。由于题目说了测试可以得出结论，所以可以这样。
        if i in posfakelight:
            print(f'{i} is the counterfeit coin and it is light.')
        elif i in posfakeheavy:
            print(f'{i} is the counterfeit coin and it is heavy.')
# 测试发现输出最后是否有空格都可以ac，所以不用考虑示例输出最后那个空格。
