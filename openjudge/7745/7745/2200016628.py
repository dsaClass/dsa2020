nums = list(map(int, input().split()))
odd_nums = [num for num in nums if num % 2 == 1]
even_nums = [num for num in nums if num % 2 == 0]
odd_nums.sort(reverse=True)
even_nums.sort()
ans = odd_nums + even_nums
print(" ".join(map(str, ans)))