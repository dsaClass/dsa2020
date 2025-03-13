N, M = map(int, input().split())
nums = list(map(int, input().split()))

for _ in range(M):
    operation = input().split()
    if operation[0] == 'C':
        d = int(operation[1])
        nums = [(num + d) % 65536 for num in nums]
    elif operation[0] == 'Q':
        i = int(operation[1])
        count = sum((num >> i) & 1 for num in nums)
        print(count)