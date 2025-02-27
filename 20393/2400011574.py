s=input()
lst=[]
for i in s:
    lst.append(i)
for j in range(len(lst)):
    if lst[j]=='2':
        lst[j]='3'
        break
print(''.join(lst))