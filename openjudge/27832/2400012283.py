n, m = map(int, input().split())
li = list(map(int, input().split()))


def ad(d, lix):
    return [(num + d) % 65536 for num in lix]


def che(i, lix):
    return sum(1 for num in lix if num & (1 << i))


for _ in range(m):
    act, num = input().split()
    num = int(num)
    if act == "C":
        li = ad(num, li)
    elif act == "Q":
        print(che(num, li))