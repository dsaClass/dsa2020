def max_candy(N, M, relations):
    INF = float('inf')
    candy = [INF] * (N + 1)
    candy[1] = 0

    # Relax edges
    for _ in range(N - 1):
        for a, b, c in relations:
            if candy[a] != INF and candy[b] > candy[a] + c:
                candy[b] = candy[a] + c

    # The maximum difference is candy[N] - candy[1]
    return candy[N]

# Read input
N, M = map(int, input().split())
relations = []
for _ in range(M):
    a, b, c = map(int, input().split())
    relations.append((a, b, c))

# Compute and print the result
print(max_candy(N, M, relations))