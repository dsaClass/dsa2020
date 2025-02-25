# 就是很简单的排列，应该没有什么改进空间了
n = int(input())  
s = list(map(int, input().split()))  
k = int(input()) 
sort_s = sorted(s, reverse=True)
numbers = sort_s[:k]
for number in numbers:
    print(number)
