while True:
    try:
        n, m = map(int, input().split())
        cups = [1] * n
        sets = {i + 1: [i + 1] for i in range(n)}
        positions = list(range(1, n + 1))

        for _ in range(m):
            x, y = map(int, input().split())
            x_set = positions[x - 1]
            y_set = positions[y - 1]
            if x_set == y_set:
                print("Yes")
            else:
                print("No")
                sets[x_set].extend(sets[y_set])
                for item in sets[y_set]:
                    positions[item - 1] = x_set
                sets[y_set] = []
                cups[x_set - 1] = 1
                cups[y_set - 1] = 0

        active_cups_count = sum(cups)
        print(active_cups_count)
        active_cups = [i + 1 for i in range(n) if cups[i] == 1]
        print(" ".join(map(str, active_cups)))
    except EOFError:
        break
