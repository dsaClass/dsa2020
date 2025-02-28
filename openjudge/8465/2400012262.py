def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        n = int(input[idx])
        m = int(input[idx+1])
        x = int(input[idx+2])
        y = int(input[idx+3])
        idx +=4
        
        visited = [[False for _ in range(m)] for _ in range(n)]
        total = n * m
        count = 0
        visited[x][y] = True
        
        directions = [ (2,1), (2,-1), (-2,1), (-2,-1),
                    (1,2), (1,-2), (-1,2), (-1,-2) ]
        
        def dfs(current_x, current_y, step):
            nonlocal count
            if step == total:
                count += 1
                return
            for dx, dy in directions:
                nx = current_x + dx
                ny = current_y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dfs(nx, ny, step + 1)
                    visited[nx][ny] = False
        
        dfs(x, y, 1)
        print(count)

if __name__ == "__main__":
    main()
