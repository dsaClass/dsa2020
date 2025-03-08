import itertools
n = int(input())
A = {'A','B','C','D','E'} #字母集
B = [str(i) for i in range(10)] #数字集
for i in range(n):
    flag1 = 1 #flag1 == 0 意味着前导零情况
    flag2 = 0 #flag2 == 0 意味着No Solution
    s = input().split()
    g = sorted(list(set(s[0]+s[1]+s[2]))) #算式字母集（排序）
    for p in itertools.permutations(B,len(g)): #生成所有可能的数字匹配
        flag1 = 1
        k = dict(zip(g,p)) #利用zip函数给出对应（tuple格式可以直接转dict）
        new = ['','','']
        for i in range(3):
            new[i] += ''.join(k[o] for o in s[i]) #替换
            if new[i][0] == '0' and len(new[i]) > 1: #查前导零，注意个位数允许是0
                flag1 = 0
                break
        if flag1 == 1:
            if int(new[0])+int(new[1]) == int(new[2]):
                print(new[0]+'+'+new[1]+'='+new[2])
                flag2 = 1
                break
    if not flag2:
        print('No Solution')

