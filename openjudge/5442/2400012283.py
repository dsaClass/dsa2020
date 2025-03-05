import sys


def prim(dic, n):
    key = {chr(65 + i): sys.maxsize for i in range(n)}
    mstSet = {chr(65 + i): False for i in range(n)}
    parent = {chr(65 + i): None for i in range(n)}
    key['A'] = 0
    for _ in range(n):
        min_key = sys.maxsize
        min_node = None
        for v in key:
            if not mstSet[v] and key[v] < min_key:
                min_key = key[v]
                min_node = v
        mstSet[min_node] = True
        for neighbor, weight in dic[min_node].items():
            if not mstSet[neighbor] and weight < key[neighbor]:
                key[neighbor] = weight
                parent[neighbor] = min_node
    return sum(key.values())


n = int(input())
dic = {chr(65 + i): {} for i in range(n)}
for i in range(n - 1):
    line = input().split()
    node = line[0]
    num_edges = int(line[1])
    for j in range(num_edges):
        neighbor = line[2 + j * 2]
        weight = int(line[2 + j * 2 + 1])
        dic[node][neighbor] = weight
        dic[neighbor][node] = weight
print(prim(dic, n))
