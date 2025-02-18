def josephus(n, m):
    monkeys = list(range(1, n + 1))
    index = 0  
    while len(monkeys) > 1:
        index = (index + m - 1) % len(monkeys)
        monkeys.pop(index)
    return monkeys[0]
n, m = map(int, input().split())
while n+m!=0:
    print(josephus(n,m))
    n, m = map(int, input().split())
    
