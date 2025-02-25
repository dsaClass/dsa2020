# 姓名：杨济泽 学号：2200015881
# 又是采用了笨方法，即利用递归枚举所有的子集，找到其中mod7的数，由于n较小
# 所以相对可行，很可以改进
def sums(lst):
    def sums_mini(index, sum):
        if index == len(lst):
            lis.append(sum)
            return
        sums_mini(index + 1, sum + lst[index])
        sums_mini(index + 1, sum)

    lis = []
    sums_mini(0, 0)
    return lis
n = int(input())
for i in range(n):
    s = list(map(int, input().split()))
    a = s[0]
    nums = s[1:]
    num = 0
    res = sums(nums)
    for j in res:
        if j%7 == 0:
            num += 1
    print(num)
