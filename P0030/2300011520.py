def yuesefu(n,m):
    monkeys=list(range(1,n+1))
    #模拟问题的进行
    while len(monkeys)>1:
        for i in range(m-1):
            monkeys.append(monkeys.pop(0))
        monkeys.pop(0)
    return monkeys[0]
while True:#无限循环
    n, m = map(int, input().split())
    if n==0 and m==0:
        break
    else:
        print(yuesefu(n,m))