'''
基础知识 & 经典代码·1
'''

#ADT Graph的实现
#包含两个类，VertBase用于记录顶点/顶点连接边的信息,Graph用于构造图，保存了包含所有顶点的主表
class VertBase:
    def __init__(self,key):
        self.id=key
        self.connectedTo={}
        self.inDegree=0
        self.outDegree=0
    def addNeighbor(self,nbr,weight=1):
        #添加从当前节点到nbr节点的有向边
        #添加重复边以增加其权值，不影响节点出入度
        if nbr not in self.connectedTo:
            self.outDegree+=1
            nbr.inDegree+=1
        self.connectedTo[nbr]=weight
    def delNeighbor(self,nbr):
        if nbr in self.connectedTo:
            self.outDegree-=1
            nbr.inDegree-=1
            del (self.connectedTo[nbr]) #为什么要加括号？
    def __str__(self):
        return f"{self.id}({self.inDegree}:{self.outDegree})"

    __repr__=__str__

    def getConnection(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    #__str__可以在print(obj),str(obj)调用下，返回用户友好的节点状态描述
    #__repr__用于交互式环境/容器内对象显示，与__str__一致，便于调试

class Graph:
    def __init__(self):
        self.vertList={}
        self.numVertices=0
    def addVertex(self,key):
        self.numVertices+=1
        newVertice=VertBase(key)
        self.vertList[key]=newVertice
        return newVertice
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    def __contains__(self,n):
        return n in self.vertList #检测特定元素是否是图的顶点
    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv=self.addVertex(f)
        if t not in self.vertList:
            nv=self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],cost)

    def getVertices(self):
        return self.vertList.keys()
    def __iter__(self):
        return iter(self.vertList.values())

g=Graph()
for i in range(10):
    g.addVertex(i)
g.addEdge(0,1,5)

#广度优先搜索(BFS)与深度优先搜索(DFS)
#核心：表示出边的连接关系；设置一个列表反映该点是否被遍历过
#Eg. 广度优先搜索
'''
while queue:
        cr,cc,time=queue.popleft()
        for dr,dc in moves:
            nr,nc=cr+dr,cc+dc
            if 0<=nr<=r-1 and 0<=nc<=c-1 and not visited_mapp[nr][nc]:
                if nr==er and nc==ec:
                    print(time+1)
                    found=True
                    break
                elif mapp[nr][nc]:
                    visited_mapp[nr][nc]=1
                    queue.append((nr,nc,time+1))
        if found:   #这个判定很重要！
            break
    if not found:
        print("oop!")
'''

#无向带权图的最短路径问题：Dijkstra算法（边权非负）
import heapq

def dijkstra(graph,start):
    distances={node:int("inf") for node in graph}   #保存了现有的起始点到终点的最短路径
    distances[start]=0

    queue=[(0,start)]
    while queue:
        current_dist,current_node=heapq.heappop(queue)  #弹出这条搜索路径下的路径之和
        if current_dist>distances[current_node]:
            continue
        for neighbor,weight in graph[current_node].items():
            distance=current_dist+weight
            if distances[neighbor]>distance:
                distances[neighbor]=distance
                heapq.heappush(queue,(distance,neighbor))
    return distances


#无向带权图的最小生成树问题
edges=[('A', 'B', 12), ('A', 'I', 25), ('B', 'C', 10),
       ('B', 'H', 40), ('B', 'I', 8), ('C', 'D', 18),
       ('C', 'G', 55), ('D', 'E', 44), ('E', 'F', 60),
       ('E', 'G', 38), ('G', 'H', 35), ('H', 'I', 35)]
n=9
node_index=[chr(ord("A")+i) for i in range(n)]

edges.sort(key=lambda x:x[2])
total_cost=0
edge_count=0

#构建最小子树
parent=[_ for _ in range(n)]  #根节点列表初始化：每个结点独立
rank=[0]*n  #每个节点所在树的高度

def find(x):  #寻找结点的根结点
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):   #按秩合并，总是将小树合并到大树下
    rx,ry=find(x),find(y)
    if rx==ry:
        return False
    if rank[rx]<rank[ry]:
        parent[rx]=ry
    elif rank[ry]<rank[rx]:
        parent[ry]=rx
    else:
        parent[ry]=rx
        rank[rx]+=1  #秩的计算其实是扁平的，无法反映真实的树高
    return True

for u,v,weight in edges:  #贪心算法，从最短边开始处理
    u_idx=node_index[u]
    v_idx=node_index[v]
    if find(u_idx)!=find(v_idx): #如果根相同，则已经合并，不做处理
        union(u_idx,v_idx)  #如果根不同，加以合并
        edge_count+=1
        total_cost+=weight

        if edge_count==n-1:
            break


'''
作业题
'''
#7218 献给阿尔吉侬的花束
#计算迷宫最短路径长度：BFS搜索
#BFS有天然优势，可以按层级向下伸展
from collections import deque

t = int(input())
for _ in range(t):
    r, c = map(int, input().split())
    mapp = [[1 for _ in range(c)] for _ in range(r)]
    visited_mapp=[[0 for _ in range(c)] for _ in range(r)]
    sr, sc = 0, 0
    er, ec = 0, 0
    for i in range(r):
        a = list(str(input()))
        for j in range(len(a)):
            if a[j] == "S":
                sr, sc = i, j
            elif a[j] == "E":
                er, ec = i, j
            elif a[j] == "#":
                mapp[i][j] = 0

    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue=deque()
    queue.append((sr, sc,0))
    found=False

    while queue:
        cr,cc,time=queue.popleft()
        for dr,dc in moves:
            nr,nc=cr+dr,cc+dc
            if 0<=nr<=r-1 and 0<=nc<=c-1 and not visited_mapp[nr][nc]:
                if nr==er and nc==ec:
                    print(time+1)
                    found=True
                    break
                elif mapp[nr][nc]:
                    visited_mapp[nr][nc]=1
                    queue.append((nr,nc,time+1))
        if found:   #这个判定很重要！
            break
    if not found:
        print("oop!")


#5443 兔子与樱花
import heapq

p=int(input())
vertices=[]
for _ in range(p):
    vertice=input()
    vertices.append(vertice)

q=int(input())
edges=[[] for _ in range(p)]
for _ in range(q):
    f,t,length=input().split()
    f=vertices.index(f)
    t=vertices.index(t)
    edges[f].append((t,int(length)))
    edges[t].append((f,int(length)))

r=int(input())
for _ in range(r):
    strf,strt=input().split()
    f=vertices.index(strf)
    t=vertices.index(strt)

    if f==t:
        print(strf)
        continue

    #初始化距离与前驱数组
    inf=10**18
    dist=[inf]*p
    prev_node=[-1]*p
    prev_weight=[0]*p

    dist[f]=0
    queue=[(0,f)]

    while queue:
        current_dist,u=heapq.heappop(queue)
        if current_dist!=dist[u]:  #不需要处理比当前路径更长的路径
            continue
        if u==t:
            break

        for v,w in edges[u]:
            new_dist=current_dist+w
            if new_dist<dist[v]:
                dist[v]=new_dist
                prev_node[v]=u
                prev_weight[v]=w
                heapq.heappush(queue,(new_dist,v))

    #回溯构建路径
    path=[]
    current=t
    while current!=f:
        path.append((vertices[current],prev_weight[current]))
        current=prev_node[current]
    path.append(vertices[f])
    path.reverse()

    result=path[0]
    for i in range(1,len(path)):
        node_name,weight=path[i]
        result+="->({})->{}".format(weight,node_name)

    print(result)

#1817 城堡问题
#深度优先搜索，注意题目给出迷宫的转化问题与方向对应问题

r=int(input())
c=int(input())
lst=[]
for _ in range(r):
    lst.append(list(map(int,input().split())))
castle=[[[] for _ in range(c)] for _ in range(r)]
visited_castle=[[0 for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        walls=[]
        wall=lst[i][j]
        while wall:
            walls.append(wall%2)
            wall//=2
        while len(walls)<4:
            walls.append(0)
        castle[i][j]=walls

def dfs(r,c):
    size=1
    visited_castle[r][c]=1
    row=len(castle)
    col=len(castle[0])
    moves=[(1,0,3), (0, 1,2), (-1, 0,1), (0, -1,0)]
    for dr,dc,direction in moves:
        if not castle[r][c][direction]:
            nr,nc=r+dr,c+dc
            if 0<=nr<=row-1 and 0<=nc<=col-1 and not visited_castle[nr][nc]:
                size+=dfs(nr,nc)
    return size

sizes=[]
for i in range(r):
    for j in range(c):
        if not visited_castle[i][j]:
            size=dfs(i,j)
            sizes.append(size)

print(len(sizes))
print(max(sizes))


#323 棋盘问题
#一种思路：将其转化为图的边数求解问题

while True:
    #读入数据，表示棋盘
    n,kk=map(int,input().split())
    if n==-1 and k==-1:
        break
    vertices=[]
    visited_vertices=[0 for _ in range(n)]
    edges={_:[] for _ in range(n)}
    for i in range(n):
        row=list(input())
        for j in range(n):
            if row[j]=="#":
                vertices.append([i,j])
    for k in range(len(vertices)):
        for l in range(len(vertices)):
            if vertices[k][0]!=vertices[l][0] and vertices[k][1]!=vertices[l][1]:
                edges[k].append(l)

    ans=[]
    def dfs(vertice_idx,path):
        global ans
        path.append(vertice_idx)
        if len(path)==kk:
            path.sort()
            if path not in ans:
                ans.append(path)
            return

        visited_vertices[vertice_idx]=1
        for e in edges[vertice_idx]:
            e_idx=vertices.index(e)
            if not visited_vertices[e_idx]:
                visited_vertices[e_idx]=1
                path.append(e_idx)
                dfs(e,path)
        visited_vertices[vertice_idx]=0

    for i in range(n):
        if visited_vertices[i]==0:
            dfs(i,[])
    print(len(ans))
'''
#另一种思路：直接递归，处理每一行的时候分两种情况：在这一行放棋子或不放棋子

while True:
    n,k=map(int,input().split())
    if n==-1 and k==-1:
        break
    board=[]
    visited=[0 for _ in range(n)]
    for _ in range(n):
        board.append(list(input()))

    def dfs(r,count):
        if count==k:
            return 1
        if r==n:
            return 0
        if n-r+count<k:
            return 0

        total_ways=dfs(r+1,count)  #对应不在这层放棋子
        for i in range(n):
            if board[r][i]=="#" and not visited[i]:   #对应在这层放棋子
                visited[i]=1
                total_ways+=dfs(r+1,count+1)
                visited[i]=0
        return total_ways

    total_ways=dfs(0,0)
    print(total_ways)
'''
#4980 拯救行动
#矩阵法表示的图的广度优先搜索

import heapq

s=int(input())
for _ in range(s):
    #转化地图
    r,c=map(int,input().split())
    mapp=[]
    fr,fc=-1,-1
    tr,tc=-1,-1
    for _ in range(r):
        mapp.append(list(input()))
    for i in range(r):
        for j in range(c):
            if mapp[i][j]=="@":
                mapp[i][j]=1
            elif mapp[i][j]=="a":
                mapp[i][j]=1
                tr,tc=i,j
            elif mapp[i][j]=="r":
                mapp[i][j]=1
                fr,fc=i,j
            elif mapp[i][j]=="x":
                mapp[i][j]=2
            else:
                mapp[i][j]=0

    #广度优先搜索
    queue=[(0,fr,fc)]
    moves=[(1,0),(0,1),(-1,0),(0,-1)]
    inf=10**9
    distances=[[inf for _ in range(c) ] for _ in range(r)]
    distances[fr][fc]=0

    while queue:
        distance,curr_r,curr_c=heapq.heappop(queue)  #注意数组的第一个元素是堆比较的元素
        if distance>distances[curr_r][curr_c]:
            continue
        if curr_c==tc and curr_r==tr:
            print(distances[curr_r][curr_c])
            break

        for dr,dc in moves:
            nr,nc=curr_r+dr,curr_c+dc
            if 0<=nr<=r-1 and 0<=nc<=c-1 and mapp[nr][nc]:
                curr_dist=distance+mapp[nr][nc]
                if curr_dist<distances[nr][nc]:
                    distances[nr][nc]=curr_dist
                    heapq.heappush(queue,(curr_dist,nr,nc))

    else:
        print("Impossible")

'''

#5442 兔子与星空
#生成一个无向带权图的最小子树，并返回最小权值和
'''
n=int(input())
edges=[]
node_index={}
#创建节点到索引的映射
for i in range(n):
    node_index[chr(ord("A")+i)]=i

#建图
for _ in range(n-1):
    a=list(input().split())
    u=a[0]
    nums=int(a[1])
    index=2
    for _ in range(nums):
        v=a[index]
        weight=int(a[index+1])
        index+=2
        edges.append((u,v,weight))
print(edges)
edges.sort(key=lambda x:x[2])
total_cost=0
edge_count=0

#构建最小子树
parent=[_ for _ in range(n)]  #根节点列表初始化：每个结点独立
rank=[0]*n  #每个节点所在树的高度

def find(x):  #寻找结点的根结点
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):   #按秩合并，总是将小树合并到大树下
    rx,ry=find(x),find(y)
    if rx==ry:
        return False
    if rank[rx]<rank[ry]:
        parent[rx]=ry
    elif rank[ry]<rank[rx]:
        parent[ry]=rx
    else:
        parent[ry]=rx
        rank[rx]+=1  #秩的计算其实是扁平的，无法反映真实的树高
    return True

for u,v,weight in edges:  #贪心算法，从最短边开始处理
    u_idx=node_index[u]
    v_idx=node_index[v]
    if find(u_idx)!=find(v_idx): #如果根相同，则已经合并，不做处理
        union(u_idx,v_idx)  #如果根不同，加以合并
        edge_count+=1
        total_cost+=weight

        if edge_count==n-1:
            break
print(total_cost)




