import heapq
import sys

input = sys.stdin.read
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 4 个方向：上、下、左、右

class Node:
    def __init__(self, x, y, time, key, snake):
        self.x = x  # 当前位置
        self.y = y  # 当前位置
        self.time = time  # 当前耗费时间
        self.key = key  # 当前拿到的钥匙数量
        self.snake = snake  # 当前杀死的蛇的状态（用 bitmask 记录）

    def __lt__(self, other):
        return self.time < other.time  # 优先队列需要按照时间排序（Dijkstra）

def bfs(maze, N, M):
    # 记录初始位置和蛇的位置
    x0, y0, snake_count = 0, 0, 0
    snake_map = [[-1] * N for _ in range(N)]  # 记录蛇的编号
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 'K':  # 孙悟空的起点
                x0, y0 = i, j
            elif maze[i][j] == 'S':  # 记录蛇的位置
                snake_map[i][j] = snake_count
                snake_count += 1

    # Dijkstra 需要的优先队列
    queue = []
    heapq.heappush(queue, Node(x0, y0, 0, 0, 0))

    # 记录访问状态：memo[x][y][key_count] 表示在 (x, y) 拥有 key_count 把钥匙的最短时间
    INF = float('inf')
    memo = [[[INF] * (M + 1) for _ in range(N)] for _ in range(N)]
    memo[x0][y0][0] = 0  # 初始状态

    while queue:
        node = heapq.heappop(queue)

        # 遍历四个方向
        for dx, dy in DIRS:
            nx, ny = node.x + dx, node.y + dy
            if 0 <= nx < N and 0 <= ny < N:
                cell = maze[nx][ny]
                new_time = node.time + 1
                new_key = node.key
                new_snake_mask = node.snake

                if cell == '#':  # 死亡房间，不能进入
                    continue
                elif cell == 'S':  # 遇到蛇
                    snake_id = snake_map[nx][ny]
                    if (node.snake & (1 << snake_id)):  # 已杀死，正常通行
                        pass
                    else:  # 需要额外 1 分钟杀死蛇
                        new_time += 1
                        new_snake_mask |= (1 << snake_id)
                elif cell.isdigit():  # 遇到钥匙
                    key_id = int(cell)
                    if key_id == node.key + 1:  # 必须按顺序拾取
                        new_key += 1
                elif cell == 'T' and new_key == M:  # 唐僧，并且钥匙足够
                    return new_time

                # 如果新的状态更优，则更新
                if new_time < memo[nx][ny][new_key]:
                    memo[nx][ny][new_key] = new_time
                    heapq.heappush(queue, Node(nx, ny, new_time, new_key, new_snake_mask))

    return "impossible"  # 无法到达

# 读取输入
def main():
    input_data = input().strip().split("\n")
    index = 0
    results = []
    
    while index < len(input_data):
        # 读取 N, M
        N, M = map(int, input_data[index].split())
        if N == 0 and M == 0:
            break
        
        # 读取宫殿地图
        maze = [list(input_data[i]) for i in range(index + 1, index + 1 + N)]
        results.append(str(bfs(maze, N, M)))

        # 更新索引
        index += N + 1

    # 输出结果
    print("\n".join(results))

if __name__ == "__main__":
    main()