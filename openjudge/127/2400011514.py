import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    index = 0
    results = []
    while index < len(data):
        n = int(data[index]); index += 1
        if n == 0:
            break
            
        INF = 10**9
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
            
        for i in range(n):
            m = int(data[index]); index += 1
            for j in range(m):
                contact = int(data[index]); index += 1
                time = int(data[index]); index += 1
                contact_index = contact - 1
                dist[i][contact_index] = time
                
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
        best_start = -1
        min_max_time = INF
        has_valid = False
        
        for i in range(n):
            current_max = 0
            valid = True
            for j in range(n):
                if dist[i][j] == INF:
                    valid = False
                    break
                if dist[i][j] > current_max:
                    current_max = dist[i][j]
                    
            if valid:
                has_valid = True
                if current_max < min_max_time:
                    min_max_time = current_max
                    best_start = i
                    
        if not has_valid:
            results.append("disjoint")
        else:
            results.append(f"{best_start+1} {min_max_time}")
            
    for res in results:
        print(res)

if __name__ == "__main__":
    main()