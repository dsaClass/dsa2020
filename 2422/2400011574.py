def dfs(r,c,total):
    matrix=[[None for _ in range(c)] for _ in range(r)]
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    x,y=0,0
    sta=0
    index=0
    while index<len(total):
        matrix[x][y]=total[index]
        index+=1
        nx,ny=x+dx[sta],y+dy[sta]
        if not(0<=nx<r and 0<=ny<c and matrix[nx][ny] is None):
            sta=(sta+1)%4
            nx, ny = x + dx[sta], y + dy[sta]#
        x=nx
        y=ny
    return matrix

ins=input()
pre=0
for d in range(len(ins)):
    if ins[d].isdigit():
        pre=d
s1=ins[:pre+1]
r,c=map(int,s1.split())
s=ins[pre+2:]
lst=[]
for char in s:
    if char == " ":
        a='00000'
        lst.append(a)
    else:
        num=['0','0','0','0','0']
        n=int(ord(char)-64)
        a=bin(n)[2:]
        t=5-len(a)
        for i in range(len(a)):
            num[i+t]=a[i]
        lst.append(''.join(num))
zero=r*c-5*len(lst)
lst.append(zero*'0')
total=''.join(lst)

result=[]
matrix=dfs(r,c,total)
for p in range(len(matrix)):
    for q in range(len(matrix[0])):
        result.append(matrix[p][q])
print(''.join(result))