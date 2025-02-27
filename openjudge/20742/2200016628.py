lst = [0,1,1]
def tai(n):
    if n <= 2:
        return lst[n]
    else:
        return tai(n-1)+tai(n-2)+tai(n-3)

n=int(input())

print(tai(n))