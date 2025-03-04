'''
最开始的思路
s=input()
print(int(s)+10**(len(s)-s.index('2')-1))
'''

#考虑一下如何让代码行数最少
print(str(input()).replace('2', '3', 1))