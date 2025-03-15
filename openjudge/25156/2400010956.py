n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
ans = []
k = int(input())
for _ in range(k):
    node = list(map(int, input().split()))
    if len(node) != n:
        ans.append('NO')
        continue
    father = [-1] * n
    # 深度优先遍历其实还是树
    # 多棵树！！
    remain = [i.copy() for i in edges] + [[i for i in range(n)]]
    # 最后一项充当remain[-1]，在一个图搜索完成后可以进入任何一个图
    now = node[0]
    for i in range(n):
        try:
            remain[i].remove(now)
        except:
            continue
    for i in range(1,n):
        while len(remain[now]) == 0:
            now = father[now]
        if node[i] in remain[now]:
            father[node[i]] = now
            now = node[i]
            for i in range(n):
                try:
                    remain[i].remove(now)
                except:
                    continue
        else:
            ans.append('NO')
            break
    else:
        ans.append('YES')
for i in ans:
    print(i)
            

