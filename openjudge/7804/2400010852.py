def f(s):
    res=[]
    temp=[]
    for i in s:
        if i not in res:
            if i not in temp:
                temp.append(i)
            else:
                temp.remove(i)
                res.append(i)
    if temp:
        return temp[0]
    else:
        return 'no'
s=input()
print((f(s)))
