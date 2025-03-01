def has_cycle(n, edges):
    # 初始化邻接表
    adj_list = {i: [] for i in range(n)}
    for u, v in edges:
        adj_list[u].append(v)
    
    # 初始化访问状态数组
    visited = [False] * n
    rec_stack = [False] * n
    
    # 定义DFS函数
    def dfs(v):
        if rec_stack[v]:
            return True
        if visited[v]:
            return False
        
        visited[v] = True
        rec_stack[v] = True
        
        for neighbor in adj_list[v]:
            if dfs(neighbor):
                return True
        
        rec_stack[v] = False
        return False
    
    # 对每个顶点进行DFS
    for i in range(n):
        if not visited[i]:
            if dfs(i):
                return "yes"
    
    return "no"

def main():
    map_list = None
    n, m = map(int, input().split())
    map_list = [n, []]
    for _ in range(m):
        begin, end = map(int, input().split())
        map_list[1].append([begin, end])
    print(has_cycle(map_list[0], map_list[1]))
    new_map = True
        


if __name__ == "__main__":
    main()
