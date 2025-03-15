from math import sqrt
n = int(input())
ans = []
# 并查集函数
father = []
level = []
def find_root(node:int):
    global father
    if father[node] == -1:
        return node
    else:
        return find_root(father[node])
    
def union(a:int, b:int):
    global father, level
    root_a = find_root(a)
    root_b = find_root(b)
    if root_a == root_b:
        # 已经联通
        return False
    else:
        if level[root_a] > level[root_b]:
            father[root_b] = root_a
        elif level[root_a] == level[root_b]:
            father[root_b] = root_a
            level[root_a] += 1
        else:
            father[root_a] = root_b
        return True

for sample in range(n):
    s, p = map(int, input().split())
    site = []
    # 按编号储存的站点
    father = [-1] * p
    level = [1] * p
    for i in range(p):
        x, y = map(int, input().split())
        site.append((x, y))
    distance = []
    for i in range(p):
        for j in range(i + 1, p):
            distance.append(((site[i][0] - site[j][0]) ** 2 + (site[i][1] - site[j][1]) ** 2, i, j))
    distance.sort(key = lambda x: x[0])
    real_dis = []
    # 储存派上用场的无限电收发
    for i in distance:
        d, a, b = i
        # 提高可读性
        if union(a, b):
            # 如果a与b仍未相连
            real_dis.append(d)
            # 每次都能多连上一个
        if len(real_dis) == p-1:
            break
    for i in range(s-1):
        real_dis.pop(-1)
    ans.append(real_dis[-1])
for i in ans:
    print(f'{sqrt(i):.2f}')
            