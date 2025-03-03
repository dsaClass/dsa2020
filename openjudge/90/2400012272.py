R,C = map(int,input().split())
grid = []
for _ in range(R):
     line = [int(i) for i in input().split()] 
     grid.append(line)
def get_available_points(x,y): 
    result = [] 
    for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
        if 0<=nx<R and 0<=ny<C and grid[nx][ny] < grid[x][y]: 
            result.append((nx,ny)) 
    return result
memory = [[0 for _ in range(110)] for _ in range(110)]
def f(x,y):
    if memory[x][y]:
        return memory[x][y] 
    available_points = get_available_points(x,y) 
    if len(available_points) == 0: 
        return 1
    res = 1 + max(f(i,j) for i,j in available_points)
    memory[x][y] = res
    return res
max_length = max(f(i,j) for i in range(R) for j in range(C))
print(max_length)