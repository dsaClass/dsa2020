Status0 = list(map(int, input()))
Status1 = list(map(int,input()))
n = len(Status0)
answer=n+100
for i in range(2):
	totalPush=0
	status=Status0[:]+[0]
	if i==1:
		status[0]=1-status[0]
		status[1]=1-status[1]
		totalPush+=1
	for k in range(1,len(Status0)):
		if status[k-1]!=Status1[k-1]:
			totalPush+=1
			status[k]=1-status[k]
			status[k+1]=1-status[k+1]
	if status[n-1]==Status1[-1]:
		answer=min(answer,totalPush)
if answer<=len(Status0):
	print(answer)
else:
	print("impossible")

