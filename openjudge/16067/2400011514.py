import sys

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        n = int(line.strip())
        if n == 0:
            break
        intervals = []
        for _ in range(n):
            a, b = map(int, sys.stdin.readline().strip().split())
            intervals.append((a, b))
        # 按结束时间排序
        sorted_intervals = sorted(intervals, key=lambda x: x[1])
        count = 0
        last_end = -1
        for start, end in sorted_intervals:
            if start >= last_end:
                count += 1
                last_end = end
        print(count)

if __name__ == "__main__":
    main()