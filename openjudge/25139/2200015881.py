# 姓名：杨济泽 学号：2200015881  
# 首先按照题目顺序，最先要求的就是考虑到字母更换数值问题，因此建立函数transfer，
# 由于要整体采取枚举法（这是因为题目中要求从小到大算解，
# 因此也要从小到大枚举可能性），所以首先按照ABCDE的顺序建立字典用于匹配数值
#（这是由于先更新A再更新B会加快比较速度），a字典用于整体更新数值，
# 如果映射不完整应当判定为错误返回-1，result用于储存替换后的数值，
# 同时要防止第一位为0的问题出现。renum函数用于递归，是采用枚举法的关键，
# 判断标准就是满足两个相加等于第三个这个等式，相当于从0-9为每个字母分配值，
# 如果分配值不正确就删掉重新分配，如果分配值正确就直接返回true
#（可以减少再分配其他字母导致的浪费），直到每个字母都分配到为止，
# 进行递归的时候每次加一位数上去进行调整，最后输出结果
def count(s1, s2, s3):
    a = {}
    letters = 'ABCDE'
    def transfer(s):
        result = 0
        for i in s:
            if i not in a:
                return -1
            result = result * 10 + a[i] 
        if s and a[s[0]] == 0 and len(s) > 1:
            return -1
        return result
    def renum(position):
        if position == len(letters):
            n1, n2, n3 = transfer(s1), transfer(s2), transfer(s3)
            if n1 >= 0 and n2 >= 0 and n3 >= 0 and n1 + n2 == n3:
                print(f"{n1}+{n2}={n3}")
                return True
        else:
            for k in range(10):
                if k not in a.values(): 
                    a[letters[position]] = k
                    if renum(position + 1):
                        return True
                    del a[letters[position]]  
        return False
    return renum(0)
n = int(input())
for i in range(n):
   s1,s2,s3 = input().split()
   if not count(s1,s2,s3):
      print("No Solution")
