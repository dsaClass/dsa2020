def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    nums = list(map(int, data[2:2 + N]))
    operations = data[2 + N:]
    
    delta = 0
    results = []
    
    for i in range(0, len(operations), 2):
        op = operations[i]
        value = int(operations[i + 1])
        
        if op == 'C':
            delta = (delta + value) % 65536
        elif op == 'Q':
            count = 0
            for num in nums:
                if (num + delta) & (1 << value):
                    count += 1
            results.append(count)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    solve()