
#DFS样例：走迷宫（给出所有解）
dirs = [(-1,0), (1,0), (0,-1), (0,1)]  # 上下左右四个方向
def dfs(x, y, path):
    if (x, y) == (ex, ey):
        all_paths.append(list(path))  # 注意要深拷贝当前路径
        return
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and maze[nx][ny] != '#':  #可走的判定
            visited[nx][ny] = True
            path.append((nx, ny))
            dfs(nx, ny, path)
            path.pop()                # 回溯
            visited[nx][ny] = False   # 回溯 注意：如果要剪枝，需要保留这行代码清理列表。


#求解的数量
count=0
def dfs(x, y):
    global count
    if (x, y) == (ex, ey):
        count+=1
        return
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and maze[nx][ny] != '#':
            visited[nx][ny] = True
            dfs(nx, ny)
            visited[nx][ny] = False

# 输入处理
T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    maze = [list(input().strip()) for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'S':
                sx, sy = i, j
            elif maze[i][j] == 'E':
                ex, ey = i, j

    visited = [[False]*C for _ in range(R)]
    visited[sx][sy] = True
    all_paths = []  # 存储所有路径
    dfs(sx, sy, [(sx, sy)])

    # 输出所有路径
    if not all_paths:
        print("oop!")
    else:
        for path in all_paths:
            print(path)



#BFS样例：迷宫最短路径
S=int(input())
from collections import deque
def count(n,m,l):
    global visited,step,prev
    for i in range(n):
        for j in range(m):
            if l[i][j]=='r':
                rx,ry=i,j
            elif l[i][j]=='a':
                ax,ay=i,j

    q=deque()
    visited=set()

    prev = [[None] * m for _ in range(n)]
    step=0
    q.append((rx,ry,0))
    visited.add((rx,ry))
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    while q:
        x,y,step=q.popleft()
        for dx,dy in dirs:
            newx,newy=x+dx,y+dy
            if newx==ax and newy==ay:
                #prev[newx][newy] = (x, y)
                return step+1
            if (newx,newy) not in visited and 0<=newx<n and 0<=newy<m and l[newx][newy]!='#':
                visited.add((newx,newy))
                #prev[newx][newy] = (x, y)
                q.append((newx,newy,step+1))
    return 'Impossible'

#输出最短路径：利用prev
def reconstruct_path():
    path = []
    curr = (n-1,m-1)
    while curr:
        path.append(curr)
        curr = prev[curr[0]][curr[1]]
    path.reverse()
    return path


ans=[]
for i in range(S):
    n,m=map(int,input().split())
    l=[input() for _ in range(n)]
    ans.append(count(n,m,l))
for i in ans:
    print(i)
    

#dijkstra算法（带权图找最短路径）
import heapq

def dijkstra(n, edges, start):
#edges为邻接表，n为节点数，start为起始点
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n

    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True

        for v, w in edges[u]:
            if not visited[v] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist


#DFS找连通块
visited = [[False] * n for _ in range(m)]

def dfs(x, y):
    """返回以 (x, y) 为根的连通块大小"""
    stack = [(x, y)]
    visited[x][y] = True
    size = 0
    while stack:
        i, j = stack.pop()
        size += 1
        cell = l[i][j]
        for dx, dy, wall in dirs:
            ni, nj = i + dx, j + dy
            # 越界或有墙则不可通行
            if 0 <= ni < m and 0 <= nj < n and not (cell & wall):
                if not visited[ni][nj]:
                    visited[ni][nj] = True
                    stack.append((ni, nj))
    return size

rooms = 0
max_room = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            rooms += 1
            max_room = max(max_room, dfs(i, j))
print(rooms)
print(max_room)


#并查集判断连通性，适用于动态加边
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # 连通块数量，初始为 n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False  # 已经连通，不改变连通块数量
        # 否则合并集合
        if self.rank[fx] < self.rank[fy]:
            self.parent[fx] = fy
        else:
            self.parent[fy] = fx
            if self.rank[fx] == self.rank[fy]:
                self.rank[fx] += 1
        self.count -= 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def is_connected_graph(self):
        return self.count == 1

    def get_connected_components(self):
        return self.count

uf = UnionFind(n)  # 初始有n个点，0~n-1。后每次加入一个点并判断

edges = []
for i, (u, v) in enumerate(edges):
    uf.union(u, v)
    print(f"加入边 ({u}, {v}) 后，连通块数 = {uf.get_connected_components()}")
    if uf.is_connected_graph():
        print(f"  图在第 {i+1} 条边加入后已经连通了。")


#判断有向图是否有环
def has_cycle_directed(graph):
    n = len(graph)
    status = [0] * n  

    def dfs(u):
        status[u] = 1  # 正在访问
        for v in graph[u]: #遍历和u连接的点
            if status[v] == 0:
                if dfs(v): return True
            elif status[v] == 1:
                return True  # 发现回边：有环
        status[u] = 2  # 访问完成
        return False

    for u in range(n):
        if status[u] == 0:
            if dfs(u): return True
    return False


#判断无向图是否有环  输入为每个节点相连的点[[v1,v2],[v3,v4]]
def has_cycle_undirected(graph):
    n = len(graph)
    visited = [False] * n

    def dfs(u, parent):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True  # 访问到已访问、非父节点 → 有环
        return False

    for i in range(n):  # 多个连通分量时
        if not visited[i]:
            if dfs(i, -1):  # 初始节点无父亲
                return True
    return False


#拓扑排序(KAHN)  输入为邻接表
from collections import deque
def kahn_topo_sort(n, edges):
    adj = [[] for _ in range(n)]
    in_deg = [0] * n

    for u, v in edges:
        adj[u].append(v)  #从u出发的边
        in_deg[v] += 1    #入度

    q = deque([i for i in range(n) if in_deg[i] == 0])
    res = []

    in_degnew=in_deg.copy()
    while q:
        if len(q) > 1:
            print("拓扑序不唯一")
            break
        u = q.popleft()
        res.append(u)
        for v in adj[u]:
            in_degnew[v] -= 1
            if in_degnew[v] == 0:
                q.append(v)    #入度为0时加入队列

    if len(res) != n:
        print("图中存在环")
        return None
    return res


#最小生成树
#使用并查集
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # 每个节点的初始父节点是自己

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False  # 说明已经连通，不能再连接（避免成环）
        self.parent[fx] = fy  # 合并两个集合
        return True
    
def kruskal(n, edge_list):
    """
    n: 节点数（编号从 0 到 n-1）
    edge_list: 边集合，每条边是 (weight, u, v)
    返回：最小生成树的总权值；若图不连通返回 None
    """
    # 1. 边按权重排序
    edge_list.sort()
    
    uf = UnionFind(n)
    mst_weight = 0
    edge_count = 0

    # 2. 遍历每条边
    for weight, u, v in edge_list:
        if uf.union(u, v):  # 若不成环
            mst_weight += weight
            edge_count += 1
            if edge_count == n - 1:  # 已选 n-1 条边
                break

    if edge_count < n - 1:
        return None  # 图不连通，无法形成生成树
    return mst_weight


#构建图
import heapq
from collections import deque

class Graph:
    def __init__(self, num_nodes, directed=False):
        self.n = num_nodes
        self.directed = directed
        self.adj = [[] for _ in range(num_nodes)]  # 邻接表：adj[i] 存 (neighbor, weight)

    def add_edge(self, u, v, weight=1): #可用于生成邻接表
        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))

    def print_graph(self):
        for i in range(self.n):
            neighbors = ', '.join(f"{v}({w})" for v, w in self.adj[i])
            print(f"{i} → {neighbors}")

    def get_adjacency_list(self):
        """返回字典形式的邻接表，不含权重"""
        adj_list = {i: [] for i in range(self.n)}
        for u in range(self.n):
            for v, _ in self.adj[u]:
                adj_list[u].append(v)
        return adj_list

    def get_edge_list(self):
        """返回边列表 [(u, v, w), ...]"""
        edges = []
        for u in range(self.n):
            for v, w in self.adj[u]:
                if self.directed or u < v:
                    edges.append((u, v, w))
        return edges

    def get_adjacency_matrix(self):
        """返回邻接矩阵表示（二维列表），不可达为inf"""
        matrix = [[float('inf')] * self.n for _ in range(self.n)]
        for i in range(self.n):
            matrix[i][i] = 0  # 自环距离设为0
        for u in range(self.n):
            for v, w in self.adj[u]:
                matrix[u][v] = w
        return matrix

    def print_adjacency_list(self):
        """打印点邻接列表（无权）"""
        adj_list = self.get_adjacency_list()
        for u in range(self.n):
            neighbors = ', '.join(str(v) for v in adj_list[u])
            print(f"{u} → {neighbors}")

    def print_adjacency_matrix(self):
        """打印邻接矩阵（有权）"""
        matrix = self.get_adjacency_matrix()
        for row in matrix:
            print(' '.join(str(x) if x != float('inf') else '∞' for x in row))

    def print_edge_list(self):
        """打印边列表（有向或无向）"""
        for u, v, w in self.get_edge_list():
            print(f"{u} → {v} (weight={w})")

    # ===== DFS =====
    def dfs(self, start):
        visited = [False] * self.n
        result = []

        def dfs_visit(u):
            visited[u] = True
            result.append(u)
            for v, _ in self.adj[u]:
                if not visited[v]:
                    dfs_visit(v)

        dfs_visit(start)
        return result

    # ===== BFS =====
    def bfs(self, start):
        visited = [False] * self.n
        queue = deque([start])
        result = []
        visited[start] = True

        while queue:
            u = queue.popleft()
            result.append(u)
            for v, _ in self.adj[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        return result

    # ===== Dijkstra（最短路）=====
    def dijkstra(self, start):
        dist = [float('inf')] * self.n
        dist[start] = 0
        visited = [False] * self.n
        pq = [(0, start)]  # (distance, node)

        while pq:
            d, u = heapq.heappop(pq)
            if visited[u]:
                continue
            visited[u] = True
            for v, w in self.adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        return dist

    # ===== 拓扑排序=====
    def topo_sort(self):
        in_deg = [0] * self.n
        for u in range(self.n):
            for v, _ in self.adj[u]:
                in_deg[v] += 1

        queue = deque([u for u in range(self.n) if in_deg[u] == 0])
        result = []

        while queue:
            u = queue.popleft()
            result.append(u)
            for v, _ in self.adj[u]:
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    queue.append(v)

        if len(result) != self.n:
            return None  # 有环
        return result

# 创建一个图，编号为 0~4，共 5 个点
g = Graph(5, directed=True)
g.add_edge(0, 1, 2) #(u,v,weight)
g.add_edge(1, 2, 1)

g.print_graph()
print(g.adj)
