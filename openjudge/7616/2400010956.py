def translate(node:dict, now_point:str) -> list:
    # now_point记录了已经该从那个点进行了
    if node[now_point][1] == 0:
        # 是根，那么返回
        return [now_point]
    ans = []
    for i in node[now_point][2:]:
        ans += translate(node, i)
    return ans + [now_point]

n = int(input())
trees = []
for i in range(n):
    temporary = input().split()
    node = {}
    # 使用 自定义的孩子表示法
    # 每棵树记录为一个字典，key为字母，value为列表
    # 节点名 = [层数, 孩子数, 孩子1, 孩子2,……]
    level = 0
    level_need = 1
    next_level_need = 0
    letter = []
    level_letter = []
    # 分层记录节点名
    for j in range(len(temporary)//2):
        level_letter.append(temporary[2 * j])
        node[temporary[2 * j]] = [level, int(temporary[2 * j + 1])]
        next_level_need +=  int(temporary[2 * j + 1])
        level_need -= 1
        if not level_need:
            level += 1
            level_need = next_level_need
            next_level_need = 0
            letter.append(level_letter)
            level_letter = []
            # 进入下一层录入
    # 填充孩子
    # level_point是一个指针列表，标注了对给定的层应该从第几个孩子接着分。
    level_point = [0 for j in range(level)]
    # 恰好是对的
    for j in node:
        if node[j][1]:
            # 有孩子的话
            level = node[j][0] + 1
            # 孩子所在level
            node[j] += letter[level][level_point[level]: level_point[level] + node[j][1]]
            level_point[level] += node[j][1]
    # 到此，树记录成功
    # 我们用迭代的方法返回应该输出的字符串，然后添加到trees之中
    trees += translate(node, letter[0][0])
print(' '.join(trees))



