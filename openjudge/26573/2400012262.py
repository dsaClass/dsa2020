import math
n = int(input())
s = 3**n
def find(a):
    if a == 1 :
        return '*'
    return find(a//3) + '-'*(a//3) + find(a//3)
print(find(s))
