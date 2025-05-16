from collections import Counter
s = input()
count = Counter(s) #字典保存 时间复杂度o(n)
for ch in s:
    if count[ch] == 1: #遍历 时间复杂度o(n)
        print(ch)
        break
else:
    print("no")

#整体时间复杂度o(n)