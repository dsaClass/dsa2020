n , k = map(int,input().split())
datas = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    datas[i].append(i)
datas.sort()
data = datas[n-k:]
data.sort(key = lambda x : x[1])
print(data[-1][-1]+1)
