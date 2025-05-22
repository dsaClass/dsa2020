def is_valid(length, woods, k):
    # 判断是否能用给定的长度切出至少 k 段
    return sum(wood // length for wood in woods) >= k

def max_piece_length(woods, k):
    left, right = 1, max(woods)
    best = 0

    while left <= right:
        mid = (left + right) // 2
        if is_valid(mid, woods, k):
            best = mid  # mid 可行，尝试更大
            left = mid + 1
        else:
            right = mid - 1

    return best

# 读取输入
N, K = map(int, input().split())
woods = [int(input()) for _ in range(N)]

# 特殊情况处理：无论如何都切不出K段
if sum(wood for wood in woods) < K:
    print(0)
else:
    print(max_piece_length(woods, K))