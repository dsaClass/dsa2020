n = int(input())
spe = list(map(int, input().split()))
ans = 0

def guibing(s:list):
    global ans
    if len(s) == 1:
        return s
    k = len(s) // 2
    a = guibing(s[:k])
    b = guibing(s[k:])
    a.append(-1)
    b.append(-1)
    # 这是为了避免出界
    inda, indb = 0, 0
    for i in range(len(s)):
        if a[inda] < b[indb]:
            s[i] = b[indb]
            ans += k + indb - i
            indb += 1
        else:
            s[i] = a[inda]
            inda += 1
    return s

guibing(spe)
print(ans)
