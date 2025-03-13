n,x=map(int,input().split())
coins=list(map(int,input().split()))
achi={0:set()}
todolist=[]
def my_add(mon,coinset):
    if mon>x:
        return
    if mon in achi.keys():
        achi[mon]=achi[mon]&coinset
    else:
        achi[mon]=coinset
for i in coins:
    for keys,values in achi.items():
        todolist.append([keys+i,values|{i}])
    for j in todolist:
        my_add(j[0],j[1])
    todolist=[]
ans=list(achi[x])
ans.sort()
print(len(ans))
if ans:
    for i in ans:
        print(i,end=' ')
