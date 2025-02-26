# 发现操作复合符合交换律，因此按编号从小到大广搜即可
# “图权”并不相同，仍然应该使用dfs

state = []
state += list(map(int, input().split()))
state += list(map(int, input().split()))
state += list(map(int, input().split()))
ans = 27
# 理论最大答案
ans_list = []
operate = [None, (1, 2, 4, 5), (1, 2, 3), (2, 3, 5, 6), (1, 4, 7), (2, 4, 5, 6, 8), (3, 6, 9), (4, 5, 7, 8), (7, 8, 9), (5, 6, 8, 9)]
# 打表记录操作种类
def adapt(manner:int, step:int, recent:list, done:list):
    global ans, operate, ans_list
    '''测试用
    if 4 in done and 5 in done and 8 in done:
        1 == 1'''
    if sum(recent) == 0:
        # 已经调好了，此路径到达终点
        ans = step
        ans_list = done.copy()
        # 若step更大，则已经终止
        return None
    if manner == 10:
        return None
    now = recent.copy()
    now_done = done.copy()
    adapt(manner + 1, step, now, now_done)
    for i in range(3):
        # 进行i+1次操作
        step += 1
        now_done.append(manner)
        if step >= ans:
            # 如果已经不是最优，则不再测试
            return None
        for j in operate[manner]:
            now[j - 1] += 1
            now[j - 1] %= 4
        adapt(manner + 1, step, now, now_done)
    return None

adapt(1, 0, state, ans_list)
print(' '.join(map(str, ans_list)))
