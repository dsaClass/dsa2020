def jie(rem):
    if rem == 0:
        return 1
    elif rem == 1:
        return 1
    else:
        return jie(rem - 1)+jie(rem - 2)


n = int(input())
print(jie(n))