T, M = map(int, input().split())
P = []
N = []
for _ in range(T):
    p, n = map(int, input().split())
    P.append(p)
    N.append(n)

if T == 0:
    print(0)
else:
    # 初始化动态规划数组，dp_b[i]表示第i个月在北京时的最大收入，dp_n[i]表示在南京时的最大收入
    dp_b = [0] * T
    dp_n = [0] * T
    dp_b[0] = P[0]
    dp_n[0] = N[0]
    
    for i in range(1, T):
        # 当前在北京，前一次可以在北京或者南京
        dp_b[i] = max(dp_b[i-1] + P[i], dp_n[i-1] + P[i] - M)
        # 当前在南京，前一次可以在南京或者北京
        dp_n[i] = max(dp_n[i-1] + N[i], dp_b[i-1] + N[i] - M)
    
    print(max(dp_b[-1], dp_n[-1]))