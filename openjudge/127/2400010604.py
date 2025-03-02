import sys
import math

def main():
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break
        # 初始化邻接矩阵
        INF = math.inf
        dist = [[INF for _ in range(n+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            dist[i][i] = 0
        # 读取每个股票经纪人的信任关系
        for i in range(1, n+1):
            parts = list(map(int, sys.stdin.readline().split()))
            m = parts[0]
            for j in range(m):
                contact = parts[1 + 2*j]
                time = parts[1 + 2*j + 1]
                dist[i][contact] = time
        # Floyd-Warshall算法计算最短路径
        for k in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        # 选择最优起点
        min_time = INF
        best_broker = -1
        for i in range(1, n+1):
            max_time = 0
            disjoint = False
            for j in range(1, n+1):
                if dist[i][j] == INF:
                    disjoint = True
                    break
                if dist[i][j] > max_time:
                    max_time = dist[i][j]
            if not disjoint and max_time < min_time:
                min_time = max_time
                best_broker = i
        # 输出结果
        if best_broker == -1:
            print("disjoint")
        else:
            print(best_broker, min_time)

if __name__ == "__main__":
    main()