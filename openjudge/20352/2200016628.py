def positions(S, S1):
    s1_positions = []
    start = 0
    while True:
        pos = S.find(S1, start)
        if pos == -1:
            break
        s1_positions.append(pos)
        start = pos + len(S1)

    if not s1_positions :
        return "no"

    return " ".join(map(str,s1_positions))

n = int(input())
for _ in range(n):
    S, S1= input().split()
    print(positions(S, S1))