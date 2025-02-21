n=int(input())
l=[input() for _ in range(n)]
def f(s):
    string=[]
    for i in s:
        if i=='(' or i== '[' or i=='{':
            string.append(i)
        elif i == ')':
            if string !=[] and string[-1]=='(':
                string.pop()
            else:
                return 'NO'
        elif i == ']':
            if string !=[] and string[-1]=='[':
                string.pop()
            else:
                return 'NO'
        elif i == '}':
            if string !=[] and string[-1]=='{':
                string.pop()
            else:
                return 'NO'
    if string==[]:
        return 'YES'
    else:
        return 'NO'
for i in l:
    print(f(i))    
