import re
n = int(input())
def euqal(x,y):
    for i in range(-20,21):
        k1 = re.sub(r'[a-zA-Z]',str(i),x)
        k2 = re.sub(r'[a-zA-Z]',str(i),y)
        if eval(k1) != eval(k2):
            return 0
    return 1
for i in range(n):
    x = input()
    y = input()
    if euqal(x,y):
        print('YES')
    else:
        print('NO')
