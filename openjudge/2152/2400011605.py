from collections import deque

def bfs(A, B, C):
    queue = deque([((0, 0), [])])
    visited = {(0, 0)}

    while queue:
        (a, b), path = queue.popleft()
        if a == C or b == C:
            print(len(path))
            for PATH in path:
                print(PATH)
            return
        
        #FILL(1)
        if (A, b) not in visited:
            visited.add((A, b))
            queue.append(((A, b), path + ["FILL(1)"]))
        #FILL(2)
        if (a, B) not in visited:
            visited.add((a, B))
            queue.append(((a, B), path + ["FILL(2)"]))
        #DROP(1)
        if (0, b) not in visited:
            visited.add((0, b))
            queue.append(((0, b), path + ["DROP(1)"]))
        #DROP(2)
        if (a, 0) not in visited:
            visited.add((a, 0))
            queue.append(((a, 0), path + ["DROP(2)"]))
        #POUR(1, 2)
        new_a = a - min(a, B - b)
        new_b = b + min(a, B - b)
        if (new_a, new_b) not in visited:
            visited.add((new_a, new_b))
            queue.append(((new_a, new_b), path + ["POUR(1,2)"]))
        #POUR(2, 1)
        new_a = a + min(b, A - a)
        new_b = b - min(b, A - a)
        if (new_a, new_b) not in visited:
            visited.add((new_a, new_b))
            queue.append(((new_a, new_b), path + ["POUR(2,1)"]))
        
    print("impossible")
    return

A, B, C = map(int, input().split())
bfs(A, B, C)