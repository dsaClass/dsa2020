n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
c[0], c[-1] = 0, 0
buffer = {}


def divide_dp(start: int, end: int, left: bool, right: bool) -> int:
    '''二分动归，通过中间座位最终结算情况计算对应情况下的最大值，left与right变量记录了这一段开始坐人的时候，左右两侧的状态，超出座位范围记为False'''
    global n, a, b, c
    # 将某个座位有一个人坐下时两侧有人的数量记做状态标号
    buffer.setdefault((start, end, left, right), -1)
    if buffer.setdefault((start, end, left, right), -1) != -1:
        return buffer[(start, end, left, right)]
    if start == end - 1:
        # 第一递归出口
        if not left:
            if not right:
                buffer[(start, end, left, right)] = max(
                    a[start] + b[end], b[start] + a[end])
                return buffer[(start, end, left, right)]
            else:
                buffer[(start, end, left, right)] = max(
                    a[start] + c[end], b[start] + b[end])
                return buffer[(start, end, left, right)]
        else:
            if not right:
                buffer[(start, end, left, right)] = max(
                    b[start] + b[end], c[start] + a[end])
                return buffer[(start, end, left, right)]
            else:
                buffer[(start, end, left, right)] = max(
                    b[start] + c[end], c[start] + b[end])
                return buffer[(start, end, left, right)]
    if start == end:
        # 第二递归出口
        if not left:
            if not right:
                buffer[(start, end, left, right)] = a[start]
                return buffer[(start, end, left, right)]
            else:
                buffer[(start, end, left, right)] = b[start]
                return buffer[(start, end, left, right)]
        else:
            if not right:
                buffer[(start, end, left, right)] = b[start]
                return buffer[(start, end, left, right)]
            else:
                buffer[(start, end, left, right)] = c[start]
                return buffer[(start, end, left, right)]
    # 继续二分
    mid = (start + end) // 2
    # 选择mid的情况，即0,1,2，对应有四种情况
    ans = divide_dp(start, mid - 1, left, True) + \
        divide_dp(mid + 1, end, True, right) + a[mid]
    # mid选择0
    ans = max(ans, divide_dp(start, mid - 1, left, True) +
              divide_dp(mid + 1, end, False, right) + b[mid])
    ans = max(ans, divide_dp(start, mid - 1, left, False) +
              divide_dp(mid + 1, end, True, right) + b[mid])
    # mid选择1的两种情况
    ans = max(ans, divide_dp(start, mid - 1, left, False) +
              divide_dp(mid + 1, end, False, right) + c[mid])
    # mid选择2
    buffer[(start, end, left, right)] = ans
    return ans


print(divide_dp(0, n-1, False, False))
