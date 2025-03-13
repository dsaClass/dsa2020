s=input()

def arrange(s):
    if len(s)==1:
        return [s]
    result=[]
    for i in range(len(s)):
        for sub_arrange in arrange(s[:i]+s[i+1:]):
            result.append(s[i]+sub_arrange)
    return result

for a in arrange(s):
    print(a)