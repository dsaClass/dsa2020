def dfs(stick, length, last_index):
    global visited
    if stick > total_sticks:
        return True
    if length == target_length:
        return dfs(stick + 1, 0, 0)
    fail_value = 0
    for j in range(last_index, N):
        if not visited[j] and fail_value != lengths[j] and length + lengths[j] <= target_length:
            visited[j] = 1
            if dfs(stick, length + lengths[j], j + 1):
                return True
            fail_value = lengths[j]
            visited[j] = 0
            if length == 0 or length + lengths[j] == target_length:
                return False

while True:
    N = int(input())
    if N:
        lengths = list(map(int, input().split()))
        total_length = sum(lengths)
        possible_lengths = []
        for i in range(1, total_length + 1):
            if total_length % i == 0:
                possible_lengths.append(i)
        lengths.sort(reverse=True)
        for target_length in possible_lengths:
            total_sticks = total_length // target_length
            visited = [0 for j in range(N)]
            if dfs(1, 0, 0):
                print(target_length)
                break
    else:
        break
