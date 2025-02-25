def max_movies(n, movies):
    # 按照结束时间升序排序，如果结束时间相同，则按开始时间升序排序
    movies.sort(key=lambda x: (x[1], x[0]))

    count = 0
    last_end = -1

    for start, end in movies:
        if start >= last_end:
            count += 1
            last_end = end

    return count


# 处理多组数据
while True:
    n = int(input())
    if n == 0:
        break
    movies = []
    for _ in range(n):
        start, end = map(int, input().split())
        movies.append((start, end))
    print(max_movies(n, movies))