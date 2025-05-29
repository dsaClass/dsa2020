import sys

def main():
    n, c = map(int, sys.stdin.readline().split())
    positions = [int(sys.stdin.readline().strip()) for _ in range(n)]
    positions.sort()
    
    left = 0
    right = positions[-1] - positions[0]
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        count = 1
        prev = positions[0]
        for pos in positions[1:]:
            if pos - prev >= mid:
                count += 1
                prev = pos
                if count >= c:
                    break
        if count >= c:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    print(answer)

if __name__ == "__main__":
    main()