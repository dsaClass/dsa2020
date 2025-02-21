a=input()
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
flag=True
for j in b:
    if b[j]==1:
        print(j)
        flag=False
        break
if flag:
    print('no')
