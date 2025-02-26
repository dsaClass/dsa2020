def is_divisible_by_5(A):
    answer = ""
    current_num = 0
    for i, char in enumerate(A):
        current_num = (current_num * 2 + int(char)) % 5
        answer += '1' if current_num == 0 else '0'
    return answer
A = str(input())
print(is_divisible_by_5(A))