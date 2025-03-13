def find_path(x,y):
    if x>=N or y>=N or maze[x][y]=='1':
        return False
    if (x==N-1 and y==N-2) or (x==N-2 and y==N-1):
        return True
    else:
        return find_path(x+1,y) or find_path(x,y+1)
        

N=int(input())
maze=[() for _ in range(N)]
for i in range(N):
    maze[i]=input().split()
if(find_path(0,0)):
    print("Yes")
else:
    print("No")

