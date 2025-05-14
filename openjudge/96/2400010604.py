from collections import deque

def solve():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        
        adj = [[] for _ in range(26)]
        in_degree = [0] * 26
        determined = False
        inconsistency = False
        result_sequence = []
        step = 0
        
        for _ in range(m):
            relation = input().strip()
            if determined or inconsistency:
                continue
            step += 1
            u = ord(relation[0]) - ord('A')
            v = ord(relation[2]) - ord('A')
            adj[u].append(v)
            in_degree[v] += 1
            
            temp_in_degree = in_degree.copy()
            temp_adj = [lst.copy() for lst in adj]
            queue = deque()
            for i in range(n):
                if temp_in_degree[i] == 0:
                    queue.append(i)
            
            sequence = []
            unique = True
            while queue:
                if len(queue) > 1:
                    unique = False
                u = queue.popleft()
                sequence.append(u)
                for v in temp_adj[u]:
                    temp_in_degree[v] -= 1
                    if temp_in_degree[v] == 0:
                        queue.append(v)
            
            if len(sequence) != n:
                inconsistency = True
            elif unique and not determined:
                determined = True
                result_sequence = sequence
        
        if inconsistency:
            print(f"Inconsistency found after {step} relations.")
        elif determined:
            sorted_sequence = ''.join([chr(ord('A') + i) for i in result_sequence])
            print(f"Sorted sequence determined after {step} relations: {sorted_sequence}.")
        else:
            print("Sorted sequence cannot be determined.")

solve()