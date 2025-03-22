def can_form_sticks(sticks, used, target, current_length, index, count):
    if count == 0:  # 所有木棍都拼完了，返回 True
        return True
    if current_length == target:  # 当前木棍拼接完成，开始新的木棍
        return can_form_sticks(sticks, used, target, 0, 0, count - 1)
    prev = -1  # 记录上一次尝试的木棍长度，避免重复搜索
    for i in range(index, len(sticks)):
        if used[i] or (current_length + sticks[i] > target):
            continue  # 已使用 或 超出目标长度，则跳过
        if sticks[i] == prev:
            continue  # 剪枝：避免重复使用相同长度的木棍导致冗余计算
        used[i] = True
        if can_form_sticks(sticks, used, target, current_length + sticks[i], i + 1, count):
            return True
        used[i] = False  # 回溯
        prev = sticks[i]  # 记录本次尝试的木棍长度
        if current_length == 0:
            return False  # 剪枝：当前木棍还没开始拼接就失败，说明 `target` 不可行
    return False
def find_min_original_length(sticks):
    total_length = sum(sticks)
    max_length = max(sticks)
    # 逆序尝试可能的原始木棍长度
    for length in range(max_length, total_length + 1):
        if total_length % length == 0:  # 仅尝试 `total_length` 的因子
            used = [False] * len(sticks)  # 记录哪些木棍已经使用
            count = total_length // length  # 需要拼凑的木棍数量

            if can_form_sticks(sticks, used, length, 0, 0, count):
                return length  # 找到最小的 `L`
    return total_length  # 最坏情况下 `L` 只能是 `sum(sticks)`
while True:
    n = int(input().strip())
    if n == 0:
        break  # 结束
    sticks = list(map(int, input().strip().split()))
    sticks.sort(reverse=True)  # 降序排序，优化搜索顺序
    print(find_min_original_length(sticks))
