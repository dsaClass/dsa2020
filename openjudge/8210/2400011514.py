import sys

# P0200: 河中跳房子
# 二分查找 + 贪心判定

def max_min_jump(L, stones, M):
    # stones: sorted list of intermediate stones distances
    # include start 0 and end L
    positions = [0] + stones + [L]
    # binary search on answer
    lo, hi = 1, L
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        # check if we can ensure minimal jump >= mid by removing <= M stones
        removed = 0
        last = 0  # index of last kept stone
        for i in range(1, len(positions)):
            if positions[i] - positions[last] < mid:
                # need to remove this stone
                removed += 1
            else:
                last = i
        if removed <= M:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans


def main():
    data = sys.stdin.read().strip().split()
    L, N, M = map(int, data[:3])
    stones = list(map(int, data[3:]))
    print(max_min_jump(L, stones, M))

if __name__ == "__main__":
    main()
