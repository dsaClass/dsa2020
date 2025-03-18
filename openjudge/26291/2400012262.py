def find(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n == 2:
        return 1
    return find(n-1)+find(n-2)
n=int(input())
print(find(n))
