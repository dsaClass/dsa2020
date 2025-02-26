s=input()
space=0
for i in range(len(s)):
    if s[i]!=' ':
        continue
    space+=1
    if space==2:
        break
r,c=map(int,s[:i].split())
s=s[i+1:]
def trans(c):
    if c==' ':
        return '00000'
    else:
        n=ord(c)-64
        result=''
        while n>0:
            result=str(n%2)+result
            n//=2
        result='0'*(5-len(result))+result
        return result
t=''
for i in s:
    t=t+trans(i)
t=t+(r*c-len(t))*'0'

def move(i,j,dir):
    if dir==0:
        return i,j+1
    if dir==1:
        return i+1,j
    if dir==2:
        return i,j-1
    if dir==3:
        return i-1,j
    
def turn(dir):
    dir +=1
    dir%=4
    return dir

dir=0
i=j=0
matrix=[]

for _ in range(r):
    matrix.append([None]*c)

for k in range(r*c):
    matrix[i][j]=t[k]
    m,n=move(i,j,dir)
    if m>r-1 or m<0 or n>c-1 or n<0:
        dir=turn(dir)
        i,j=move(i,j,dir)
    elif matrix[m][n]!=None:
        dir=turn(dir)
        i,j=move(i,j,dir)
    else:
        i,j=m,n

out=''
for i in range(r):
    matrix[i]=''.join(matrix[i])

print(''.join(matrix))

