def can_form_sticks(sticks, target, used, start, current_length, num_sticks):
    if num_sticks == 0:
        return True
    if current_length == target:
        return can_form_sticks(sticks, target, used, 0, 0, num_sticks - 1)
    
    for i in range(start, len(sticks)):
        if not used[i] and current_length + sticks[i] <= target:
            used[i] = True
            if can_form_sticks(sticks, target, used, i + 1, current_length + sticks[i], num_sticks):
                return True
            used[i] = False
            while i + 1 < len(sticks) and sticks[i] == sticks[i + 1]:
                i += 1
    return False

def find_min_original_length(sticks):
    total_length = sum(sticks)
    max_stick = max(sticks)
    sticks.sort(reverse=True)
    
    for length in range(max_stick, total_length + 1):
        if total_length % length == 0:
            num_sticks = total_length // length
            used = [False] * len(sticks)
            if can_form_sticks(sticks, length, used, 0, 0, num_sticks):
                return length
    return -1

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        sticks = list(map(int, input().split()))
        print(find_min_original_length(sticks))

if __name__ == "__main__":
    main()