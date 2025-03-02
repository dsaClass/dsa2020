l=input().split(maxsplit=2)
r,c=int(l[0]),int(l[1])

def change(x):
    if x==' ':
        return '00000'
    else:
        a=ord(x)-ord('A')+1
        s=bin(a)
        s=s[2:]
        return f'{s:>05}'

ss=''
for _ in l[2]:
    ss+=change(_)

s=f'{ss:<0{r * c}}'

i_min,i_max,j_min,j_max=1,r-1,0,c-1 # 从开始走之后，不论怎样都不可能转一圈回到第一行。
i=j=count=0
matrix=[['0' for _ in range(c)]for _ in range(r)]

while count<r*c:
    if i<i_min:
        if j<j_max:
            matrix[i][j]=s[count]
            j+=1
            count+=1
        elif j==j_max:
            matrix[i][j] = s[count]
            i += 1
            j_max-=1
            count += 1
    elif i>i_max:
        if j>j_min:
            matrix[i][j]=s[count]
            j-=1
            count+=1
        elif j==j_min:
            matrix[i][j] = s[count]
            i -= 1
            j_min+=1
            count += 1
    elif j<j_min:
        if i>i_min:
            matrix[i][j]=s[count]
            i-=1
            count+=1
        elif i==i_min:
            matrix[i][j] = s[count]
            j += 1
            i_min+=1
            count += 1
    elif j>j_max:
        if i<i_max:
            matrix[i][j]=s[count]
            i+=1
            count+=1
        elif i==i_max:
            matrix[i][j] = s[count]
            j -= 1
            i_max-=1
            count += 1

for i in range(r):
    for j in range(c):
        print(matrix[i][j],end='')