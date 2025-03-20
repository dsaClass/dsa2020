def find_min(lst):
    total=sum(lst)
    sorted_lst=sorted(lst,reverse=True)
    used=[False]*len(lst)
    def dfs(start,curr,target,count):
        if count==total//target:
            return True
        if curr==target:
            return dfs(0,0,target,count+1)
        pre_fail=-1#用来剪枝
        for i in range(start,len(lst)):
            if not used[i] and sorted_lst[i]!=pre_fail:#剪枝,用过的不再探索，之前失败过的也不再探索
               if curr+sorted_lst[i]>target:
                   continue
               used[i]=True#进行探索，尝试使用这个棍
               if dfs(i+1,curr+sorted_lst[i],target,count):
                   return True
               used[i]=False#如果使用这个棍不行，就进行回溯
               pre_fail=sorted_lst[i]#记录失败的棍
               if curr==0:#剪枝，第一根棍都拼不上
                   break
    for t in range(sorted_lst[0],total//2+1):
        if total%t!=0:
            continue
        if dfs(0,0,t,0):
            return t
    return total
while True:
    n=int(input())
    if n==0:
        break
    sticks=list(map(int,input().split()))
    print(find_min(sticks))