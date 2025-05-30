from functools import lru_cache

# 高精度加法函数
def add(a, b):
    # 让a是更长的那个
    if len(a) < len(b):
        a, b = b, a
    a = list(map(int, a[::-1]))
    b = list(map(int, b[::-1]))
    res = []
    carry = 0
    for i in range(len(a)):
        x = a[i]
        y = b[i] if i < len(b) else 0
        s = x + y + carry
        res.append(str(s % 10))
        carry = s // 10
    if carry:
        res.append(str(carry))
    return ''.join(res[::-1])

def solve_case(m, s):
    n = len(s)

    @lru_cache(None)
    def dp(i, k):
        if k == 0:
            return s[i:]  # 没有加号时，剩下的是一个整体
        min_sum = None
        for j in range(i + 1, n - k + 1):  # j 是分割点
            left = s[i:j]
            right = dp(j, k - 1)
            total = add(left, right)
            if (min_sum is None) or (len(total) < len(min_sum)) or (len(total) == len(min_sum) and total < min_sum):
                min_sum = total
        return min_sum

    return dp(0, m)

# 读取所有数据
def main():
    results = []
    try:
        while True:
            m = int(input())
            s = input().strip()
            results.append(solve_case(m, s))
    except EOFError:
        pass
    for res in results:
        print(res)

main()