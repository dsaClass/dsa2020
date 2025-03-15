n = int(input())
ways = [0] * (n + 1)
ways[0] = 1
for i in range(1, n+1):
    ways[i] = ways[i-1]
    if i >= 3:
        ways[i] += ways[i -3]
    if i >= 5:
        ways[i] += ways[i - 5]
print(ways[n])