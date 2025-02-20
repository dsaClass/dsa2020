# 姓名：杨济泽 学号：2200015881
# 本题采用的思路非常简单，即逐步找最大的值并从原列表中剔除该值，因此改进空间很大
# 最终主要卡在了输出上，因此建立了一个新列表进行输出
container=[]
while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    contain_a = []
    contain_b = []
    while len(contain_a) < n-k:
        s = []
        up = sum(contain_a)
        down = sum(contain_b)
        for i in range(len(a)):
            new_a = up + a[i]
            new_b = down + b[i]
            s.append(new_a/new_b)
        t = s.index(max(s))
        contain_a.append(a[t])
        contain_b.append(b[t])
        a.pop(t)
        b.pop(t)
    score = int(sum(contain_a)/sum(contain_b)*100 + 0.5)
    container.append(score)
for i in container:
    print(i)
