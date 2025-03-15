def judge(n):
    if len(n) != len(str):
        return "NO"
    data=[]
    i=0
    j=0
    while i < len(n) or j < len(str):
        if len(data)>0 and data[-1] == n[i]:
            del data[-1]
            i+=1
        else:
            if j >= len(str):
                break
            data.append(str[j])
            j+=1
    if i == len(n):
        return "YES"
    else:
        return "NO"
str=input()
while True:
    try:
        s=input()
        print(judge(s))
    except EOFError:
        break
