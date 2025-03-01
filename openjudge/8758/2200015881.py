def simplify(n):
    if n == 0:
        return "0"
    s = bin(n)[2:]
    t = len(s)
    res = []
    for i in range(t - 1, -1, -1): 
        if s[i] == '1':
            str_s = simplify(t - 1 - i)
            if str_s == "2(0)":
                res.insert(0, "2")
            else:
                res.insert(0, f"2({str_s})")
    return "+".join(res)
n = int(input().strip())
res = simplify(n)
print(res)     
