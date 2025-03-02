def cut(N,M):
    width = min(N,M)
    length = max(N,M)
    number = 1
    while width != length:
        length_new = length - width
        number += 1
        width_new = width
        width = min(length_new,width_new)
        length = max(length_new,width_new)
    return number
N,M = map(int,input().split())
print(cut(N,M))