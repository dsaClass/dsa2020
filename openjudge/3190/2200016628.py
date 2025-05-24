def count_sequences(n):
    from functools import lru_cache

    @lru_cache(None)
    def dfs(pushed, stack_size):
        # pushed: 已经push的元素个数
        # stack_size: 当前栈中元素个数

        # 如果所有元素都已push且栈空，完成一个合法序列
        if pushed == n and stack_size == 0:
            return 1

        res = 0

        # 可以push的话
        if pushed < n:
            res += dfs(pushed + 1, stack_size + 1)

        # 可以pop的话（栈非空）
        if stack_size > 0:
            res += dfs(pushed, stack_size - 1)

        return res

    return dfs(0, 0)


# 读取输入
n = int(input())
print(count_sequences(n))
