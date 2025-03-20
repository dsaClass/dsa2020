def find_odd_combinations(n, start, path, result):
    if n == 0:
        result.append(path)
        return
    for i in range(start, n + 1, 2):
        find_odd_combinations(n - i, i + 2, path + [i], result)

def main():
    n = int(input())
    result = []
    find_odd_combinations(n, 1, [], result)
    
    for combination in result:
        print(" ".join(map(str, combination)))
    
    print(len(result))

if __name__ == "__main__":
    main()