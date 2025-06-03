import sys


def kadane(arr):
    max_ = arr[0]
    current = arr[0]  # 记录以当前元素结尾的最大和

    for i in range(1, len(arr)):
        current = max(arr[i], current + arr[i])
        max_ = max(max_, current)

    return max_


def main():
    n = int(input())
    matrix = [[0] * n for _ in range(n)]
    if n > 0:
        inp = sys.stdin.read().strip()
        elements = [int(s) for s in inp.split()]
        k = 0
        for r in range(n):
            for c in range(n):
                if k < len(elements):
                    matrix[r][c] = elements[k]
                    k += 1
    max_sum = -float('inf')
    for r1 in range(n):
        temp_sums = [0] * n
        for r2 in range(r1, n):
            for c in range(n):  # 遍历每一列
                temp_sums[c] += matrix[r2][c]
            current_max = kadane(temp_sums)
            if current_max > max_sum:
                max_sum = current_max

    print(max_sum)

if __name__ == '__main__':
    main()
