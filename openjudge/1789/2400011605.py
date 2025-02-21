from itertools import permutations

def is_valid(a, b, c, d):
    '''判定4个数能否凑24点'''
    def all_results(x, y):
        '''返回两数四则运算的所有结果'''
        potential = [x+y, x-y, y-x, x*y]
        if x != 0: potential.append(y/x)
        if y != 0: potential.append(x/y)
        return potential
    
    numlist = [a, b, c, d]
    Iter = permutations(numlist, 4)
    #以四个数所有排列顺序形成迭代器
    for a, b, c, d in Iter:
        list1 = all_results(a, b)
        #第一类：((a?b)?c)?d 构成24点
        for i in list1:
            list2 = all_results(i, c)
            for j in list2:
                list3 = all_results(j, d)
                for ans in list3:
                    if abs(ans - 24) <= 1e-8: 
                    #判定24是否是可能结果（考虑了浮点数计算误差）
                        return "YES"
        #第二类：(a?b)?(c?d) 构成24点
        list4 = all_results(c, d)
        Potential = []
        for i in list1:
            for j in list4: Potential = Potential + all_results(i, j)
        for ans in Potential:
            if abs(ans - 24) <= 1e-8: 
            #判定24是否是可能结果（考虑了浮点数计算误差）
                return "YES" 
    return "NO"

while True:
    a, b, c, d = map(int, input().split())
    if a == b == c == d == 0: break
    print(is_valid(a, b, c, d))