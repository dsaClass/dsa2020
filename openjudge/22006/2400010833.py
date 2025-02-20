'''2400010833 闵诗珈
递归
将 n-1 个盘子从 A 移动到 B，使用 C 作为中介。
将第 n 个盘子（最大的）从 A 移动到 C。
将 n-1 个盘子从 B 移动到 C，使用 A 作为中介。'''

def hanoi(n,a,b,c):
    if n == 1:
        print(f'{a}->{c}')
        return
    else:
        hanoi(n-1,a,c,b)
        print(f'{a}->{c}')
        hanoi(n-1,b,a,c)

n=int(input())
hanoi(n,'A','B','C')

