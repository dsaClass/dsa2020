def main():
    while True:
        n = int(input())
        if n == 0:
            break
        movies = []
        for _ in range(n):
            start, end = map(int, input().split())
            movies.append((start, end))
        movies.sort(key=lambda x: x[1])
        ans = 0
        current_end_time = float('-inf')
        for start, end in movies:
            if start >= current_end_time:
                ans += 1
                current_end_time = end
        print(ans)
if __name__ == "__main__":
    main()