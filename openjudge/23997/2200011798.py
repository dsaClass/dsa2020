def find_odd_splits(N, start, path, result):
    if N == 0:
        result.append(path)
        return
    for i in range(start, N + 1, 2):
        find_odd_splits(N - i, i + 2, path + [i], result)

if __name__ == "__main__":
    N = int(input())
    result = []
    find_odd_splits(N, 1, [], result)
    result.sort()
    for r in result:
        print(' '.join(map(str, r)))
    print(len(result))
