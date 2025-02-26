def first_unique_char(s):
    # 使用字典记录每个字符出现的次数
    char_count = {}

    # 第一次遍历，统计每个字符的出现次数
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # 第二次遍历，找到第一个只出现一次的字符
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index

    # 如果没有找到，返回 -1
    return -1

s = input()
print(first_unique_char(s))