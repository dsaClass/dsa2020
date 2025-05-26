n = int(input())
# 减去 "+" 和 "=" 所需的 4 根火柴棍，剩下的用来拼数字
left = n - 4
# 每个数字所需的火柴棍数
pre = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4,'5': 5, '6': 6, '7': 3, '8': 7, '9': 6}
# 计算一个数字拼成需要的火柴棍数
def matchsticks(num):
    count = 0
    for ch in str(num):
        count += pre[ch]
    return count
ans = 0
# 如果剩下的火柴棍数少于8直接无解(枚举)
if left > 8:
    # 遍历所有可能的 a 和 b（限制为 < 1000 是为了满足 n <= 24 的限制）
    for a in range(1000):
        for b in range(1000):
            c = a + b
            total = matchsticks(a) + matchsticks(b) + matchsticks(c)
            if total == left:
                ans += 1
# 输出满足条件的等式个数
print(ans)























