from collections import deque
N=int(input())
map=[list(map(int,input().split())) for _ in range(N)]
movement=[(1,0),(0,1)]
visited=set()
def legal(step):
	i,j=step
	if 0<=i<=N-1 and 0<=j<=N-1 and map[i][j]!=1 and step not in visited:
		return True
	else:
		return False
def bfs(map):
	queue=deque()
	start=(0,0)
	queue.append(start)
	visited.add(start)
	while queue:
		position=queue.popleft()
		if position==(N-1,N-1):
			return "Yes"
		for move in movement:
			dx,dy=move
			x,y=position
			next_step=(x+dx,y+dy)
			if legal(next_step):
				queue.append(next_step)
				visited.add(next_step)
			
	else:
		return "No"
result=bfs(map)
print(result)