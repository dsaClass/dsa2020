r,c=[int(x) for x in input().split()]
matrix=[]
for i in range(r):
    alist=[]
    str1=input()
    for j in range(c):
        alist.append(str1[j])
    matrix.append(alist)
s=0
def f(i,j):
    if matrix[i][j]==".":
        global s
        s+=1
        matrix[i][j]="#"
        for (delta_x,delta_y) in [(1,0),(-1,0),(0,-1),(0,1)]:
            f(i+delta_x,j+delta_y)
            None
rooms=[]
for i in range(1,r-1):
    for j in range(1,c-1):
         if matrix[i][j]==".":
            s=0
            f(i,j)
            rooms.append(s)
print(len(rooms))
print(max(rooms))
