import sys
sys.setrecursionlimit(10000)

from copy import deepcopy
n,m=map(int,input().split())
graph=[[0]*n for _ in range(n)]
graph.append([1]*n)
for _ in range(m):
    x1,x2=map(int,input().split())
    graph[x1][x2]=graph[x2][x1]=1


def deep(current_node,s:list):
    global graph1
    for i in range(n + 1):
        if current_node < n:
            graph1[i][current_node] = 0
    # print(current_node,graph1)
    if 1 not in graph1[current_node]:
        return True,s
    
    else:
        next_node = int(s[0])
        
        if graph1[current_node][next_node]==0:
            return False,s
        else:
            t=deep(next_node,s[1:])
            if not t[0]:
                return False,s
            else:
                return deep(current_node, t[1])


k=int(input())
for _ in range(k):
    graph1=deepcopy(graph)
    l=list(map(int,input().split()))
    t=deep(n,l)
    if t[0]:
        print('YES')
    else:
        print('NO')